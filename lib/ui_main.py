# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'maingcbrQq.ui'
##
## Created by: Qt User Interface Compiler version 6.1.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.main_layout = QVBoxLayout()
        self.main_layout.setSpacing(0)
        self.main_layout.setObjectName(u"main_layout")
        self.main_layout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.main_layout.setContentsMargins(0, 0, 0, 0)
        self.content_layout = QVBoxLayout()
        self.content_layout.setObjectName(u"content_layout")
        self.content_layout.setContentsMargins(1, 0, 1, 1)
        self.scrollArea = QScrollArea(self.centralwidget)
        self.scrollArea.setObjectName(u"scrollArea")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy)
        self.scrollArea.viewport().setProperty("cursor", QCursor(Qt.ArrowCursor))
        self.scrollArea.setMouseTracking(True)
        self.scrollArea.setAutoFillBackground(False)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 792, 2086))
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(1)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.scrollAreaWidgetContents.sizePolicy().hasHeightForWidth())
        self.scrollAreaWidgetContents.setSizePolicy(sizePolicy1)
        self.scrollAreaWidgetContents.setMaximumSize(QSize(16777215, 16777215))
        self.scrollAreaWidgetContents.setMouseTracking(True)
        self.scrollAreaWidgetContents.setAutoFillBackground(True)
        self.verticalLayout_8 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(-1, -1, 200, -1)
        self.label_8 = QLabel(self.scrollAreaWidgetContents)
        self.label_8.setObjectName(u"label_8")

        self.verticalLayout_8.addWidget(self.label_8)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_2 = QLabel(self.scrollAreaWidgetContents)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout.addWidget(self.label_2)

        self.label_3 = QLabel(self.scrollAreaWidgetContents)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout.addWidget(self.label_3)

        self.label_4 = QLabel(self.scrollAreaWidgetContents)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout.addWidget(self.label_4)

        self.label_5 = QLabel(self.scrollAreaWidgetContents)
        self.label_5.setObjectName(u"label_5")

        self.verticalLayout.addWidget(self.label_5)

        self.label_6 = QLabel(self.scrollAreaWidgetContents)
        self.label_6.setObjectName(u"label_6")

        self.verticalLayout.addWidget(self.label_6)

        self.label_7 = QLabel(self.scrollAreaWidgetContents)
        self.label_7.setObjectName(u"label_7")

        self.verticalLayout.addWidget(self.label_7)


        self.verticalLayout_8.addLayout(self.verticalLayout)

        self.horizontalSpacer = QSpacerItem(773, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.verticalLayout_8.addItem(self.horizontalSpacer)

        self.label_10 = QLabel(self.scrollAreaWidgetContents)
        self.label_10.setObjectName(u"label_10")

        self.verticalLayout_8.addWidget(self.label_10)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.pushButton_3 = QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setEnabled(False)
        self.pushButton_3.setCheckable(False)
        self.pushButton_3.setChecked(False)

        self.gridLayout.addWidget(self.pushButton_3, 0, 1, 1, 1)

        self.pushButton_10 = QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_10.setObjectName(u"pushButton_10")
        self.pushButton_10.setCheckable(True)
        self.pushButton_10.setChecked(True)

        self.gridLayout.addWidget(self.pushButton_10, 3, 1, 1, 1)

        self.pushButton = QPushButton(self.scrollAreaWidgetContents)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setCheckable(False)

        self.gridLayout.addWidget(self.pushButton, 0, 0, 1, 1)

        self.pushButton_2 = QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setCheckable(True)
        self.pushButton_2.setChecked(False)

        self.gridLayout.addWidget(self.pushButton_2, 0, 2, 1, 1)

        self.pushButton_12 = QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_12.setObjectName(u"pushButton_12")
        self.pushButton_12.setCheckable(True)
        self.pushButton_12.setChecked(True)

        self.gridLayout.addWidget(self.pushButton_12, 4, 1, 1, 1)

        self.pushButton_5 = QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setCheckable(False)

        self.gridLayout.addWidget(self.pushButton_5, 1, 0, 1, 1)

        self.pushButton_6 = QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setCheckable(True)
        self.pushButton_6.setChecked(True)

        self.gridLayout.addWidget(self.pushButton_6, 1, 1, 1, 1)

        self.pushButton_8 = QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_8.setObjectName(u"pushButton_8")
        self.pushButton_8.setCheckable(True)
        self.pushButton_8.setChecked(True)

        self.gridLayout.addWidget(self.pushButton_8, 2, 1, 1, 1)

        self.pushButton_9 = QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_9.setObjectName(u"pushButton_9")
        self.pushButton_9.setCheckable(False)

        self.gridLayout.addWidget(self.pushButton_9, 3, 0, 1, 1)

        self.pushButton_7 = QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setCheckable(False)

        self.gridLayout.addWidget(self.pushButton_7, 2, 0, 1, 1)

        self.pushButton_11 = QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_11.setObjectName(u"pushButton_11")
        self.pushButton_11.setCheckable(False)

        self.gridLayout.addWidget(self.pushButton_11, 4, 0, 1, 1)

        self.pushButton_4 = QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_4.setObjectName(u"pushButton_4")

        self.gridLayout.addWidget(self.pushButton_4, 5, 0, 1, 1)

        self.pushButton_13 = QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_13.setObjectName(u"pushButton_13")

        self.gridLayout.addWidget(self.pushButton_13, 5, 1, 1, 1)

        self.pushButton_14 = QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_14.setObjectName(u"pushButton_14")

        self.gridLayout.addWidget(self.pushButton_14, 5, 2, 1, 1)


        self.verticalLayout_8.addLayout(self.gridLayout)

        self.horizontalSpacer_8 = QSpacerItem(773, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.verticalLayout_8.addItem(self.horizontalSpacer_8)

        self.label_12 = QLabel(self.scrollAreaWidgetContents)
        self.label_12.setObjectName(u"label_12")

        self.verticalLayout_8.addWidget(self.label_12)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.scrollAreaWidgetContents)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.lineEdit = QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit.setObjectName(u"lineEdit")

        self.horizontalLayout.addWidget(self.lineEdit)

        self.horizontalLayout.setStretch(1, 1)

        self.verticalLayout_8.addLayout(self.horizontalLayout)

        self.horizontalSpacer_2 = QSpacerItem(773, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.verticalLayout_8.addItem(self.horizontalSpacer_2)

        self.label_9 = QLabel(self.scrollAreaWidgetContents)
        self.label_9.setObjectName(u"label_9")

        self.verticalLayout_8.addWidget(self.label_9)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_13 = QLabel(self.scrollAreaWidgetContents)
        self.label_13.setObjectName(u"label_13")

        self.horizontalLayout_3.addWidget(self.label_13)

        self.textEdit = QTextEdit(self.scrollAreaWidgetContents)
        self.textEdit.setObjectName(u"textEdit")

        self.horizontalLayout_3.addWidget(self.textEdit)


        self.verticalLayout_8.addLayout(self.horizontalLayout_3)

        self.horizontalSpacer_3 = QSpacerItem(773, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.verticalLayout_8.addItem(self.horizontalSpacer_3)

        self.label_15 = QLabel(self.scrollAreaWidgetContents)
        self.label_15.setObjectName(u"label_15")

        self.verticalLayout_8.addWidget(self.label_15)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_16 = QLabel(self.scrollAreaWidgetContents)
        self.label_16.setObjectName(u"label_16")

        self.horizontalLayout_4.addWidget(self.label_16)

        self.spinBox = QSpinBox(self.scrollAreaWidgetContents)
        self.spinBox.setObjectName(u"spinBox")

        self.horizontalLayout_4.addWidget(self.spinBox)

        self.horizontalLayout_4.setStretch(1, 1)

        self.verticalLayout_8.addLayout(self.horizontalLayout_4)

        self.horizontalSpacer_4 = QSpacerItem(773, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.verticalLayout_8.addItem(self.horizontalSpacer_4)

        self.label_17 = QLabel(self.scrollAreaWidgetContents)
        self.label_17.setObjectName(u"label_17")

        self.verticalLayout_8.addWidget(self.label_17)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_18 = QLabel(self.scrollAreaWidgetContents)
        self.label_18.setObjectName(u"label_18")

        self.horizontalLayout_5.addWidget(self.label_18)

        self.doubleSpinBox = QDoubleSpinBox(self.scrollAreaWidgetContents)
        self.doubleSpinBox.setObjectName(u"doubleSpinBox")

        self.horizontalLayout_5.addWidget(self.doubleSpinBox)

        self.horizontalLayout_5.setStretch(1, 1)

        self.verticalLayout_8.addLayout(self.horizontalLayout_5)

        self.horizontalSpacer_5 = QSpacerItem(773, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.verticalLayout_8.addItem(self.horizontalSpacer_5)

        self.label_19 = QLabel(self.scrollAreaWidgetContents)
        self.label_19.setObjectName(u"label_19")

        self.verticalLayout_8.addWidget(self.label_19)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_20 = QLabel(self.scrollAreaWidgetContents)
        self.label_20.setObjectName(u"label_20")

        self.horizontalLayout_6.addWidget(self.label_20)

        self.dateTimeEdit = QDateTimeEdit(self.scrollAreaWidgetContents)
        self.dateTimeEdit.setObjectName(u"dateTimeEdit")
        self.dateTimeEdit.setCalendarPopup(False)

        self.horizontalLayout_6.addWidget(self.dateTimeEdit)

        self.horizontalLayout_6.setStretch(1, 1)

        self.verticalLayout_8.addLayout(self.horizontalLayout_6)

        self.horizontalSpacer_6 = QSpacerItem(773, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.verticalLayout_8.addItem(self.horizontalSpacer_6)

        self.label_24 = QLabel(self.scrollAreaWidgetContents)
        self.label_24.setObjectName(u"label_24")

        self.verticalLayout_8.addWidget(self.label_24)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_25 = QLabel(self.scrollAreaWidgetContents)
        self.label_25.setObjectName(u"label_25")

        self.horizontalLayout_7.addWidget(self.label_25)

        self.comboBox = QComboBox(self.scrollAreaWidgetContents)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")

        self.horizontalLayout_7.addWidget(self.comboBox)

        self.horizontalLayout_7.setStretch(1, 1)

        self.verticalLayout_8.addLayout(self.horizontalLayout_7)

        self.horizontalSpacer_7 = QSpacerItem(773, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.verticalLayout_8.addItem(self.horizontalSpacer_7)

        self.label_27 = QLabel(self.scrollAreaWidgetContents)
        self.label_27.setObjectName(u"label_27")

        self.verticalLayout_8.addWidget(self.label_27)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_28 = QLabel(self.scrollAreaWidgetContents)
        self.label_28.setObjectName(u"label_28")

        self.horizontalLayout_2.addWidget(self.label_28)

        self.widget_2 = QWidget(self.scrollAreaWidgetContents)
        self.widget_2.setObjectName(u"widget_2")
        self.verticalLayout_3 = QVBoxLayout(self.widget_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setSpacing(20)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.radioButton_5 = QRadioButton(self.widget_2)
        self.buttonGroup = QButtonGroup(MainWindow)
        self.buttonGroup.setObjectName(u"buttonGroup")
        self.buttonGroup.addButton(self.radioButton_5)
        self.radioButton_5.setObjectName(u"radioButton_5")
        self.radioButton_5.setChecked(True)

        self.horizontalLayout_9.addWidget(self.radioButton_5)

        self.radioButton_6 = QRadioButton(self.widget_2)
        self.buttonGroup.addButton(self.radioButton_6)
        self.radioButton_6.setObjectName(u"radioButton_6")

        self.horizontalLayout_9.addWidget(self.radioButton_6)

        self.horizontalLayout_9.setStretch(1, 1)

        self.verticalLayout_3.addLayout(self.horizontalLayout_9)


        self.horizontalLayout_2.addWidget(self.widget_2)


        self.verticalLayout_8.addLayout(self.horizontalLayout_2)

        self.horizontalSpacer_9 = QSpacerItem(773, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.verticalLayout_8.addItem(self.horizontalSpacer_9)

        self.label_30 = QLabel(self.scrollAreaWidgetContents)
        self.label_30.setObjectName(u"label_30")

        self.verticalLayout_8.addWidget(self.label_30)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_31 = QLabel(self.scrollAreaWidgetContents)
        self.label_31.setObjectName(u"label_31")

        self.horizontalLayout_10.addWidget(self.label_31)

        self.widget_4 = QWidget(self.scrollAreaWidgetContents)
        self.widget_4.setObjectName(u"widget_4")
        self.verticalLayout_6 = QVBoxLayout(self.widget_4)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.checkBox = QCheckBox(self.widget_4)
        self.buttonGroup_3 = QButtonGroup(MainWindow)
        self.buttonGroup_3.setObjectName(u"buttonGroup_3")
        self.buttonGroup_3.setExclusive(False)
        self.buttonGroup_3.addButton(self.checkBox)
        self.checkBox.setObjectName(u"checkBox")

        self.horizontalLayout_8.addWidget(self.checkBox)

        self.checkBox_2 = QCheckBox(self.widget_4)
        self.buttonGroup_3.addButton(self.checkBox_2)
        self.checkBox_2.setObjectName(u"checkBox_2")

        self.horizontalLayout_8.addWidget(self.checkBox_2)

        self.checkBox_3 = QCheckBox(self.widget_4)
        self.buttonGroup_3.addButton(self.checkBox_3)
        self.checkBox_3.setObjectName(u"checkBox_3")

        self.horizontalLayout_8.addWidget(self.checkBox_3)

        self.horizontalLayout_8.setStretch(2, 1)

        self.verticalLayout_6.addLayout(self.horizontalLayout_8)


        self.horizontalLayout_10.addWidget(self.widget_4)


        self.verticalLayout_8.addLayout(self.horizontalLayout_10)

        self.horizontalSpacer_10 = QSpacerItem(773, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.verticalLayout_8.addItem(self.horizontalSpacer_10)

        self.label_11 = QLabel(self.scrollAreaWidgetContents)
        self.label_11.setObjectName(u"label_11")

        self.verticalLayout_8.addWidget(self.label_11)

        self.widget = QWidget(self.scrollAreaWidgetContents)
        self.widget.setObjectName(u"widget")
        self.verticalLayout_4 = QVBoxLayout(self.widget)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, -1, 0, 0)
        self.formLayout_2 = QFormLayout()
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.formLayout_2.setVerticalSpacing(12)
        self.Label = QLabel(self.widget)
        self.Label.setObjectName(u"Label")

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.Label)

        self.LineEdit = QLineEdit(self.widget)
        self.LineEdit.setObjectName(u"LineEdit")

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.LineEdit)

        self.Label_2 = QLabel(self.widget)
        self.Label_2.setObjectName(u"Label_2")

        self.formLayout_2.setWidget(1, QFormLayout.LabelRole, self.Label_2)

        self.LineEdit_2 = QLineEdit(self.widget)
        self.LineEdit_2.setObjectName(u"LineEdit_2")

        self.formLayout_2.setWidget(1, QFormLayout.FieldRole, self.LineEdit_2)

        self.label_14 = QLabel(self.widget)
        self.label_14.setObjectName(u"label_14")

        self.formLayout_2.setWidget(2, QFormLayout.LabelRole, self.label_14)

        self.textEdit_2 = QTextEdit(self.widget)
        self.textEdit_2.setObjectName(u"textEdit_2")

        self.formLayout_2.setWidget(2, QFormLayout.FieldRole, self.textEdit_2)

        self.label_21 = QLabel(self.widget)
        self.label_21.setObjectName(u"label_21")

        self.formLayout_2.setWidget(3, QFormLayout.LabelRole, self.label_21)

        self.spinBox_2 = QSpinBox(self.widget)
        self.spinBox_2.setObjectName(u"spinBox_2")

        self.formLayout_2.setWidget(3, QFormLayout.FieldRole, self.spinBox_2)

        self.label_22 = QLabel(self.widget)
        self.label_22.setObjectName(u"label_22")

        self.formLayout_2.setWidget(4, QFormLayout.LabelRole, self.label_22)

        self.doubleSpinBox_2 = QDoubleSpinBox(self.widget)
        self.doubleSpinBox_2.setObjectName(u"doubleSpinBox_2")

        self.formLayout_2.setWidget(4, QFormLayout.FieldRole, self.doubleSpinBox_2)

        self.label_23 = QLabel(self.widget)
        self.label_23.setObjectName(u"label_23")

        self.formLayout_2.setWidget(5, QFormLayout.LabelRole, self.label_23)

        self.dateTimeEdit_2 = QDateTimeEdit(self.widget)
        self.dateTimeEdit_2.setObjectName(u"dateTimeEdit_2")
        self.dateTimeEdit_2.setCalendarPopup(True)

        self.formLayout_2.setWidget(5, QFormLayout.FieldRole, self.dateTimeEdit_2)

        self.label_26 = QLabel(self.widget)
        self.label_26.setObjectName(u"label_26")

        self.formLayout_2.setWidget(6, QFormLayout.LabelRole, self.label_26)

        self.comboBox_2 = QComboBox(self.widget)
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.setObjectName(u"comboBox_2")

        self.formLayout_2.setWidget(6, QFormLayout.FieldRole, self.comboBox_2)

        self.label_29 = QLabel(self.widget)
        self.label_29.setObjectName(u"label_29")

        self.formLayout_2.setWidget(7, QFormLayout.LabelRole, self.label_29)

        self.widget_3 = QWidget(self.widget)
        self.widget_3.setObjectName(u"widget_3")
        self.verticalLayout_5 = QVBoxLayout(self.widget_3)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setSpacing(20)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.radioButton_11 = QRadioButton(self.widget_3)
        self.buttonGroup_2 = QButtonGroup(MainWindow)
        self.buttonGroup_2.setObjectName(u"buttonGroup_2")
        self.buttonGroup_2.addButton(self.radioButton_11)
        self.radioButton_11.setObjectName(u"radioButton_11")
        self.radioButton_11.setChecked(True)

        self.horizontalLayout_12.addWidget(self.radioButton_11)

        self.radioButton_12 = QRadioButton(self.widget_3)
        self.buttonGroup_2.addButton(self.radioButton_12)
        self.radioButton_12.setObjectName(u"radioButton_12")

        self.horizontalLayout_12.addWidget(self.radioButton_12)

        self.horizontalLayout_12.setStretch(1, 1)

        self.verticalLayout_5.addLayout(self.horizontalLayout_12)


        self.formLayout_2.setWidget(7, QFormLayout.FieldRole, self.widget_3)

        self.label_32 = QLabel(self.widget)
        self.label_32.setObjectName(u"label_32")

        self.formLayout_2.setWidget(8, QFormLayout.LabelRole, self.label_32)

        self.widget_5 = QWidget(self.widget)
        self.widget_5.setObjectName(u"widget_5")
        self.verticalLayout_7 = QVBoxLayout(self.widget_5)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.checkBox_4 = QCheckBox(self.widget_5)
        self.buttonGroup_4 = QButtonGroup(MainWindow)
        self.buttonGroup_4.setObjectName(u"buttonGroup_4")
        self.buttonGroup_4.setExclusive(False)
        self.buttonGroup_4.addButton(self.checkBox_4)
        self.checkBox_4.setObjectName(u"checkBox_4")

        self.horizontalLayout_11.addWidget(self.checkBox_4)

        self.checkBox_5 = QCheckBox(self.widget_5)
        self.buttonGroup_4.addButton(self.checkBox_5)
        self.checkBox_5.setObjectName(u"checkBox_5")

        self.horizontalLayout_11.addWidget(self.checkBox_5)

        self.checkBox_6 = QCheckBox(self.widget_5)
        self.buttonGroup_4.addButton(self.checkBox_6)
        self.checkBox_6.setObjectName(u"checkBox_6")

        self.horizontalLayout_11.addWidget(self.checkBox_6)

        self.horizontalLayout_11.setStretch(2, 1)

        self.verticalLayout_7.addLayout(self.horizontalLayout_11)


        self.formLayout_2.setWidget(8, QFormLayout.FieldRole, self.widget_5)


        self.verticalLayout_4.addLayout(self.formLayout_2)


        self.verticalLayout_8.addWidget(self.widget)

        self.horizontalSpacer_11 = QSpacerItem(580, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.verticalLayout_8.addItem(self.horizontalSpacer_11)

        self.label_33 = QLabel(self.scrollAreaWidgetContents)
        self.label_33.setObjectName(u"label_33")

        self.verticalLayout_8.addWidget(self.label_33)

        self.tableWidget = QTableWidget(self.scrollAreaWidgetContents)
        if (self.tableWidget.columnCount() < 6):
            self.tableWidget.setColumnCount(6)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        if (self.tableWidget.rowCount() < 3):
            self.tableWidget.setRowCount(3)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tableWidget.setItem(0, 0, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tableWidget.setItem(0, 1, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tableWidget.setItem(0, 2, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tableWidget.setItem(0, 3, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.tableWidget.setItem(0, 4, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.tableWidget.setItem(0, 5, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.tableWidget.setItem(1, 0, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.tableWidget.setItem(1, 1, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.tableWidget.setItem(1, 2, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.tableWidget.setItem(1, 3, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.tableWidget.setItem(1, 4, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.tableWidget.setItem(1, 5, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        self.tableWidget.setItem(2, 0, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        self.tableWidget.setItem(2, 1, __qtablewidgetitem22)
        __qtablewidgetitem23 = QTableWidgetItem()
        self.tableWidget.setItem(2, 2, __qtablewidgetitem23)
        __qtablewidgetitem24 = QTableWidgetItem()
        self.tableWidget.setItem(2, 3, __qtablewidgetitem24)
        __qtablewidgetitem25 = QTableWidgetItem()
        self.tableWidget.setItem(2, 4, __qtablewidgetitem25)
        __qtablewidgetitem26 = QTableWidgetItem()
        self.tableWidget.setItem(2, 5, __qtablewidgetitem26)
        self.tableWidget.setObjectName(u"tableWidget")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy2)
        self.tableWidget.setMinimumSize(QSize(0, 0))

        self.verticalLayout_8.addWidget(self.tableWidget)

        self.horizontalSpacer_12 = QSpacerItem(580, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.verticalLayout_8.addItem(self.horizontalSpacer_12)

        self.label_37 = QLabel(self.scrollAreaWidgetContents)
        self.label_37.setObjectName(u"label_37")

        self.verticalLayout_8.addWidget(self.label_37)

        self.widget_6 = QWidget(self.scrollAreaWidgetContents)
        self.widget_6.setObjectName(u"widget_6")
        self.horizontalLayout_13 = QHBoxLayout(self.widget_6)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.pushButton_15 = QPushButton(self.widget_6)
        self.pushButton_15.setObjectName(u"pushButton_15")

        self.horizontalLayout_13.addWidget(self.pushButton_15)

        self.pushButton_16 = QPushButton(self.widget_6)
        self.pushButton_16.setObjectName(u"pushButton_16")

        self.horizontalLayout_13.addWidget(self.pushButton_16)

        self.pushButton_19 = QPushButton(self.widget_6)
        self.pushButton_19.setObjectName(u"pushButton_19")

        self.horizontalLayout_13.addWidget(self.pushButton_19)

        self.pushButton_17 = QPushButton(self.widget_6)
        self.pushButton_17.setObjectName(u"pushButton_17")

        self.horizontalLayout_13.addWidget(self.pushButton_17)

        self.pushButton_18 = QPushButton(self.widget_6)
        self.pushButton_18.setObjectName(u"pushButton_18")

        self.horizontalLayout_13.addWidget(self.pushButton_18)

        self.label_40 = QLabel(self.widget_6)
        self.label_40.setObjectName(u"label_40")

        self.horizontalLayout_13.addWidget(self.label_40)

        self.label_38 = QLabel(self.widget_6)
        self.label_38.setObjectName(u"label_38")

        self.horizontalLayout_13.addWidget(self.label_38)

        self.lineEdit_2 = QLineEdit(self.widget_6)
        self.lineEdit_2.setObjectName(u"lineEdit_2")

        self.horizontalLayout_13.addWidget(self.lineEdit_2)

        self.label_39 = QLabel(self.widget_6)
        self.label_39.setObjectName(u"label_39")

        self.horizontalLayout_13.addWidget(self.label_39)

        self.horizontalLayout_13.setStretch(8, 1)

        self.verticalLayout_8.addWidget(self.widget_6)

        self.widget_7 = QWidget(self.scrollAreaWidgetContents)
        self.widget_7.setObjectName(u"widget_7")
        self.horizontalLayout_14 = QHBoxLayout(self.widget_7)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.pushButton_20 = QPushButton(self.widget_7)
        self.pushButton_20.setObjectName(u"pushButton_20")

        self.horizontalLayout_14.addWidget(self.pushButton_20)

        self.pushButton_21 = QPushButton(self.widget_7)
        self.pushButton_21.setObjectName(u"pushButton_21")

        self.horizontalLayout_14.addWidget(self.pushButton_21)

        self.pushButton_22 = QPushButton(self.widget_7)
        self.pushButton_22.setObjectName(u"pushButton_22")

        self.horizontalLayout_14.addWidget(self.pushButton_22)

        self.pushButton_23 = QPushButton(self.widget_7)
        self.pushButton_23.setObjectName(u"pushButton_23")

        self.horizontalLayout_14.addWidget(self.pushButton_23)

        self.pushButton_24 = QPushButton(self.widget_7)
        self.pushButton_24.setObjectName(u"pushButton_24")

        self.horizontalLayout_14.addWidget(self.pushButton_24)

        self.label_41 = QLabel(self.widget_7)
        self.label_41.setObjectName(u"label_41")

        self.horizontalLayout_14.addWidget(self.label_41)

        self.label_42 = QLabel(self.widget_7)
        self.label_42.setObjectName(u"label_42")

        self.horizontalLayout_14.addWidget(self.label_42)

        self.lineEdit_3 = QLineEdit(self.widget_7)
        self.lineEdit_3.setObjectName(u"lineEdit_3")

        self.horizontalLayout_14.addWidget(self.lineEdit_3)

        self.label_43 = QLabel(self.widget_7)
        self.label_43.setObjectName(u"label_43")

        self.horizontalLayout_14.addWidget(self.label_43)

        self.horizontalLayout_14.setStretch(8, 1)

        self.verticalLayout_8.addWidget(self.widget_7)

        self.horizontalSpacer_13 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.verticalLayout_8.addItem(self.horizontalSpacer_13)

        self.label_34 = QLabel(self.scrollAreaWidgetContents)
        self.label_34.setObjectName(u"label_34")

        self.verticalLayout_8.addWidget(self.label_34)

        self.tabWidget = QTabWidget(self.scrollAreaWidgetContents)
        self.tabWidget.setObjectName(u"tabWidget")
        sizePolicy2.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy2)
        self.tabWidget.setMinimumSize(QSize(0, 100))
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.label_36 = QLabel(self.tab)
        self.label_36.setObjectName(u"label_36")
        self.label_36.setGeometry(QRect(80, 20, 55, 16))
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.label_35 = QLabel(self.tab_2)
        self.label_35.setObjectName(u"label_35")
        self.label_35.setGeometry(QRect(80, 20, 55, 16))
        self.tabWidget.addTab(self.tab_2, "")

        self.verticalLayout_8.addWidget(self.tabWidget)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.content_layout.addWidget(self.scrollArea)


        self.main_layout.addLayout(self.content_layout)


        self.verticalLayout_2.addLayout(self.main_layout)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"\u6807\u7b7e QLabel", None))
        self.label_8.setProperty("class", QCoreApplication.translate("MainWindow", u"h2", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u4e00\u7ea7\u6807\u9898H1  class=h1", None))
        self.label_2.setProperty("class", QCoreApplication.translate("MainWindow", u"h1", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u4e8c\u7ea7\u6807\u9898H2  class=h2", None))
        self.label_3.setProperty("class", QCoreApplication.translate("MainWindow", u"h2", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u4e09\u7ea7\u6807\u9898H3  class=h3", None))
        self.label_4.setProperty("class", QCoreApplication.translate("MainWindow", u"h3", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u56db\u7ea7\u6807\u9898H4  class=h4", None))
        self.label_5.setProperty("class", QCoreApplication.translate("MainWindow", u"h4", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"\u4e94\u7ea7\u6807\u9898H5  class=h5", None))
        self.label_6.setProperty("class", QCoreApplication.translate("MainWindow", u"h5", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"\u9ed8\u8ba4\u6807\u7b7e\u6587\u5b57", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"\u6309\u94ae QPushButton", None))
        self.label_10.setProperty("class", QCoreApplication.translate("MainWindow", u"h2", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"\u7981\u7528\u6309\u94ae enable=False", None))
        self.pushButton_10.setText(QCoreApplication.translate("MainWindow", u"\u5371\u9669\u6309\u94ae\u9009\u4e2d  checkable", None))
        self.pushButton_10.setProperty("class", QCoreApplication.translate("MainWindow", u"danger", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"\u9ed8\u8ba4\u6309\u94ae", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"\u9ed8\u8ba4\u6309\u94ae\u9009\u4e2d checkable", None))
        self.pushButton_12.setText(QCoreApplication.translate("MainWindow", u"\u6210\u529f\u6309\u94ae\u9009\u4e2d checkable", None))
        self.pushButton_12.setProperty("class", QCoreApplication.translate("MainWindow", u"success", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"\u4e3b\u8981\u6309\u94ae class=primary", None))
        self.pushButton_5.setProperty("class", QCoreApplication.translate("MainWindow", u"primary", None))
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"\u4e3b\u8981\u6309\u94ae\u9009\u4e2d checkable", None))
        self.pushButton_6.setProperty("class", QCoreApplication.translate("MainWindow", u"primary", None))
        self.pushButton_8.setText(QCoreApplication.translate("MainWindow", u"\u8b66\u544a\u6309\u94ae\u9009\u4e2d checkable", None))
        self.pushButton_8.setProperty("class", QCoreApplication.translate("MainWindow", u"warning", None))
        self.pushButton_9.setText(QCoreApplication.translate("MainWindow", u"\u5371\u9669\u6309\u94ae class=danger", None))
        self.pushButton_9.setProperty("class", QCoreApplication.translate("MainWindow", u"danger", None))
        self.pushButton_7.setText(QCoreApplication.translate("MainWindow", u"\u8b66\u544a\u6309\u94ae class=warning", None))
        self.pushButton_7.setProperty("class", QCoreApplication.translate("MainWindow", u"warning", None))
        self.pushButton_11.setText(QCoreApplication.translate("MainWindow", u"\u6210\u529f\u6309\u94ae class=success", None))
        self.pushButton_11.setProperty("class", QCoreApplication.translate("MainWindow", u"success", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"\u6309\u94ae\u5c3a\u5bf8\u5927 sizes=large", None))
        self.pushButton_4.setProperty("sizes", QCoreApplication.translate("MainWindow", u"large", None))
        self.pushButton_4.setProperty("class", QCoreApplication.translate("MainWindow", u"primary", None))
        self.pushButton_13.setText(QCoreApplication.translate("MainWindow", u"\u6309\u94ae\u5c3a\u5bf8\u5c0f sizes=mini", None))
        self.pushButton_13.setProperty("sizes", QCoreApplication.translate("MainWindow", u"mini", None))
        self.pushButton_13.setProperty("class", QCoreApplication.translate("MainWindow", u"primary", None))
        self.pushButton_14.setText(QCoreApplication.translate("MainWindow", u"\u5706\u89d2\u6309\u94ae shape=circle", None))
        self.pushButton_14.setProperty("class", QCoreApplication.translate("MainWindow", u"primary", None))
        self.pushButton_14.setProperty("shape", QCoreApplication.translate("MainWindow", u"circle", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"\u8f93\u5165\u6846 QLineEdit", None))
        self.label_12.setProperty("class", QCoreApplication.translate("MainWindow", u"h2", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u666e\u901a\u6587\u672c\u6846", None))
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u8bf7\u8f93\u5165\u6587\u5b57", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"\u591a\u884c\u6587\u672c\u6846 QTextEdit", None))
        self.label_9.setProperty("class", QCoreApplication.translate("MainWindow", u"h2", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"\u591a\u884c\u6587\u672c\u6846", None))
        self.textEdit.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Microsoft YaHei UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:28pt;\">\u4e00\u7ea7\u6807\u9898</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:24pt;\">\u4e8c\u7ea7\u6807\u9898</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:20pt;\">\u4e09\u7ea7\u6807\u9898</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-r"
                        "ight:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt;\">\u56db\u7ea7\u6807\u9898</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt;\">\u4e94\u7ea7\u6807\u9898</span></p></body></html>", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"\u6574\u578b\u6b65\u957f\u8f93\u5165\u6846 QSpinBox", None))
        self.label_15.setProperty("class", QCoreApplication.translate("MainWindow", u"h2", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"\u5e74\u9f84\uff1a", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"\u6d6e\u70b9\u578b\u6b65\u957f\u8f93\u5165\u6846 QDoubleSpinBox", None))
        self.label_17.setProperty("class", QCoreApplication.translate("MainWindow", u"h2", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"\u4ef7\u683c\uff1a", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"\u65e5\u671f\u6b65\u957f\u8f93\u5165\u6846 QDateTimeEdit", None))
        self.label_19.setProperty("class", QCoreApplication.translate("MainWindow", u"h2", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"\u5f00\u59cb\u65f6\u95f4\uff1a", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"\u4e0b\u62c9\u9009\u62e9\u6846 QComboBox", None))
        self.label_24.setProperty("class", QCoreApplication.translate("MainWindow", u"h2", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"\u6240\u5728\u57ce\u5e02\uff1a", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"\u4e0a\u6d77", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"\u5e7f\u5dde", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"\u676d\u5dde", None))
        self.comboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"\u5317\u4eac", None))
        self.comboBox.setItemText(4, QCoreApplication.translate("MainWindow", u"\u6df1\u5733", None))

        self.comboBox.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u8bf7\u9009\u62e9", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"\u5355\u9009\u6309\u94ae QRadioButton \u9700\u8981\u7528widget\u5305\u88f9class=radio", None))
        self.label_27.setProperty("class", QCoreApplication.translate("MainWindow", u"h2", None))
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"\u6027\u522b:", None))
        self.widget_2.setProperty("class", QCoreApplication.translate("MainWindow", u"radio", None))
        self.radioButton_5.setText(QCoreApplication.translate("MainWindow", u"\u7537", None))
        self.radioButton_6.setText(QCoreApplication.translate("MainWindow", u"\u5973", None))
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"\u590d\u9009\u6846 QCheckBox  \u9700\u8981\u7528widget\u5305\u88f9class=checkbox", None))
        self.label_30.setProperty("class", QCoreApplication.translate("MainWindow", u"h2", None))
        self.label_31.setText(QCoreApplication.translate("MainWindow", u"\u57ce\u5e02", None))
        self.widget_4.setProperty("class", QCoreApplication.translate("MainWindow", u"checkbox", None))
        self.checkBox.setText(QCoreApplication.translate("MainWindow", u"\u4e0a\u6d77", None))
        self.checkBox_2.setText(QCoreApplication.translate("MainWindow", u"\u676d\u5dde", None))
        self.checkBox_3.setText(QCoreApplication.translate("MainWindow", u"\u5317\u4eac", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"\u8868\u5355 QFromLayout \u9700\u8981\u7528widget\u5305\u88f9class=\"form\"", None))
        self.label_11.setProperty("class", QCoreApplication.translate("MainWindow", u"h2", None))
        self.widget.setProperty("class", QCoreApplication.translate("MainWindow", u"form", None))
        self.Label.setText(QCoreApplication.translate("MainWindow", u"\u8d26\u53f7\uff1a", None))
        self.LineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u8bf7\u8f93\u5165\u8d26\u53f7", None))
        self.Label_2.setText(QCoreApplication.translate("MainWindow", u"\u5bc6\u7801\uff1a", None))
        self.LineEdit_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u8bf7\u8f93\u5165\u5bc6\u7801", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"\u591a\u884c\u6587\u672c\u6846\uff1a", None))
        self.textEdit_2.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Microsoft YaHei UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:28pt;\">\u4e00\u7ea7\u6807\u9898</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:24pt;\">\u4e8c\u7ea7\u6807\u9898</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:20pt;\">\u4e09\u7ea7\u6807\u9898</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-r"
                        "ight:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt;\">\u56db\u7ea7\u6807\u9898</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt;\">\u4e94\u7ea7\u6807\u9898</span></p></body></html>", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"\u5e74\u9f84\uff1a", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"\u4ef7\u683c\uff1a", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"\u5f00\u59cb\u65f6\u95f4\uff1a", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"\u6240\u5728\u57ce\u5e02\uff1a", None))
        self.comboBox_2.setItemText(0, QCoreApplication.translate("MainWindow", u"\u4e0a\u6d77", None))
        self.comboBox_2.setItemText(1, QCoreApplication.translate("MainWindow", u"\u5e7f\u5dde", None))
        self.comboBox_2.setItemText(2, QCoreApplication.translate("MainWindow", u"\u676d\u5dde", None))
        self.comboBox_2.setItemText(3, QCoreApplication.translate("MainWindow", u"\u5317\u4eac", None))
        self.comboBox_2.setItemText(4, QCoreApplication.translate("MainWindow", u"\u6df1\u5733", None))

        self.comboBox_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u8bf7\u9009\u62e9", None))
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"\u6027\u522b:", None))
        self.widget_3.setProperty("class", QCoreApplication.translate("MainWindow", u"radio", None))
        self.radioButton_11.setText(QCoreApplication.translate("MainWindow", u"\u7537", None))
        self.radioButton_12.setText(QCoreApplication.translate("MainWindow", u"\u5973", None))
        self.label_32.setText(QCoreApplication.translate("MainWindow", u"\u57ce\u5e02", None))
        self.widget_5.setProperty("class", QCoreApplication.translate("MainWindow", u"checkbox", None))
        self.checkBox_4.setText(QCoreApplication.translate("MainWindow", u"\u4e0a\u6d77", None))
        self.checkBox_5.setText(QCoreApplication.translate("MainWindow", u"\u676d\u5dde", None))
        self.checkBox_6.setText(QCoreApplication.translate("MainWindow", u"\u5317\u4eac", None))
        self.label_33.setText(QCoreApplication.translate("MainWindow", u"\u8868\u683c QTableWidget", None))
        self.label_33.setProperty("class", QCoreApplication.translate("MainWindow", u"h2", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"id", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"\u5bc6\u7801", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"ip", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"\u767b\u5f55\u65f6\u95f4", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"\u6ce8\u518c\u65f6\u95f4", None));
        ___qtablewidgetitem5 = self.tableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"token", None));
        ___qtablewidgetitem6 = self.tableWidget.verticalHeaderItem(0)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"1", None));
        ___qtablewidgetitem7 = self.tableWidget.verticalHeaderItem(1)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"2", None));
        ___qtablewidgetitem8 = self.tableWidget.verticalHeaderItem(2)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"3", None));

        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        ___qtablewidgetitem9 = self.tableWidget.item(0, 0)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"1", None));
        ___qtablewidgetitem10 = self.tableWidget.item(0, 1)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"dsadasds", None));
        ___qtablewidgetitem11 = self.tableWidget.item(0, 2)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"120.99.88.11", None));
        ___qtablewidgetitem12 = self.tableWidget.item(0, 3)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"1952245855", None));
        ___qtablewidgetitem13 = self.tableWidget.item(0, 4)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"1952245855", None));
        ___qtablewidgetitem14 = self.tableWidget.item(0, 5)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"123dasdas2321dsad", None));
        ___qtablewidgetitem15 = self.tableWidget.item(1, 0)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"2", None));
        ___qtablewidgetitem16 = self.tableWidget.item(1, 1)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MainWindow", u"dsadasds", None));
        ___qtablewidgetitem17 = self.tableWidget.item(1, 2)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("MainWindow", u"120.99.88.11", None));
        ___qtablewidgetitem18 = self.tableWidget.item(1, 3)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("MainWindow", u"1952245855", None));
        ___qtablewidgetitem19 = self.tableWidget.item(1, 4)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("MainWindow", u"1952245855", None));
        ___qtablewidgetitem20 = self.tableWidget.item(1, 5)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("MainWindow", u"123dasdas2321dsad", None));
        ___qtablewidgetitem21 = self.tableWidget.item(2, 0)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("MainWindow", u"3", None));
        ___qtablewidgetitem22 = self.tableWidget.item(2, 1)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("MainWindow", u"dsadasds", None));
        ___qtablewidgetitem23 = self.tableWidget.item(2, 2)
        ___qtablewidgetitem23.setText(QCoreApplication.translate("MainWindow", u"120.99.88.11", None));
        ___qtablewidgetitem24 = self.tableWidget.item(2, 3)
        ___qtablewidgetitem24.setText(QCoreApplication.translate("MainWindow", u"1952245855", None));
        ___qtablewidgetitem25 = self.tableWidget.item(2, 4)
        ___qtablewidgetitem25.setText(QCoreApplication.translate("MainWindow", u"1952245855", None));
        ___qtablewidgetitem26 = self.tableWidget.item(2, 5)
        ___qtablewidgetitem26.setText(QCoreApplication.translate("MainWindow", u"123dasdas2321dsad", None));
        self.tableWidget.setSortingEnabled(__sortingEnabled)

        self.label_37.setText(QCoreApplication.translate("MainWindow", u"\u5206\u9875\u5668 \u9700\u8981\u7528widget\u5305\u88f9class=\"pagination\"", None))
        self.label_37.setProperty("class", QCoreApplication.translate("MainWindow", u"h2", None))
        self.widget_6.setProperty("class", QCoreApplication.translate("MainWindow", u"pagination", None))
        self.pushButton_15.setText(QCoreApplication.translate("MainWindow", u"\u9996\u9875", None))
        self.pushButton_16.setText(QCoreApplication.translate("MainWindow", u"\u4e0a\u4e00\u9875", None))
        self.pushButton_19.setText(QCoreApplication.translate("MainWindow", u"99", None))
        self.pushButton_17.setText(QCoreApplication.translate("MainWindow", u"\u4e0b\u4e00\u9875", None))
        self.pushButton_18.setText(QCoreApplication.translate("MainWindow", u"\u5c3e\u9875", None))
        self.label_40.setText(QCoreApplication.translate("MainWindow", u"\u5171 99 \u9875", None))
        self.label_38.setText(QCoreApplication.translate("MainWindow", u"\u8df3\u8f6c\u5230", None))
        self.label_39.setText(QCoreApplication.translate("MainWindow", u"\u9875", None))
        self.widget_7.setProperty("class", QCoreApplication.translate("MainWindow", u"pagination", None))
        self.pushButton_20.setText(QCoreApplication.translate("MainWindow", u"\u9996\u9875", None))
        self.pushButton_20.setProperty("class", QCoreApplication.translate("MainWindow", u"primary", None))
        self.pushButton_21.setText(QCoreApplication.translate("MainWindow", u"\u4e0a\u4e00\u9875", None))
        self.pushButton_21.setProperty("class", QCoreApplication.translate("MainWindow", u"primary", None))
        self.pushButton_22.setText(QCoreApplication.translate("MainWindow", u"99", None))
        self.pushButton_22.setProperty("class", QCoreApplication.translate("MainWindow", u"primary", None))
        self.pushButton_23.setText(QCoreApplication.translate("MainWindow", u"\u4e0b\u4e00\u9875", None))
        self.pushButton_23.setProperty("class", QCoreApplication.translate("MainWindow", u"primary", None))
        self.pushButton_24.setText(QCoreApplication.translate("MainWindow", u"\u5c3e\u9875", None))
        self.pushButton_24.setProperty("class", QCoreApplication.translate("MainWindow", u"primary", None))
        self.label_41.setText(QCoreApplication.translate("MainWindow", u"\u5171 99 \u9875", None))
        self.label_42.setText(QCoreApplication.translate("MainWindow", u"\u8df3\u8f6c\u5230", None))
        self.label_43.setText(QCoreApplication.translate("MainWindow", u"\u9875", None))
        self.label_34.setText(QCoreApplication.translate("MainWindow", u"\u9009\u9879\u5361 QTabWidget", None))
        self.label_34.setProperty("class", QCoreApplication.translate("MainWindow", u"h2", None))
        self.label_36.setText(QCoreApplication.translate("MainWindow", u"\u5185\u5bb9\u4e00", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"\u9009\u9879\u53611", None))
        self.label_35.setText(QCoreApplication.translate("MainWindow", u"\u5185\u5bb9\u4e8c", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"\u9009\u9879\u53612", None))
    # retranslateUi

