# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'tablaJXhOlE.ui'
##
## Created by: Qt User Interface Compiler version 6.8.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QAbstractScrollArea, QApplication, QFrame,
    QHBoxLayout, QHeaderView, QLineEdit, QPushButton,
    QSizePolicy, QTableWidget, QTableWidgetItem, QVBoxLayout,
    QWidget)
from Vista import icon 

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.setWindowModality(Qt.WindowModality.WindowModal)
        Form.resize(540, 244)
        font = QFont()
        font.setPointSize(12)
        Form.setFont(font)
        icon = QIcon()
        icon.addFile(u":/icon/icon.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        Form.setWindowIcon(icon)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.tableWidget = QTableWidget(Form)
        if (self.tableWidget.columnCount() < 4):
            self.tableWidget.setColumnCount(4)
        font1 = QFont()
        font1.setBold(True)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setFont(font1);
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setFont(font1);
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setFont(font1);
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        __qtablewidgetitem3.setFont(font1);
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        if (self.tableWidget.rowCount() < 3):
            self.tableWidget.setRowCount(3)
        self.tableWidget.setObjectName(u"tableWidget")
        font2 = QFont()
        font2.setPointSize(12)
        font2.setBold(False)
        self.tableWidget.setFont(font2)
        self.tableWidget.setFrameShape(QFrame.Shape.StyledPanel)
        self.tableWidget.setFrameShadow(QFrame.Shadow.Sunken)
        self.tableWidget.setMidLineWidth(0)
        self.tableWidget.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.tableWidget.setSizeAdjustPolicy(QAbstractScrollArea.SizeAdjustPolicy.AdjustToContents)
        self.tableWidget.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.tableWidget.setAlternatingRowColors(True)
        self.tableWidget.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)
        self.tableWidget.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.tableWidget.setTextElideMode(Qt.TextElideMode.ElideMiddle)
        self.tableWidget.setVerticalScrollMode(QAbstractItemView.ScrollMode.ScrollPerPixel)
        self.tableWidget.setGridStyle(Qt.PenStyle.SolidLine)
        self.tableWidget.setSortingEnabled(True)
        self.tableWidget.setRowCount(3)
        self.tableWidget.setColumnCount(4)

        self.verticalLayout.addWidget(self.tableWidget)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pushButton_Actualizar = QPushButton(Form)
        self.pushButton_Actualizar.setObjectName(u"pushButton_Actualizar")

        self.horizontalLayout.addWidget(self.pushButton_Actualizar)

        self.pushButton_Importar = QPushButton(Form)
        self.pushButton_Importar.setObjectName(u"pushButton_Importar")

        self.horizontalLayout.addWidget(self.pushButton_Importar)

        self.pushButton_Transform = QPushButton(Form)
        self.pushButton_Transform.setObjectName(u"pushButton_Transform")

        self.horizontalLayout.addWidget(self.pushButton_Transform)

        self.pushButton_Eliminar = QPushButton(Form)
        self.pushButton_Eliminar.setObjectName(u"pushButton_Eliminar")

        self.horizontalLayout.addWidget(self.pushButton_Eliminar)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.lineEdit_Buscar = QLineEdit(Form)
        self.lineEdit_Buscar.setObjectName(u"lineEdit_Buscar")

        self.horizontalLayout_2.addWidget(self.lineEdit_Buscar)

        self.pushButton_Buscar = QPushButton(Form)
        self.pushButton_Buscar.setObjectName(u"pushButton_Buscar")
        self.pushButton_Buscar.setMinimumSize(QSize(75, 29))
        self.pushButton_Buscar.setMaximumSize(QSize(75, 29))

        self.horizontalLayout_2.addWidget(self.pushButton_Buscar)


        self.verticalLayout.addLayout(self.horizontalLayout_2)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Tabla de Alumnos", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Form", u"ID", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Form", u"Alumno", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Form", u"Correo", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Form", u"UltimoAcceso", None));
#if QT_CONFIG(tooltip)
        self.pushButton_Actualizar.setToolTip(QCoreApplication.translate("Form", u"Lee datos de la database, y actualiza el contenido en esta tabla en funci\u00f3n de esos datos.", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_Actualizar.setText(QCoreApplication.translate("Form", u"Refrescar p\u00e1gina", None))
#if QT_CONFIG(tooltip)
        self.pushButton_Importar.setToolTip(QCoreApplication.translate("Form", u"Muestra en la tabla los datos extra\u00eddos de un .csv. No opera con ellos.", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_Importar.setText(QCoreApplication.translate("Form", u"Leer CSV", None))
#if QT_CONFIG(tooltip)
        self.pushButton_Transform.setToolTip(QCoreApplication.translate("Form", u"Introduce los datos del .csv en la base de datos.", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_Transform.setText(QCoreApplication.translate("Form", u"CSV -> Base de datos", None))
#if QT_CONFIG(tooltip)
        self.pushButton_Eliminar.setToolTip(QCoreApplication.translate("Form", u"Elimina los datos de la base de datos y de la tabla.", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_Eliminar.setText(QCoreApplication.translate("Form", u"Eliminar contenido", None))
#if QT_CONFIG(tooltip)
        self.pushButton_Buscar.setToolTip(QCoreApplication.translate("Form", u"Buscar alumno por id.", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_Buscar.setText(QCoreApplication.translate("Form", u"Buscar", None))
    # retranslateUi

