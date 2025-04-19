# Vista/login_dialog.py

from PySide6.QtWidgets import QDialog, QMessageBox
from Vista.ui_login import Ui_LoginDialog


class LoginDialog(QDialog, Ui_LoginDialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.login_button.clicked.connect(self.acceptar_login)

    def acceptar_login(self):
        if self.lineUser.text() and self.linePass.text():
            self.accept()
        else:
            QMessageBox.warning(
                self, "Error", "Por favor, ingrese un nombre de usuario y una contraseña."
            )

    def get_credentials(self):
        return self.lineUser.text(), self.linePass.text()
