from PyQt5 import QtCore, QtGui, QtWidgets
import string
import re
import sys, traceback
from DBConnection import DBConnection
import mysql.connector
class Ui_ViewVoters(object):
    def voters(self):
        try:
          database = DBConnection.getConnection()
          cursor=database.cursor()
          cursor.execute("SELECT voterid,name,iris FROM voter")
          row = cursor.fetchall()
          self.tableWidget.setRowCount(0)
          for row_number, row_data in enumerate(row):
            self.tableWidget.insertRow(row_number)
            for col_number, data in enumerate(row_data):
                self.tableWidget.setItem(row_number, col_number, QtWidgets.QTableWidgetItem(str(data)))


        except Exception as e:
               print("Error="+e.args[0])
               tb = sys.exc_info()[2]
               print(tb.tb_lineno)


    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(320, 210)
        self.tableWidget = QtWidgets.QTableWidget(Dialog)
        self.tableWidget.setGeometry(QtCore.QRect(0, 1, 421, 241))
        self.tableWidget.setRowCount(5)
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setObjectName("tableWidget")
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)

        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 0, item)
        self.tableWidget.horizontalHeader().setVisible(True)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Nominee Details"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "VoterID"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "VoterName"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "IRIS"))

        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        self.tableWidget.setSortingEnabled(__sortingEnabled)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_ViewVoters()
    ui.setupUi(Dialog)
    ui.voters()
    Dialog.show()
    sys.exit(app.exec_())

