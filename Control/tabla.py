from PySide6 import QtWidgets
from Vista.ui_tabla import Ui_Form
import csv
from PySide6.QtWidgets import QFileDialog, QMessageBox, QWidget


class Tabla(QWidget, Ui_Form):
    """Clase para la interfaz de la tabla."""

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.pushButton_Importar.clicked.connect(self.importar_datos)

    def importar_datos(self):
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

        try:
            # Abrir el archivo CSV y leer los datos
            with open(ruta_archivo, newline="", encoding="utf-8") as archivo_csv:
                lector_csv = csv.reader(archivo_csv)
                encabezados = next(lector_csv)  # Leer la primera fila como encabezados

                # Configurar la tabla con los encabezados
                self.tableWidget.setColumnCount(len(encabezados))
                self.tableWidget.setHorizontalHeaderLabels(encabezados)

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

                # Ajustar el tamaño de las columnas y filas al contenido
                self.tableWidget.resizeColumnsToContents()
                self.tableWidget.resizeRowsToContents()

                self.adjustSize()  # Ajustar el tamaño de la ventana a los contenidos
                ancho_total = sum(
                    self.tableWidget.columnWidth(i)
                    for i in range(self.tableWidget.columnCount())
                )
                # Agregar un margen extra para evitar que los contenidos se corten y poder verlos
                # correctamente sin scroll
                self.tableWidget.setMinimumWidth(ancho_total + 30)

        except Exception as e:
            # Mostrar un mensaje de error si ocurre algún problema
            QMessageBox.critical(
                self, "Error", f"No se pudo importar el archivo CSV:\n{str(e)}"
            )
