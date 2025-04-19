import sqlite3
import sys
import logging
from typing import Optional

from PySide6.QtWidgets import (
    QApplication,
    QDialog,
    QMainWindow,
    QMessageBox,
    QWidget,
    QVBoxLayout,
    QPushButton,
    QLabel,
)
from Control.connection import DB
from Control.login import LoginDialog
from Vista.ui_tabla import Ui_Form

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)


class Tarea(QWidget, Ui_Form):
    """Clase principal de la aplicación."""

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        """ Estos type hints son para ayudar a los desarrolladores a entender el tipo de datos que se espera en cada variable. """
        self.user: Optional[str] = None
        self.password: Optional[str] = None

        self.db = DB()
        self.conectar_sqlite()

    def conectar_sqlite(self):
        """Establece una conexión directa con la base de datos SQLite."""
        try:
            if not self.db.is_connected():
                logging.info("Intentando conectar a SQLite...")
                self.db.conectar(self.user, self.password)
                logging.info("Conexión establecida.")
        except sqlite3.Error as e:
            logging.error(f"Error al conectar con SQLite: {str(e)}")
            self.mostrar_login()

    def mostrar_login(self):
        """Muestra la interfaz de login para obtener credenciales."""
        max_retries = 3
        for attempt in range(max_retries):
            logging.info("Mostrando LoginDialog...")
            login_dialog = LoginDialog()
            if login_dialog.exec():  # Si el usuario presiona "Aceptar"
                self.user, self.password = login_dialog.get_credentials()
                try:
                    self.db.conectar(self.user, self.password)
                    logging.info("Conexión exitosa.")
                    return  # Salir del método si la conexión es exitosa
                except sqlite3.Error as e:
                    logging.error(f"Error al conectar con SQLite: {str(e)}")
                    logging.info("Reintente ingresar las credenciales.")
            else:
                logging.warning("LoginDialog cancelado por el usuario.")
                break
        QMessageBox.critical(
            self,
            "Error de conexión",
            "No se pudo establecer conexión después de varios intentos.",
        )
        logging.critical("No se pudo establecer conexión. Cerrando aplicación.")
        self.close_application()

    def close_application(self):
        """Cierra la aplicación de forma segura."""
        logging.info("Cerrando aplicación...")
        self.db.conexion.close() if self.db.conexion else None
        logging.info("Conexión cerrada.")
        QApplication.quit()
        sys.exit(0)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mi_app = Tarea()
    mi_app.show()
    sys.exit(app.exec())
