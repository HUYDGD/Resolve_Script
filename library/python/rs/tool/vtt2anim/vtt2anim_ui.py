# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\yoshi\PycharmProjects\Resolve_Script\library\python\rs\tool\vtt2anim\vtt2anim.ui',
# licensing of 'C:\Users\yoshi\PycharmProjects\Resolve_Script\library\python\rs\tool\vtt2anim\vtt2anim.ui' applies.
#
# Created: Tue Jun  7 06:27:36 2022
#      by: pyside2-uic  running on PySide2 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(576, 538)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox = QtWidgets.QGroupBox(Form)
        self.groupBox.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.groupBox.setObjectName("groupBox")
        self.formLayout = QtWidgets.QFormLayout(self.groupBox)
        self.formLayout.setObjectName("formLayout")
        self.label_8 = QtWidgets.QLabel(self.groupBox)
        self.label_8.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_8.setObjectName("label_8")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_8)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 0, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 0, 2, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.groupBox)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 0, 4, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.groupBox)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 0, 6, 1, 1)
        self.hSpinBox = QtWidgets.QSpinBox(self.groupBox)
        self.hSpinBox.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.hSpinBox.setMaximum(24)
        self.hSpinBox.setObjectName("hSpinBox")
        self.gridLayout.addWidget(self.hSpinBox, 1, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setMinimumSize(QtCore.QSize(0, 0))
        self.label_2.setMaximumSize(QtCore.QSize(15, 16777215))
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 1, 1, 1)
        self.mSpinBox = QtWidgets.QSpinBox(self.groupBox)
        self.mSpinBox.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.mSpinBox.setMaximum(59)
        self.mSpinBox.setObjectName("mSpinBox")
        self.gridLayout.addWidget(self.mSpinBox, 1, 2, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setMaximumSize(QtCore.QSize(15, 16777215))
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 1, 3, 1, 1)
        self.sSpinBox = QtWidgets.QSpinBox(self.groupBox)
        self.sSpinBox.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.sSpinBox.setMaximum(59)
        self.sSpinBox.setObjectName("sSpinBox")
        self.gridLayout.addWidget(self.sSpinBox, 1, 4, 1, 1)
        self.label8 = QtWidgets.QLabel(self.groupBox)
        self.label8.setMaximumSize(QtCore.QSize(15, 16777215))
        self.label8.setAlignment(QtCore.Qt.AlignCenter)
        self.label8.setObjectName("label8")
        self.gridLayout.addWidget(self.label8, 1, 5, 1, 1)
        self.msSpinBox = QtWidgets.QSpinBox(self.groupBox)
        self.msSpinBox.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.msSpinBox.setMaximum(999)
        self.msSpinBox.setObjectName("msSpinBox")
        self.gridLayout.addWidget(self.msSpinBox, 1, 6, 1, 1)
        self.formLayout.setLayout(0, QtWidgets.QFormLayout.FieldRole, self.gridLayout)
        self.label_9 = QtWidgets.QLabel(self.groupBox)
        self.label_9.setObjectName("label_9")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_9)
        self.fpsDoubleSpinBox = QtWidgets.QDoubleSpinBox(self.groupBox)
        self.fpsDoubleSpinBox.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.fpsDoubleSpinBox.setObjectName("fpsDoubleSpinBox")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.fpsDoubleSpinBox)
        self.verticalLayout.addWidget(self.groupBox)
        self.groupBox_2 = QtWidgets.QGroupBox(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy)
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.dropLabel = QtWidgets.QLabel(self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dropLabel.sizePolicy().hasHeightForWidth())
        self.dropLabel.setSizePolicy(sizePolicy)
        self.dropLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.dropLabel.setObjectName("dropLabel")
        self.verticalLayout_2.addWidget(self.dropLabel)
        self.verticalLayout.addWidget(self.groupBox_2)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtWidgets.QApplication.translate("Form", "Form", None, -1))
        self.groupBox.setTitle(QtWidgets.QApplication.translate("Form", "Setting", None, -1))
        self.label_8.setText(QtWidgets.QApplication.translate("Form", "\n"
"Start timecode", None, -1))
        self.label_4.setText(QtWidgets.QApplication.translate("Form", "00 h", None, -1))
        self.label_5.setText(QtWidgets.QApplication.translate("Form", "00 m", None, -1))
        self.label_6.setText(QtWidgets.QApplication.translate("Form", "00 s", None, -1))
        self.label_7.setText(QtWidgets.QApplication.translate("Form", "000 ms", None, -1))
        self.label_2.setText(QtWidgets.QApplication.translate("Form", ":", None, -1))
        self.label_3.setText(QtWidgets.QApplication.translate("Form", ":", None, -1))
        self.label8.setText(QtWidgets.QApplication.translate("Form", ".", None, -1))
        self.label_9.setText(QtWidgets.QApplication.translate("Form", "FPS", None, -1))
        self.groupBox_2.setTitle(QtWidgets.QApplication.translate("Form", "DROP AREA", None, -1))
        self.dropLabel.setText(QtWidgets.QApplication.translate("Form", "TextLabel", None, -1))
