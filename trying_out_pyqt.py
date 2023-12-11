from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(533, 384)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setStyleSheet("QWidget{\n"
                                  "background-color: rgb(190, 190, 190);\n"
                                  "}")
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setObjectName("gridLayout")
        self.textEdit = QtWidgets.QTextEdit(self.widget)
        self.textEdit.setStyleSheet("QTextEdit{\n"
                                    "background-color: black;\n"
                                    "color: rgb(0, 165, 80);\n"
                                    "}")
        self.textEdit.setObjectName("textEdit")
        self.gridLayout.addWidget(self.textEdit, 0, 0, 1, 1)
        self.frame = QtWidgets.QFrame(self.widget)
        self.frame.setStyleSheet("QPushButton {\n"
                                 "background-color: rgb(76, 187, 23);\n"
                                 "border: 2px solid black;\n"
                                 "border-radius: 3px;\n"
                                 "color: black;\n"
                                 "font: 13pt \"Avenir Next\";\n"
                                 "}\n"
                                 "QFrame {\n"
                                 "background-color: rgb(134, 134, 134);\n"
                                 "}")
        self.frame.setObjectName("frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName("verticalLayout")
        self.btn_save = QtWidgets.QPushButton(self.frame)
        self.btn_save.setObjectName("btn_save")
        self.verticalLayout.addWidget(self.btn_save)
        self.btn_clear = QtWidgets.QPushButton(self.frame)
        self.btn_clear.setStyleSheet("QFrame {\n"
                                     "    background-color: gray;    \n"
                                     "}")
        self.btn_clear.setObjectName("btn_clear")
        self.verticalLayout.addWidget(self.btn_clear)
        self.btn_close = QtWidgets.QPushButton(self.frame)
        self.btn_close.setObjectName("btn_close")
        self.verticalLayout.addWidget(self.btn_close)
        self.gridLayout.addWidget(self.frame, 0, 1, 1, 1)
        self.horizontalLayout.addWidget(self.widget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 533, 24))
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
        filename, _ = QtWidgets.QFileDialog.getSaveFileName(None, "Save File", ".", "Text Files (*.txt);;All Files (*)")
        if filename:
            with open(filename, 'w') as file:
                file.write(self.textEdit.toPlainText())

    def Close__File(self):
        app.quit()


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
