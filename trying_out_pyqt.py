from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(10, 0, 781, 561))
        self.widget.setObjectName("widget")
        self.btn_save = QtWidgets.QPushButton(self.widget)
        self.btn_save.setGeometry(QtCore.QRect(610, 40, 151, 71))
        self.btn_save.setObjectName("btn_save")
        self.btn_clear = QtWidgets.QPushButton(self.widget)
        self.btn_clear.setGeometry(QtCore.QRect(610, 130, 151, 71))
        self.btn_clear.setObjectName("btn_clear")
        self.btn_close = QtWidgets.QPushButton(self.widget)
        self.btn_close.setGeometry(QtCore.QRect(610, 230, 151, 71))
        self.btn_close.setObjectName("btn_close")
        self.textEdit = QtWidgets.QTextEdit(self.widget)
        self.textEdit.setGeometry(QtCore.QRect(20, 20, 551, 521))
        self.textEdit.setObjectName("textEdit")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.btn_save.clicked.connect(self.Save__File)
        self.btn_clear.clicked.connect(self.Clear__File)
        self.btn_close.clicked.connect(self.Close__File)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btn_save.setText(_translate("MainWindow", "Сохранить"))
        self.btn_clear.setText(_translate("MainWindow", "Очистить"))
        self.btn_close.setText(_translate("MainWindow", "Закрыть приложение"))

    def Clear__File(self):
        self.textEdit.setText("")

    def Save__File(self):
        S__File = QtWidgets.QFileDialog.getSaveFileName(None,'SaveTextFile','/')

    def Close__File(self):
        sys.exit(app.exec())

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())