# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\yoshi\PycharmProjects\Resolve_Script\app\fusion\python\rs_fusion\tool\tatie\tatie.ui',
# licensing of 'C:\Users\yoshi\PycharmProjects\Resolve_Script\app\fusion\python\rs_fusion\tool\tatie\tatie.ui' applies.
#
# Created: Sun Sep 11 05:19:33 2022
#      by: pyside2-uic  running on PySide2 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(460, 458)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.openDirButton = QtWidgets.QPushButton(self.centralwidget)
        self.openDirButton.setMinimumSize(QtCore.QSize(100, 40))
        self.openDirButton.setObjectName("openDirButton")
        self.verticalLayout_4.addWidget(self.openDirButton)
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName("verticalLayout")
        self.multiplyCheckBox = QtWidgets.QCheckBox(self.groupBox)
        self.multiplyCheckBox.setObjectName("multiplyCheckBox")
        self.verticalLayout.addWidget(self.multiplyCheckBox)
        spacerItem = QtWidgets.QSpacerItem(20, 0, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.verticalLayout_4.addWidget(self.groupBox)
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.groupBox_3 = QtWidgets.QGroupBox(self.groupBox_2)
        self.groupBox_3.setObjectName("groupBox_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.groupBox_3)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(self.groupBox_3)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.widthSpinBox = QtWidgets.QSpinBox(self.groupBox_3)
        self.widthSpinBox.setMinimumSize(QtCore.QSize(100, 0))
        self.widthSpinBox.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.widthSpinBox.setMinimum(1)
        self.widthSpinBox.setMaximum(999999)
        self.widthSpinBox.setDisplayIntegerBase(10)
        self.widthSpinBox.setObjectName("widthSpinBox")
        self.horizontalLayout.addWidget(self.widthSpinBox)
        spacerItem1 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.label_3 = QtWidgets.QLabel(self.groupBox_3)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.heightSpinBox = QtWidgets.QSpinBox(self.groupBox_3)
        self.heightSpinBox.setMinimumSize(QtCore.QSize(100, 0))
        self.heightSpinBox.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.heightSpinBox.setMinimum(1)
        self.heightSpinBox.setMaximum(999999)
        self.heightSpinBox.setObjectName("heightSpinBox")
        self.horizontalLayout.addWidget(self.heightSpinBox)
        spacerItem2 = QtWidgets.QSpacerItem(8, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.verticalLayout_3.addWidget(self.groupBox_3)
        self.cbGroupBox = QtWidgets.QGroupBox(self.groupBox_2)
        self.cbGroupBox.setCheckable(False)
        self.cbGroupBox.setChecked(False)
        self.cbGroupBox.setObjectName("cbGroupBox")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.cbGroupBox)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.groupBox_4 = QtWidgets.QGroupBox(self.cbGroupBox)
        self.groupBox_4.setObjectName("groupBox_4")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.groupBox_4)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.chkRadioButton = QtWidgets.QRadioButton(self.groupBox_4)
        self.chkRadioButton.setObjectName("chkRadioButton")
        self.horizontalLayout_4.addWidget(self.chkRadioButton)
        self.cmbRadioButton = QtWidgets.QRadioButton(self.groupBox_4)
        self.cmbRadioButton.setChecked(True)
        self.cmbRadioButton.setObjectName("cmbRadioButton")
        self.horizontalLayout_4.addWidget(self.cmbRadioButton)
        self.sldRadioButton = QtWidgets.QRadioButton(self.groupBox_4)
        self.sldRadioButton.setObjectName("sldRadioButton")
        self.horizontalLayout_4.addWidget(self.sldRadioButton)
        spacerItem3 = QtWidgets.QSpacerItem(90, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem3)
        self.verticalLayout_2.addWidget(self.groupBox_4)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label = QtWidgets.QLabel(self.cbGroupBox)
        self.label.setObjectName("label")
        self.horizontalLayout_3.addWidget(self.label)
        self.ctrlNameLineEdit = QtWidgets.QLineEdit(self.cbGroupBox)
        self.ctrlNameLineEdit.setObjectName("ctrlNameLineEdit")
        self.horizontalLayout_3.addWidget(self.ctrlNameLineEdit)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.verticalLayout_3.addWidget(self.cbGroupBox)
        spacerItem4 = QtWidgets.QSpacerItem(20, 2, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem4)
        self.verticalLayout_4.addWidget(self.groupBox_2)
        self.groupBox_5 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_5.setObjectName("groupBox_5")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.groupBox_5)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.openSiteButton = QtWidgets.QPushButton(self.groupBox_5)
        self.openSiteButton.setMinimumSize(QtCore.QSize(100, 40))
        self.openSiteButton.setObjectName("openSiteButton")
        self.horizontalLayout_5.addWidget(self.openSiteButton)
        self.openFuseDirButton = QtWidgets.QPushButton(self.groupBox_5)
        self.openFuseDirButton.setMinimumSize(QtCore.QSize(100, 40))
        self.openFuseDirButton.setObjectName("openFuseDirButton")
        self.horizontalLayout_5.addWidget(self.openFuseDirButton)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem5)
        self.verticalLayout_4.addWidget(self.groupBox_5)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem6 = QtWidgets.QSpacerItem(13, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem6)
        self.loaderButton = QtWidgets.QPushButton(self.centralwidget)
        self.loaderButton.setMinimumSize(QtCore.QSize(100, 40))
        self.loaderButton.setObjectName("loaderButton")
        self.horizontalLayout_2.addWidget(self.loaderButton)
        self.margeButton = QtWidgets.QPushButton(self.centralwidget)
        self.margeButton.setMinimumSize(QtCore.QSize(100, 40))
        self.margeButton.setObjectName("margeButton")
        self.horizontalLayout_2.addWidget(self.margeButton)
        self.switchButton = QtWidgets.QPushButton(self.centralwidget)
        self.switchButton.setMinimumSize(QtCore.QSize(100, 40))
        self.switchButton.setObjectName("switchButton")
        self.horizontalLayout_2.addWidget(self.switchButton)
        spacerItem7 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem7)
        self.closeButton = QtWidgets.QPushButton(self.centralwidget)
        self.closeButton.setMinimumSize(QtCore.QSize(100, 40))
        self.closeButton.setObjectName("closeButton")
        self.horizontalLayout_2.addWidget(self.closeButton)
        self.verticalLayout_4.addLayout(self.horizontalLayout_2)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtWidgets.QApplication.translate("MainWindow", "MainWindow", None, -1))
        self.openDirButton.setText(QtWidgets.QApplication.translate("MainWindow", "Generators テンプレートフォルダを開く", None, -1))
        self.groupBox.setTitle(QtWidgets.QApplication.translate("MainWindow", "静止画読み込み(Loader)", None, -1))
        self.multiplyCheckBox.setText(QtWidgets.QApplication.translate("MainWindow", "Post-Multiply by Alpha", None, -1))
        self.groupBox_2.setTitle(QtWidgets.QApplication.translate("MainWindow", " マージ", None, -1))
        self.groupBox_3.setTitle(QtWidgets.QApplication.translate("MainWindow", "BG", None, -1))
        self.label_2.setText(QtWidgets.QApplication.translate("MainWindow", "幅", None, -1))
        self.label_3.setText(QtWidgets.QApplication.translate("MainWindow", "高さ", None, -1))
        self.cbGroupBox.setTitle(QtWidgets.QApplication.translate("MainWindow", "コントローラ", None, -1))
        self.groupBox_4.setTitle(QtWidgets.QApplication.translate("MainWindow", "タイプ", None, -1))
        self.chkRadioButton.setText(QtWidgets.QApplication.translate("MainWindow", "チェックボックス", None, -1))
        self.cmbRadioButton.setText(QtWidgets.QApplication.translate("MainWindow", "コンボボックス", None, -1))
        self.sldRadioButton.setText(QtWidgets.QApplication.translate("MainWindow", "スライダー", None, -1))
        self.label.setText(QtWidgets.QApplication.translate("MainWindow", "名前", None, -1))
        self.groupBox_5.setTitle(QtWidgets.QApplication.translate("MainWindow", "SwitchFuse", None, -1))
        self.openSiteButton.setText(QtWidgets.QApplication.translate("MainWindow", " ダウンロードページを開く ", None, -1))
        self.openFuseDirButton.setText(QtWidgets.QApplication.translate("MainWindow", " インストールフォルダを開く ", None, -1))
        self.loaderButton.setText(QtWidgets.QApplication.translate("MainWindow", "読み込み", None, -1))
        self.margeButton.setText(QtWidgets.QApplication.translate("MainWindow", "マージ", None, -1))
        self.switchButton.setText(QtWidgets.QApplication.translate("MainWindow", "SwitchFuse", None, -1))
        self.closeButton.setText(QtWidgets.QApplication.translate("MainWindow", "close", None, -1))

