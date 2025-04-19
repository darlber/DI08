# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'loginycjSGg.ui'
##
## Created by: Qt User Interface Compiler version 6.8.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (
    QCoreApplication,
    QDate,
    QDateTime,
    QLocale,
    QMetaObject,
    QObject,
    QPoint,
    QRect,
    QSize,
    QTime,
    QUrl,
    Qt,
)
from PySide6.QtGui import (
    QBrush,
    QColor,
    QConicalGradient,
    QCursor,
    QFont,
    QFontDatabase,
    QGradient,
    QIcon,
    QImage,
    QKeySequence,
    QLinearGradient,
    QPainter,
    QPalette,
    QPixmap,
    QRadialGradient,
    QTransform,
)
from PySide6.QtWidgets import (
    QApplication,
    QDialog,
    QLineEdit,
    QPushButton,
    QSizePolicy,
    QSpacerItem,
    QVBoxLayout,
    QWidget,
)


class Ui_LoginDialog(object):
    def setupUi(self, LoginDialog):
        if not LoginDialog.objectName():
            LoginDialog.setObjectName("LoginDialog")
        LoginDialog.setWindowModality(Qt.WindowModality.WindowModal)
        LoginDialog.resize(213, 168)
        LoginDialog.setMinimumSize(QSize(213, 168))
        LoginDialog.setMaximumSize(QSize(213, 168))
        self.verticalLayout_2 = QVBoxLayout(LoginDialog)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.lineUser = QLineEdit(LoginDialog)
        self.lineUser.setObjectName("user_line")
        self.lineUser.setMinimumSize(QSize(0, 31))
        self.lineUser.setMaximumSize(QSize(201, 31))
        font = QFont()
        font.setPointSize(11)
        self.lineUser.setFont(font)

        self.verticalLayout_2.addWidget(self.lineUser)

        self.linePass = QLineEdit(LoginDialog)
        self.linePass.setObjectName("pass_line")
        self.linePass.setMinimumSize(QSize(0, 31))
        self.linePass.setMaximumSize(QSize(201, 31))
        self.linePass.setFont(font)
        self.linePass.setEchoMode(QLineEdit.EchoMode.Password)

        self.verticalLayout_2.addWidget(self.linePass)

        self.verticalSpacer = QSpacerItem(
            20, 24, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding
        )

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.login_button = QPushButton(LoginDialog)
        self.login_button.setObjectName("login_button")
        self.login_button.setMinimumSize(QSize(121, 41))
        self.login_button.setMaximumSize(QSize(121, 41))
        self.login_button.setFont(font)

        self.verticalLayout_2.addWidget(
            self.login_button, 0, Qt.AlignmentFlag.AlignHCenter
        )

        self.retranslateUi(LoginDialog)

        QMetaObject.connectSlotsByName(LoginDialog)

    # setupUi

    def retranslateUi(self, LoginDialog):
        LoginDialog.setWindowTitle(
            QCoreApplication.translate("LoginDialog", "Dialog", None)
        )
        self.lineUser.setPlaceholderText(
            QCoreApplication.translate("LoginDialog", "Usuario", None)
        )
        self.linePass.setPlaceholderText(
            QCoreApplication.translate("LoginDialog", "Contrase\u00f1a", None)
        )
        self.login_button.setText(
            QCoreApplication.translate("LoginDialog", "Login", None)
        )

    # retranslateUi
