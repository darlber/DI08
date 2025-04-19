import logging
import sqlite3

from PySide6.QtWidgets import QMessageBox


class DB:
    _instance = None

    # TODO login desde base de datos y no hardcodeado
    def __init__(self):
        self.conexion = None
        self.valid_user = "root"
        self.valid_password = "root"

    # Singleton pattern to ensure only one instance of DB exists
    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance

    def conectar(self, user, password):
        """Establece una conexión directa con la base de datos SQLite."""
        if not (user == self.valid_user and password == self.valid_password):
            logging.error("Usuario o contraseña incorrectos.")
            QMessageBox.critical(None, "Error", "Usuario o contraseña incorrectos.")
            raise sqlite3.Error(
                "Usuario o contraseña incorrectos."
            )  # Lanza una excepción

        if self.conexion is None:  # Solo intenta conectar si no hay una conexión activa
            try:
                self.conexion = sqlite3.connect(
                    "C:/Users/darlb/Desktop/DI08/Modelo/acceso.db"
                )
                logging.info("Conexión a SQLite establecida.")
            except sqlite3.Error as e:
                raise sqlite3.Error(f"Error al conectar con SQLite: {str(e)}")
        return self.conexion


    def is_connected(self):
        """Verifica si hay una conexión activa."""
        return self.conexion is not None

    def close_connection(self):
        """Cierra la conexión a la base de datos."""
        if self.conexion:
            self.conexion.close()
            self.conexion = None
            
    def ejecutar_consulta(self, query):
        """Ejecuta una consulta SQL y devuelve los resultados."""
        if not self.is_connected():
            raise sqlite3.Error("No hay una conexión activa a la base de datos.")
        try:
            #with es un contexto que asegura que la conexión se cierre correctamente
            # y que los cambios se guarden o se deshagan en caso de error.
            with self.conexion: 
                cursor = self.conexion.cursor()
                cursor.execute(query)
                return cursor.fetchall()
        except sqlite3.Error as e:
            raise sqlite3.Error(f"Error al ejecutar consulta: {str(e)}")
