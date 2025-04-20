import logging
from PySide6 import QtWidgets
from PySide6.QtCore import QTimer
from Vista.ui_tabla import Ui_Form
from Control.connection import DB
import csv
from PySide6.QtWidgets import QFileDialog, QMessageBox, QWidget
from Control.connection import DB


class Tabla(QWidget, Ui_Form):
    """Clase para la interfaz de la tabla."""
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.db = DB()

        self.cargar_desde_SQLite()
        
        self.pushButton_Importar.clicked.connect(self.importar_datos_desde_csv)
        self.pushButton_Transform.clicked.connect(self.csv_to_sql)
        self.pushButton_Eliminar.clicked.connect(self.eliminar_datos)
        self.pushButton_Actualizar.clicked.connect(self.cargar_desde_SQLite)

        self.pushButton_Buscar.clicked.connect(self.buscar_alumno)
        # si apretamos el enter en el lineEdit_Buscar se ejecuta la funcion buscar_alumno
        self.lineEdit_Buscar.returnPressed.connect(self.buscar_alumno)
        # al hacer doble click en una celda de la tabla se ejecuta la funcion mostrar_alumnos
        self.tableWidget.cellDoubleClicked.connect(self.mostrar_alumnos)
        
        # Usar un QTimer para ajustar el tamaño después de mostrar la ventana
        # con este pequeño retraso, aseguramos que la tabla esté completamente renderizada
        # antes de ajustar el tamaño de los encabezados y evitamos ligeros desajustes
        QTimer.singleShot(0, self.ajustar_size_encabezados)

    def cargar_desde_SQLite(self):
        """Carga los datos desde la base de datos SQLite y los muestra en la tabla."""
        try:
            # Obtener la conexión a la base de datos
            with DB() as conexion:
                cursor = conexion.cursor()
                query = "SELECT * FROM alumnos"
                # Ejecutar la consulta para obtener los datos de la tabla 'alumnos'
                cursor.execute(query)
                # Obtener los nombres de las columnas
                datos = cursor.fetchall()
                encabezados = [desc[0] for desc in cursor.description]

            # Configurar la tabla con los encabezados
            self.tableWidget.setColumnCount(len(encabezados))
            self.tableWidget.setHorizontalHeaderLabels(encabezados)

            # Limpiar la tabla antes de llenarla
            self.tableWidget.setRowCount(0)

            if not datos:  # Si no hay datos
                self.tableWidget.horizontalHeader().setStretchLastSection(True)
                self.tableWidget.horizontalHeader().setSectionResizeMode(
                    QtWidgets.QHeaderView.Stretch
                )
                return  # Salir del método si no hay datos

            # Poblar la tabla con los datos obtenidos
            for fila_datos in datos:
                fila_actual = self.tableWidget.rowCount()
                self.tableWidget.insertRow(fila_actual)
                for columna, dato in enumerate(fila_datos):
                    self.tableWidget.setItem(
                        fila_actual, columna, QtWidgets.QTableWidgetItem(str(dato))
                    )
            logging.info("Datos cargados desde SQLite")

            self.ajustar_size_encabezados()

        except Exception as e:
            # Mostrar un mensaje de error si ocurre algún problema
            QMessageBox.critical(
                self, "Error", f"No se pudo cargar los datos desde SQLite:\n{str(e)}"
            )

    def importar_datos_desde_csv(self):
        """Importa datos desde un archivo CSV y los muestra en la tabla."""
        # Abrir el cuadro de diálogo para seleccionar el archivo CSV
        ruta_archivo, _ = QFileDialog.getOpenFileName(
            self,
            "Seleccionar archivo CSV",
            "c:/Users/darlb/Desktop/DI08/Modelo",
            "Archivos CSV (*.csv)",
        )
        if not ruta_archivo:  # Si no se selecciona un archivo, salir
            return

        self.ruta_csv = (
            ruta_archivo  # Guardar la ruta del archivo CSV para uso posterior
        )

        try:
            # Abrir el archivo CSV y leer los datos
            with open(ruta_archivo, newline="", encoding="utf-8") as archivo_csv:
                lector_csv = csv.reader(archivo_csv)
                encabezados = next(lector_csv)  # Leer la primera fila como encabezados

                # Configurar la tabla con los encabezados
                self.tableWidget.setColumnCount(len(encabezados))
                self.tableWidget.setHorizontalHeaderLabels(encabezados)

                # Configurar el comportamiento del header para ajustar contenido
                header = self.tableWidget.horizontalHeader()
                header.setStretchLastSection(False)
                for col in range(len(encabezados)):
                    header.setSectionResizeMode(
                        col, QtWidgets.QHeaderView.ResizeToContents
                    )

                # Limpiar la tabla antes de llenarla
                self.tableWidget.setRowCount(0)

                # Poblar la tabla con los datos del CSV
                for fila_datos in lector_csv:
                    fila_actual = self.tableWidget.rowCount()
                    self.tableWidget.insertRow(fila_actual)
                    for columna, dato in enumerate(fila_datos):
                        self.tableWidget.setItem(
                            fila_actual, columna, QtWidgets.QTableWidgetItem(dato)
                        )
                logging.info(f"Datos importados desde {ruta_archivo}")

                self.ajustar_size_encabezados()

        except Exception as e:
            # Mostrar un mensaje de error si ocurre algún problema
            logging.error(f"Error al importar el archivo CSV: {str(e)}")
            QMessageBox.critical(
                self, "Error", f"No se pudo importar el archivo CSV:\n{str(e)}"
            )

    def ajustar_size_encabezados(self):
        """Ajusta tamaño de columnas y filas después del render."""
        self.tableWidget.resizeColumnsToContents()
        self.tableWidget.resizeRowsToContents()

        ancho_total = sum(
            self.tableWidget.columnWidth(i)
            for i in range(self.tableWidget.columnCount())
        )
        self.tableWidget.setMinimumWidth(ancho_total + 30)
        self.adjustSize()

    def eliminar_datos(self):
        """Elimina los datos de la tabla SQLite y llama al método update. qalertdialog
        para confirmar la eliminación.
        """
        respuesta = QMessageBox.question(
            self,
            "Confirmar eliminación",
            "¿Estás seguro de que deseas eliminar todos los datos de la tabla?",
            QMessageBox.Yes | QMessageBox.No,
        )

        if respuesta == QMessageBox.Yes:
            try:
                with DB() as conexion:
                    cursor = conexion.cursor()
                    cursor.execute("DELETE FROM alumnos")

                QMessageBox.information(
                    self, "Éxito", "Todos los datos han sido eliminados correctamente."
                )
                self.cargar_desde_SQLite()

            except Exception as e:
                QMessageBox.critical(
                    self, "Error", f"No se pudieron eliminar los datos:\n{str(e)}"
                )

    def csv_to_sql(self):
        """Convierte el CSV y lo guarda en la base de datos SQLite."""
        # Verificar si ya se seleccionó un archivo CSV
        if not hasattr(self, "ruta_csv") or not self.ruta_csv:
            QMessageBox.warning(
                self,
                "Advertencia",
                "Primero debes importar un archivo CSV desde 'Importar Datos'.",
            )
            return

        try:
            # Abrir el archivo CSV y leer los datos
            with open(self.ruta_csv, newline="", encoding="utf-8") as archivo_csv:
                lector_csv = csv.reader(archivo_csv)
                encabezados = next(lector_csv)  # Leer la primera fila como encabezados

                # Verificar que el archivo CSV tiene las columnas necesarias
                columnas_requeridas = {"ID", "Alumno", "Correo", "UltimoAcceso"}
                if not columnas_requeridas.issubset(set(encabezados)):
                    QMessageBox.critical(
                        self,
                        "Error",
                        "El archivo CSV no contiene las columnas requeridas: ID, Alumno, Correo, ultimoAcceso.",
                    )
                    return

                with DB() as conexion:
                    cursor = conexion.cursor()
                    for fila in lector_csv:
                        cursor.execute(
                            "INSERT INTO alumnos (ID, Alumno, Correo, ultimoAcceso) VALUES (?, ?, ?, ?)",
                            fila,
                        )

                QMessageBox.information(
                    self, "Éxito", "Datos importados correctamente a la base de datos."
                )

        except Exception as e:
            # Mostrar un mensaje de error si ocurre algún problema
            QMessageBox.critical(
                self,
                "Error",
                f"No se pudo importar el archivo CSV a la base de datos:\n{str(e)}",
            )

        except Exception as e:
            # Mostrar un mensaje de error si ocurre algún problema
            QMessageBox.critical(
                self,
                "Error",
                f"No se pudo importar el archivo CSV a la base de datos:\n{str(e)}",
            )

    def mostrar_alumnos(self):
        """Muestra alumno seleccionado aparte en un QMessageBox."""
        fila_seleccionada = self.tableWidget.currentRow()
        if fila_seleccionada == -1:
            QMessageBox.warning(
                self, "Advertencia", "Por favor, selecciona un alumno de la tabla."
            )
            return

        try:
            alumno_id = self.tableWidget.item(fila_seleccionada, 0).text()
            nombre_alumno = self.tableWidget.item(fila_seleccionada, 1).text()
            correo_alumno = self.tableWidget.item(fila_seleccionada, 2).text()
            ultimo_acceso = self.tableWidget.item(fila_seleccionada, 3).text()

            QMessageBox.information(
                self,
                "Alumno seleccionado",
                f"ID: {alumno_id}\nNombre: {nombre_alumno}\nCorreo: {correo_alumno}\nÚltimo Acceso: {ultimo_acceso}",
            )
        except Exception as e:
            QMessageBox.critical(
                self, "Error", f"Error al mostrar el alumno:\n{str(e)}"
            )

    def buscar_alumno(self):
        """Busca un alumno por nombre y muestra los resultados en un QMessageBox."""
        texto_busqueda = self.lineEdit_Buscar.text().strip()
        if not texto_busqueda:
            QMessageBox.warning(
                self, "Advertencia", "Por favor, introduce un nombre para buscar."
            )
            return

        # Normalizar el texto de búsqueda (convertir a minúsculas y eliminar tildes)
        texto_busqueda = texto_busqueda.lower()
        texto_busqueda = (
            texto_busqueda.replace("á", "a")
            .replace("é", "e")
            .replace("í", "i")
            .replace("ó", "o")
            .replace("ú", "u")
        )

        try:
            with DB() as conexion:
                cursor = conexion.cursor()
                # Usar LOWER y REPLACE en la consulta para normalizar los datos de la base de datos
                # la idea es que la consulta ignore las tildes y mayúsculas/minúsculas
                query = """
                    SELECT ID, Alumno, Correo, ultimoAcceso 
                    FROM alumnos 
                    WHERE LOWER(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(Alumno, 'á', 'a'), 'é', 'e'), 'í', 'i'), 'ó', 'o'), 'ú', 'u')) 
                    LIKE ?
                """
                cursor.execute(query, (f"%{texto_busqueda}%",))
                resultados = cursor.fetchall()
            logging.info(
                f"Resultados de búsqueda para '{texto_busqueda}': {resultados}"
            )

            if resultados:
                mensaje = "Resultados encontrados:\n\n"
                for resultado in resultados:
                    alumno_id, nombre_alumno, correo_alumno, ultimo_acceso = resultado
                    mensaje += (
                        f"🆔 ID: {alumno_id}\n"
                        f"👤 Nombre: {nombre_alumno}\n"
                        f"📧 Correo: {correo_alumno}\n"
                        f"⏰ Último Acceso: {ultimo_acceso}\n\n"
                    )

                QMessageBox.information(self, "Resultados", mensaje)
            else:
                QMessageBox.information(
                    self,
                    "Sin resultados",
                    "No se encontró ningún alumno con ese nombre.",
                )

        except Exception as e:
            QMessageBox.critical(self, "Error", f"Error al buscar el alumno:\n{str(e)}")
