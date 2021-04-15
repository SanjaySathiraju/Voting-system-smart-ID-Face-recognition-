from PyQt5 import QtCore, QtGui, QtWidgets
from Voter import Ui_Voter
from Admin import Ui_Admin
class Ui_Main(object):

    def adminlogin(self, event):
        try:
            self.admn = QtWidgets.QDialog()
            self.ui = Ui_Admin(self.admn)
            self.ui.setupUi(self.admn)
            self.admn.show()
        except Exception as e:
            print(e.args[0])
            tb = sys.exc_info()[2]
            print(tb.tb_lineno)
        event.accept()


    def voterlogin(self, event):
        try:
            self.voter = QtWidgets.QDialog()
            self.ui = Ui_Voter(self.voter)
            self.ui.setupUi(self.voter)
            self.voter.show()
        except Exception as e:
            print(e.args[0])
            tb = sys.exc_info()[2]
            print(tb.tb_lineno)
        event.accept()



    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(741, 491)
        Dialog.setStyleSheet("background-color: rgb(200, 52, 74);")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(40, 50, 681, 51))
        self.label.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 20pt \"Vani\";")
        self.label.setObjectName("label")
        self.voter = QtWidgets.QLabel(Dialog)
        self.voter.setGeometry(QtCore.QRect(380, 150, 271, 191))
        self.voter.setStyleSheet("image: url(../IRIS/images/userss.png);")
        self.voter.setText("")
        self.voter.setObjectName("faculty")
        self.voter.mousePressEvent = self.voterlogin
        self.admin = QtWidgets.QLabel(Dialog)
        self.admin.setGeometry(QtCore.QRect(50, 160, 251, 191))
        self.admin.setStyleSheet("image: url(../IRIS/images/user-admin-gear.png);")
        self.admin.setText("")
        self.admin.setObjectName("admin")
        self.admin.mousePressEvent = self.adminlogin
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(140, 370, 121, 31))
        self.label_2.setStyleSheet("font: 16pt \"Vani\";\n"
"color: rgb(255, 255, 255);")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(490, 360, 121, 41))
        self.label_3.setStyleSheet("font: 16pt \"Vani\";\n"
"color: rgb(255, 255, 255);")
        self.label_3.setObjectName("label_3")


        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Voting System by Sanjay"))
        self.label.setText(_translate("Dialog", "Voting System Using Iris"))
        self.label_2.setText(_translate("Dialog", "Admin"))
        self.label_3.setText(_translate("Dialog", "Voters"))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Main()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
