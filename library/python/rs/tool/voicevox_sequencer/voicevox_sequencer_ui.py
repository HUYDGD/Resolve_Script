# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'voicevox_sequencer.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QComboBox, QHBoxLayout,
    QHeaderView, QLabel, QMainWindow, QMenu,
    QMenuBar, QPushButton, QSizePolicy, QSpacerItem,
    QSpinBox, QTextEdit, QVBoxLayout, QWidget)

from rs.gui.log import LogTextEdit
from rs.tool.voicevox_sequencer.seq import View

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(502, 632)
        self.actionNew = QAction(MainWindow)
        self.actionNew.setObjectName(u"actionNew")
        self.actionOpen = QAction(MainWindow)
        self.actionOpen.setObjectName(u"actionOpen")
        self.actionSave = QAction(MainWindow)
        self.actionSave.setObjectName(u"actionSave")
        self.actionCopy = QAction(MainWindow)
        self.actionCopy.setObjectName(u"actionCopy")
        self.actionPaste = QAction(MainWindow)
        self.actionPaste.setObjectName(u"actionPaste")
        self.actionPlay = QAction(MainWindow)
        self.actionPlay.setObjectName(u"actionPlay")
        self.actionWav_Save = QAction(MainWindow)
        self.actionWav_Save.setObjectName(u"actionWav_Save")
        self.actionExit = QAction(MainWindow)
        self.actionExit.setObjectName(u"actionExit")
        self.actionDelete = QAction(MainWindow)
        self.actionDelete.setObjectName(u"actionDelete")
        self.actionUp = QAction(MainWindow)
        self.actionUp.setObjectName(u"actionUp")
        self.actionDown = QAction(MainWindow)
        self.actionDown.setObjectName(u"actionDown")
        self.actionAdd = QAction(MainWindow)
        self.actionAdd.setObjectName(u"actionAdd")
        self.actionEdit = QAction(MainWindow)
        self.actionEdit.setObjectName(u"actionEdit")
        self.actionSave_As = QAction(MainWindow)
        self.actionSave_As.setObjectName(u"actionSave_As")
        self.actionClear = QAction(MainWindow)
        self.actionClear.setObjectName(u"actionClear")
        self.actionImport_From_Clipboard = QAction(MainWindow)
        self.actionImport_From_Clipboard.setObjectName(u"actionImport_From_Clipboard")
        self.actionUndo = QAction(MainWindow)
        self.actionUndo.setObjectName(u"actionUndo")
        self.actionRedo = QAction(MainWindow)
        self.actionRedo.setObjectName(u"actionRedo")
        self.actionDecrement = QAction(MainWindow)
        self.actionDecrement.setObjectName(u"actionDecrement")
        self.actionIncrement = QAction(MainWindow)
        self.actionIncrement.setObjectName(u"actionIncrement")
        self.actionIncrementPlus = QAction(MainWindow)
        self.actionIncrementPlus.setObjectName(u"actionIncrementPlus")
        self.actionDecrementPlus = QAction(MainWindow)
        self.actionDecrementPlus.setObjectName(u"actionDecrementPlus")
        self.actionOpwn_MIDI = QAction(MainWindow)
        self.actionOpwn_MIDI.setObjectName(u"actionOpwn_MIDI")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")

        self.horizontalLayout_2.addWidget(self.label)

        self.speakerComboBox = QComboBox(self.centralwidget)
        self.speakerComboBox.setObjectName(u"speakerComboBox")
        self.speakerComboBox.setMinimumSize(QSize(200, 30))

        self.horizontalLayout_2.addWidget(self.speakerComboBox)

        self.getSpeakerButton = QPushButton(self.centralwidget)
        self.getSpeakerButton.setObjectName(u"getSpeakerButton")
        self.getSpeakerButton.setMinimumSize(QSize(0, 30))
        self.getSpeakerButton.setMaximumSize(QSize(40, 16777215))

        self.horizontalLayout_2.addWidget(self.getSpeakerButton)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_2.addWidget(self.label_2)

        self.tempoSpinBox = QSpinBox(self.centralwidget)
        self.tempoSpinBox.setObjectName(u"tempoSpinBox")
        self.tempoSpinBox.setMinimumSize(QSize(50, 0))
        self.tempoSpinBox.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.tempoSpinBox.setMinimum(5)
        self.tempoSpinBox.setMaximum(999)
        self.tempoSpinBox.setValue(120)

        self.horizontalLayout_2.addWidget(self.tempoSpinBox)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.tableView = View(self.centralwidget)
        self.tableView.setObjectName(u"tableView")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableView.sizePolicy().hasHeightForWidth())
        self.tableView.setSizePolicy(sizePolicy)
        self.tableView.setEditTriggers(QAbstractItemView.DoubleClicked)

        self.verticalLayout.addWidget(self.tableView)

        self.logTextEdit = LogTextEdit(self.centralwidget)
        self.logTextEdit.setObjectName(u"logTextEdit")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.logTextEdit.sizePolicy().hasHeightForWidth())
        self.logTextEdit.setSizePolicy(sizePolicy1)
        self.logTextEdit.setMaximumSize(QSize(16777215, 80))
        self.logTextEdit.setLineWrapMode(QTextEdit.NoWrap)
        self.logTextEdit.setReadOnly(True)

        self.verticalLayout.addWidget(self.logTextEdit)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.playButton = QPushButton(self.centralwidget)
        self.playButton.setObjectName(u"playButton")
        self.playButton.setMinimumSize(QSize(80, 30))

        self.horizontalLayout.addWidget(self.playButton)

        self.playPhraseButton = QPushButton(self.centralwidget)
        self.playPhraseButton.setObjectName(u"playPhraseButton")
        self.playPhraseButton.setMinimumSize(QSize(80, 30))

        self.horizontalLayout.addWidget(self.playPhraseButton)

        self.stopButton = QPushButton(self.centralwidget)
        self.stopButton.setObjectName(u"stopButton")
        self.stopButton.setMinimumSize(QSize(80, 30))

        self.horizontalLayout.addWidget(self.stopButton)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_3)

        self.saveButton = QPushButton(self.centralwidget)
        self.saveButton.setObjectName(u"saveButton")
        self.saveButton.setMinimumSize(QSize(80, 30))

        self.horizontalLayout.addWidget(self.saveButton)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.closeButton = QPushButton(self.centralwidget)
        self.closeButton.setObjectName(u"closeButton")
        self.closeButton.setMinimumSize(QSize(80, 30))

        self.horizontalLayout.addWidget(self.closeButton)


        self.verticalLayout.addLayout(self.horizontalLayout)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 502, 22))
        self.menuFaile = QMenu(self.menubar)
        self.menuFaile.setObjectName(u"menuFaile")
        self.menuEdit = QMenu(self.menubar)
        self.menuEdit.setObjectName(u"menuEdit")
        MainWindow.setMenuBar(self.menubar)

        self.menubar.addAction(self.menuFaile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menuFaile.addAction(self.actionNew)
        self.menuFaile.addAction(self.actionOpen)
        self.menuFaile.addAction(self.actionOpwn_MIDI)
        self.menuFaile.addSeparator()
        self.menuFaile.addAction(self.actionSave)
        self.menuFaile.addAction(self.actionSave_As)
        self.menuFaile.addSeparator()
        self.menuFaile.addAction(self.actionExit)
        self.menuEdit.addAction(self.actionUndo)
        self.menuEdit.addAction(self.actionRedo)
        self.menuEdit.addSeparator()
        self.menuEdit.addAction(self.actionEdit)
        self.menuEdit.addSeparator()
        self.menuEdit.addAction(self.actionCopy)
        self.menuEdit.addAction(self.actionPaste)
        self.menuEdit.addSeparator()
        self.menuEdit.addAction(self.actionIncrement)
        self.menuEdit.addAction(self.actionIncrementPlus)
        self.menuEdit.addAction(self.actionDecrement)
        self.menuEdit.addAction(self.actionDecrementPlus)
        self.menuEdit.addSeparator()
        self.menuEdit.addAction(self.actionAdd)
        self.menuEdit.addAction(self.actionDelete)
        self.menuEdit.addSeparator()
        self.menuEdit.addAction(self.actionUp)
        self.menuEdit.addAction(self.actionDown)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionNew.setText(QCoreApplication.translate("MainWindow", u"New", None))
#if QT_CONFIG(shortcut)
        self.actionNew.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+N", None))
#endif // QT_CONFIG(shortcut)
        self.actionOpen.setText(QCoreApplication.translate("MainWindow", u"Open", None))
#if QT_CONFIG(shortcut)
        self.actionOpen.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+O", None))
#endif // QT_CONFIG(shortcut)
        self.actionSave.setText(QCoreApplication.translate("MainWindow", u"Save", None))
#if QT_CONFIG(shortcut)
        self.actionSave.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+S", None))
#endif // QT_CONFIG(shortcut)
        self.actionCopy.setText(QCoreApplication.translate("MainWindow", u"Copy", None))
#if QT_CONFIG(shortcut)
        self.actionCopy.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+C", None))
#endif // QT_CONFIG(shortcut)
        self.actionPaste.setText(QCoreApplication.translate("MainWindow", u"Paste", None))
#if QT_CONFIG(shortcut)
        self.actionPaste.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+V", None))
#endif // QT_CONFIG(shortcut)
        self.actionPlay.setText(QCoreApplication.translate("MainWindow", u"Play", None))
#if QT_CONFIG(shortcut)
        self.actionPlay.setShortcut(QCoreApplication.translate("MainWindow", u"Space", None))
#endif // QT_CONFIG(shortcut)
        self.actionWav_Save.setText(QCoreApplication.translate("MainWindow", u"Wav Save", None))
#if QT_CONFIG(shortcut)
        self.actionWav_Save.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+E", None))
#endif // QT_CONFIG(shortcut)
        self.actionExit.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
#if QT_CONFIG(shortcut)
        self.actionExit.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+Q", None))
#endif // QT_CONFIG(shortcut)
        self.actionDelete.setText(QCoreApplication.translate("MainWindow", u"Delete", None))
#if QT_CONFIG(shortcut)
        self.actionDelete.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+Del", None))
#endif // QT_CONFIG(shortcut)
        self.actionUp.setText(QCoreApplication.translate("MainWindow", u"Up", None))
#if QT_CONFIG(shortcut)
        self.actionUp.setShortcut(QCoreApplication.translate("MainWindow", u"Alt+Up", None))
#endif // QT_CONFIG(shortcut)
        self.actionDown.setText(QCoreApplication.translate("MainWindow", u"Down", None))
#if QT_CONFIG(shortcut)
        self.actionDown.setShortcut(QCoreApplication.translate("MainWindow", u"Alt+Down", None))
#endif // QT_CONFIG(shortcut)
        self.actionAdd.setText(QCoreApplication.translate("MainWindow", u"Add", None))
#if QT_CONFIG(shortcut)
        self.actionAdd.setShortcut(QCoreApplication.translate("MainWindow", u"Shift+Return", None))
#endif // QT_CONFIG(shortcut)
        self.actionEdit.setText(QCoreApplication.translate("MainWindow", u"Edit", None))
#if QT_CONFIG(shortcut)
        self.actionEdit.setShortcut(QCoreApplication.translate("MainWindow", u"I", None))
#endif // QT_CONFIG(shortcut)
        self.actionSave_As.setText(QCoreApplication.translate("MainWindow", u"Save As", None))
#if QT_CONFIG(shortcut)
        self.actionSave_As.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+Shift+S", None))
#endif // QT_CONFIG(shortcut)
        self.actionClear.setText(QCoreApplication.translate("MainWindow", u"Clear", None))
#if QT_CONFIG(shortcut)
        self.actionClear.setShortcut(QCoreApplication.translate("MainWindow", u"Del", None))
#endif // QT_CONFIG(shortcut)
        self.actionImport_From_Clipboard.setText(QCoreApplication.translate("MainWindow", u"Import From Clipboard", None))
#if QT_CONFIG(shortcut)
        self.actionImport_From_Clipboard.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+Shift+V", None))
#endif // QT_CONFIG(shortcut)
        self.actionUndo.setText(QCoreApplication.translate("MainWindow", u"Undo", None))
#if QT_CONFIG(shortcut)
        self.actionUndo.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+Z", None))
#endif // QT_CONFIG(shortcut)
        self.actionRedo.setText(QCoreApplication.translate("MainWindow", u"Redo", None))
#if QT_CONFIG(shortcut)
        self.actionRedo.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+Shift+Z", None))
#endif // QT_CONFIG(shortcut)
        self.actionDecrement.setText(QCoreApplication.translate("MainWindow", u"-", None))
#if QT_CONFIG(shortcut)
        self.actionDecrement.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+Down", None))
#endif // QT_CONFIG(shortcut)
        self.actionIncrement.setText(QCoreApplication.translate("MainWindow", u"+", None))
#if QT_CONFIG(shortcut)
        self.actionIncrement.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+Up", None))
#endif // QT_CONFIG(shortcut)
        self.actionIncrementPlus.setText(QCoreApplication.translate("MainWindow", u"++", None))
#if QT_CONFIG(shortcut)
        self.actionIncrementPlus.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+Shift+Up", None))
#endif // QT_CONFIG(shortcut)
        self.actionDecrementPlus.setText(QCoreApplication.translate("MainWindow", u"--", None))
#if QT_CONFIG(shortcut)
        self.actionDecrementPlus.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+Shift+Down", None))
#endif // QT_CONFIG(shortcut)
        self.actionOpwn_MIDI.setText(QCoreApplication.translate("MainWindow", u"Opwn MIDI", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Speakers:", None))
        self.getSpeakerButton.setText(QCoreApplication.translate("MainWindow", u"Get", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Tempo:", None))
        self.playButton.setText(QCoreApplication.translate("MainWindow", u"Play", None))
        self.playPhraseButton.setText(QCoreApplication.translate("MainWindow", u"Play Phrase", None))
        self.stopButton.setText(QCoreApplication.translate("MainWindow", u"Stop", None))
        self.saveButton.setText(QCoreApplication.translate("MainWindow", u"Wav Save", None))
        self.closeButton.setText(QCoreApplication.translate("MainWindow", u"close", None))
        self.menuFaile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuEdit.setTitle(QCoreApplication.translate("MainWindow", u"Edit", None))
    # retranslateUi

