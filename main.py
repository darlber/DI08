import sys
import logging
from typing import Optional
from PySide6.QtWidgets import QApplication
from Control.connection import DB

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)

# Consideraciones previas: modificamos el archivo acceso.db de manera que:
# 1. Id sea Primary Key;
# 2. No existan dos campos con el mismo id (Marcos Antonio Vaquero Díaz2 tenia id 10 en vez de 11);
# hubiese podido solventarse con un id autoincremental
# 3. si importamos el mismo archivo .csv, no se repitan los datos


class Tarea:
    """Clase principal de la aplicación."""

    def __init__(self):
        super().__init__()

        """ Estos type hints son para ayudar a
        entender el tipo de datos que se espera en cada variable. """
        self.user: Optional[str] = "root"
        self.password: Optional[str] = "root"

        self.db = DB()
        self.conectar_sqlite()

    def conectar_sqlite(self):
        """Establece la conexión, o solicita login si falla."""
        logging.info("Intentando conectar a la base de datos...")
        # Parte 2. Si la conexión es fallida, mostrará una interfaz
        # para loguearnos correctamente
        # Simulamos un login erróneo para mostrar la interfaz de login
        # y cumplir con el requerimiento de la tarea
        if self.db.is_connected() or self.db.intentar_conectar_con_login(
            self.user, self.password
        ):
            logging.info("Conexión exitosa. Mostrando la tabla...")
            self.mostrar_tabla()
        else:
            logging.critical("No se pudo conectar. Cerrando aplicación.")
            self.close_application()

    def close_application(self):
        """Cierra la aplicación de forma segura."""
        logging.info("Cerrando aplicación...")
        self.db.close_connection()
        QApplication.quit()
        sys.exit(0)

    def mostrar_tabla(self):
        """Muestra la tabla de la base de datos."""

        from Control.tabla import Tabla

        self.tabla = Tabla()
        self.tabla.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mi_app = Tarea()
    sys.exit(app.exec())
