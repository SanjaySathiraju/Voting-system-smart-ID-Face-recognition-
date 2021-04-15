

from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from DBConnection import DBConnection

class Ui_Voting(object):

    def __init__(self, dialog, vid):
        self.dialog = dialog;
        self.vid = vid

    def nominelist(self):
        try:
            database = DBConnection.getConnection()
            cursor = database.cursor()
            cursor.execute("select nominee,partyname from nominee")
            records = cursor.fetchall()
            for row in records:
                self.comboBox.addItem(str(row[0]) + "  -->  " + str(row[1]))

        except Exception as e:
            print("Error=" + e.args[0])
            tb = sys.exc_info()[2]
            print(tb.tb_lineno)

    def votingnm(self):
        database = DBConnection.getConnection()
        cursor = database.cursor()
        nmlist = self.comboBox.currentText()
        nm = nmlist.split("  -->  ")
        nominee = nm[0]
        symbol = nm[1]
        sql = "select count(*) from voting where vid='" + self.vid + "'"
        cursor.execute(sql)
        res = cursor.fetchone()[0]
        if res > 0:
            self.showMessageBox("Information", "Already Voted..!")
        else:
            try:
                vcnt = 0;
                sql = "select count(*) from voting where name='" + nominee + "'"
                cursor.execute(sql)
                res = cursor.fetchone()[0]
                if res > 0:
                    sql = "select vcnt from voting where name='" + nominee + "'"
                    cursor.execute(sql)
                    vcnt = cursor.fetchone()[0]
                    vcnt = vcnt + 1
                    sqll = "update voting set vcnt=" + str(vcnt) + " where name='" + nominee + "'"
                    cursor.execute(sqll)
                    database.commit();
                    self.showMessageBox("Information", "Voted Successfully..!")
                    self.dialog.hide()
                else:
                    vcnt = 1;
                    sql = "insert into voting values(%s,%s,%s,%s)"
                    values = (nominee, symbol, int(vcnt), self.vid)
                    cursor.execute(sql, values)
                    database.commit()
                    self.showMessageBox("Information", "Voted Successfully..!")
                    self.dialog.hide()

            except Exception as e:
                print("Error=" + e.args[0])
                tb = sys.exc_info()[2]
                print(tb.tb_lineno)

    def showMessageBox(self, title, message):
        msgBox = QtWidgets.QMessageBox()
        msgBox.setIcon(QtWidgets.QMessageBox.Information)
        msgBox.setWindowTitle(title)
        msgBox.setText(message)
        msgBox.setStandardButtons(QtWidgets.QMessageBox.Ok)
        msgBox.exec_()

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(691, 424)
        Dialog.setStyleSheet("background-color: rgb(85, 85, 255);")
        self.comboBox = QtWidgets.QComboBox(Dialog)
        self.comboBox.setGeometry(QtCore.QRect(170, 170, 181, 41))
        self.comboBox.setStyleSheet("color: rgb(0, 0, 0);\n"
"font: 75 12pt \"Verdana\";")
        self.comboBox.setObjectName("comboBox")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(170, 140, 151, 31))
        self.label.setStyleSheet("color: rgb(0, 0, 0);\n"
"font: 12pt \"Georgia\";")
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(170, 260, 181, 41))
        self.pushButton.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(170, 85, 0);\n"
"font: 14pt \"Franklin Gothic Heavy\";")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.votingnm)
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(310, 60, 201, 31))
        self.label_2.setStyleSheet("font: 18pt \"Franklin Gothic Heavy\";")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(430, 90, 221, 271))
        self.label_3.setStyleSheet("image: url(../IRIS/images/Vote.png);")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Voting"))
        self.label.setText(_translate("Dialog", "Select Nominee"))
        self.pushButton.setText(_translate("Dialog", "Vote"))
        self.label_2.setText(_translate("Dialog", "Voting"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Voting(Dialog,'1839')
    ui.setupUi(Dialog)
    Dialog.show()
    ui.nominelist()
    sys.exit(app.exec_())
