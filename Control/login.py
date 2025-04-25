# Vista/login_dialog.py

import logging
from PySide6.QtWidgets import QDialog, QMessageBox
from Vista.ui_login import Ui_LoginDialog
from Control.connection import DB


class LoginDialog(QDialog, Ui_LoginDialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.valid_user = "root"
        self.valid_password = "root"
        self.db = DB()

        self.login_button.clicked.connect(self.acceptar_login)

    def acceptar_login(self):

        if self.lineUser.text() and self.linePass.text():
            self.accept()
        else:
            QMessageBox.warning(
                self,
                "Error",
                "Por favor, ingrese un nombre de usuario y una contraseña.",
            )

    def get_credentials(self):
        return self.lineUser.text(), self.linePass.text()

    def validar_user_pass(self, user, password):
        return user == self.valid_user and password == self.valid_password

    def validar_credenciales(self, user, password):
        """Muestra el diálogo de login hasta 3 intentos o éxito."""
        max_retries = 3
        attempt = 0
        if self.validar_user_pass(user, password):
            self.db.conectarConSQLite()
            logging.info("Conexión establecida con credenciales válidas.")
            return True
        else:
            QMessageBox.warning(
                self,"Error", "Credenciales incorrectas. Intente nuevamente."
            )

        while attempt < max_retries:
            if self.exec():
                user, password = self.get_credentials()
                if user == self.valid_user and password == self.valid_password:
                    self.db.conectarConSQLite()
                    logging.info("Conexión establecida con credenciales válidas.")
                    QMessageBox.information(self, "Conexión", "Conexión establecida.")
                    return True
                else:
                    attempt += 1
                    self.linePass.clear()
                    QMessageBox.warning(
                        self,
                        "Error de conexión",
                        f"Intento {attempt} fallido. Credenciales incorrectas.",
                    )
                    logging.warning(
                        f"Intento {attempt} fallido: credenciales incorrectas."
                    )
            else:
                logging.info("Login cancelado por el usuario.")
                break

        QMessageBox.critical(
            self,
            "Error de conexión",
            "No se pudo establecer conexión después de varios intentos.",
        )
        return False
