from PyQt5 import QtCore, QtGui, QtWidgets
from DBConnection import DBConnection

class Ui_AddNominee(object):

    def addnomine(self):
        try:
            name = self.lineEdit.text()
            pname = self.lineEdit_2.text()
            database = DBConnection.getConnection()
            cursor = database.cursor()
            if name == "" or name == "null" or pname == "" or pname == "null":
                self.showMessageBox("Information", "Please fill out all fields")
            else:
                sql = "select count(*) from nominee where nominee='" + name + "'"
                cursor.execute(sql)
                res = cursor.fetchone()[0]
                if res > 0:
                    self.showMessageBox("Information", "Nominee name already exists..!")
                else:

                    query = "insert into nominee values(%s,%s)"
                    values = (name, pname)
                    cursor.execute(query, values)
                    database.commit()

                    self.showMessageBox("Information", "Nominee Added Successfully..!")
                    self.lineEdit.setText("")
                    self.lineEdit_2.setText("")



        except Exception as e:
            print(e.args[0])
            tb = sys.exc_info()[2]
            print(tb.tb_lineno)
            print(e)

    def showMessageBox(self, title, message):
        msgBox = QtWidgets.QMessageBox()
        msgBox.setIcon(QtWidgets.QMessageBox.Information)
        msgBox.setWindowTitle(title)
        msgBox.setText(message)
        msgBox.setStandardButtons(QtWidgets.QMessageBox.Ok)
        msgBox.exec_()

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(609, 503)
        Dialog.setStyleSheet("background-color: rgb(200, 129, 152);")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(230, 60, 201, 31))
        self.label.setStyleSheet("font: 75 14pt \"Vani\";")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(200, 130, 141, 41))
        self.label_2.setStyleSheet("font: 75 12pt \"Vani\";")
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(200, 160, 221, 41))
        self.lineEdit.setStyleSheet("font: 75 12pt \"Vani\";")
        self.lineEdit.setObjectName("lineEdit")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(200, 220, 151, 71))
        self.label_3.setStyleSheet("font: 75 12pt \"Vani\";")
        self.label_3.setObjectName("label_3")
        self.lineEdit_2 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(200, 270, 221, 41))
        self.lineEdit_2.setStyleSheet("font: 75 12pt \"Vani\";")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(240, 350, 131, 31))
        self.pushButton.setStyleSheet("font: 75 14pt \"Times New Roman\";\n"
"background-color: rgb(85, 170, 127);\n"
"color: rgb(255, 255, 255);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.addnomine)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Add Nominee"))
        self.label.setText(_translate("Dialog", "Adding Nominee"))
        self.label_2.setText(_translate("Dialog", "Nominee Name"))
        self.label_3.setText(_translate("Dialog", "Party Name"))
        self.pushButton.setText(_translate("Dialog", "Add "))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_AddNominee()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
