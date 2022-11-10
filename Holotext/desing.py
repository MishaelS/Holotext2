# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'form.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(512, 512)
        MainWindow.setMinimumSize(QtCore.QSize(512, 512))
        MainWindow.setMaximumSize(QtCore.QSize(512, 512))
        
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../image/icon_diamond.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(20, 20, 471, 451))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        
        self.txtEditField = QtWidgets.QTextEdit(self.gridLayoutWidget)
        self.txtEditField.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.txtEditField.setObjectName("txtEditField")
        self.gridLayout.addWidget(self.txtEditField, 3, 0, 1, 1)
        
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        
        self.btnVoiceInput = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btnVoiceInput.setMinimumSize(QtCore.QSize(0, 0))
        self.btnVoiceInput.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("image/icon_record.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnVoiceInput.setIcon(icon1)
        self.btnVoiceInput.setObjectName("btnVoiceInput")
        self.horizontalLayout.addWidget(self.btnVoiceInput)
        
        self.btnVocalize = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btnVocalize.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("image/icon_volume.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnVocalize.setIcon(icon2)
        self.btnVocalize.setObjectName("btnVocalize")
        self.horizontalLayout.addWidget(self.btnVocalize)
        
        self.btnClear = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btnClear.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("image/icon_trash.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnClear.setIcon(icon3)
        self.btnClear.setObjectName("btnClear")
        self.horizontalLayout.addWidget(self.btnClear)
        
        self.btnCopy = QtWidgets.QPushButton(self.gridLayoutWidget)
        
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("image/icon_copy.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnCopy.setIcon(icon4)
        self.btnCopy.setObjectName("btnCopy")
        self.horizontalLayout.addWidget(self.btnCopy)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        
        self.lblName = QtWidgets.QLabel(self.gridLayoutWidget)
        self.lblName.setObjectName("lblName")
        self.gridLayout.addWidget(self.lblName, 2, 0, 1, 1)
        
        self.line_1 = QtWidgets.QFrame(self.gridLayoutWidget)
        self.line_1.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_1.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_1.setObjectName("line_1")
        self.gridLayout.addWidget(self.line_1, 1, 0, 1, 1)
        
        self.playSlider = QtWidgets.QSlider(self.gridLayoutWidget)
        self.playSlider.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.playSlider.setOrientation(QtCore.Qt.Horizontal)
        self.playSlider.setObjectName("playSlider")
        self.gridLayout.addWidget(self.playSlider, 5, 0, 1, 1)
        
        self.line_2 = QtWidgets.QFrame(self.gridLayoutWidget)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.gridLayout.addWidget(self.line_2, 4, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 512, 20))
        self.menubar.setObjectName("menubar")
        
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        MainWindow.setMenuBar(self.menubar)
        
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setCheckable(False)
        
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("image/icon_open.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionOpen.setIcon(icon5)
        self.actionOpen.setObjectName("actionOpen")
        
        self.actionSave = QtWidgets.QAction(MainWindow)
        
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("image/icon_save.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSave.setIcon(icon6)
        self.actionSave.setObjectName("actionSave")
        
        self.actionSaveAs = QtWidgets.QAction(MainWindow)
        self.actionSaveAs.setObjectName("actionSaveAs")
        
        self.actionToClose = QtWidgets.QAction(MainWindow)
        self.actionToClose.setObjectName("actionToClose")
        
        self.actionExit = QtWidgets.QAction(MainWindow)
        
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("image/icon_exit.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionExit.setIcon(icon7)
        self.actionExit.setObjectName("actionExit")
        
        self.actionClear = QtWidgets.QAction(MainWindow)
        self.actionClear.setIcon(icon3)
        self.actionClear.setObjectName("actionClear")
        
        self.actionVocalize = QtWidgets.QAction(MainWindow)
        self.actionVocalize.setIcon(icon2)
        self.actionVocalize.setObjectName("actionVocalize")
        
        self.actionVoiceInput = QtWidgets.QAction(MainWindow)
        self.actionVoiceInput.setIcon(icon1)
        self.actionVoiceInput.setObjectName("actionVoiceInput")
        
        self.actionCopy = QtWidgets.QAction(MainWindow)
        self.actionCopy.setIcon(icon4)
        self.actionCopy.setObjectName("actionCopy")
        
        self.action123 = QtWidgets.QAction(MainWindow)
        self.action123.setObjectName("action123")
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionSaveAs)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionToClose)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.menu.addAction(self.actionVoiceInput)
        self.menu.addAction(self.actionVocalize)
        self.menu.addAction(self.actionClear)
        self.menu.addAction(self.actionCopy)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btnVoiceInput.setText(_translate("MainWindow", "Голосовой ввод"))
        self.btnVocalize.setText(_translate("MainWindow", "Озвучить"))
        self.btnClear.setText(_translate("MainWindow", "Очистить"))
        self.btnCopy.setText(_translate("MainWindow", "Копировать"))
        self.lblName.setText(_translate("MainWindow", "Ввод/Вывод"))
        self.menuFile.setTitle(_translate("MainWindow", "Файл"))
        self.menu.setTitle(_translate("MainWindow", "Редактировать"))
        self.actionOpen.setText(_translate("MainWindow", "Открыть..."))
        self.actionSave.setText(_translate("MainWindow", "Сохранить"))
        self.actionSaveAs.setText(_translate("MainWindow", "Сохранить как..."))
        self.actionToClose.setText(_translate("MainWindow", "Закрыть"))
        self.actionExit.setText(_translate("MainWindow", "Выход"))
        self.actionClear.setText(_translate("MainWindow", "Очистить"))
        self.actionVocalize.setText(_translate("MainWindow", "Озвучить"))
        self.actionVoiceInput.setText(_translate("MainWindow", "Голосовой ввод"))
        self.actionCopy.setText(_translate("MainWindow", "Копировать"))
        self.action123.setText(_translate("MainWindow", "123"))

