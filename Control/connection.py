import logging
import os
import sqlite3

from PySide6.QtWidgets import QMessageBox


class DB:
    _instance = None

    # Singleton pattern to ensure only one instance of DB exists
    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self):
        self.conexion = None


    def conectarConSQLite(self):
        """Establece una conexión directa con la base de datos SQLite."""
        # Si ya hay una conexión activa, reutilizarla
        if self.is_connected():
            logging.info("Reutilizando conexión activa a SQLite.")
            return self.conexion
        try:
            base_dir = os.path.dirname(os.path.abspath(__file__))
            db_path = os.path.join(base_dir, "../Modelo/acceso.db")
            self.conexion = sqlite3.connect(db_path)
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

    def ejecutar_consulta(self, query, params=None):
        """Ejecuta una consulta SQL y devuelve los resultados."""
        if not self.is_connected():
            raise sqlite3.Error("No hay una conexión activa a la base de datos.")
        try:
            # with es un contexto que asegura que la conexión se cierre correctamente
            # y que los cambios se guarden o se deshagan en caso de error. hace commit
            # y rollback automáticamente
            with self.conexion:
                cursor = self.conexion.cursor()
                if params:
                    cursor.execute(query, params)  # Usar parámetros si se proporcionan
                else:
                    cursor.execute(query)
                if query.strip().upper().startswith("SELECT"):
                    return cursor.fetchall()
        except sqlite3.Error as e:
            raise sqlite3.Error(f"Error al ejecutar consulta: {str(e)}")


    def __enter__(self):
        self.conectarConSQLite()
        return self.conexion

    def __exit__(self, exc_type, exc_value, traceback):
        if self.conexion:
            if exc_type is None:
                self.conexion.commit()
            else:
                self.conexion.rollback()
            self.close_connection()
