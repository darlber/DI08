import sys
import logging
from typing import Optional
from PySide6.QtWidgets import QApplication
from Control.connection import DB

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)


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
        # Parte 2. Si la conexión es fallida, mostrará una interfaz para loguearnos correctamente
        # Simulamos un login erróneo para mostrar la interfaz de login
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
        from Control.tabla import Tabla

        self.tabla = Tabla()
        self.tabla.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mi_app = Tarea()
    sys.exit(app.exec())
