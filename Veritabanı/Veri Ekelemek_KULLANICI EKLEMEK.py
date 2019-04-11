import sys, pyodbc
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtCore import *
uygulama = QtWidgets.QApplication(sys.argv)

pencere01 = QtWidgets.QWidget()
pencere01.setWindowTitle("Kayıt Ol")
pencere01.setGeometry(400, 100, 400, 400)
pencere01.setWindowIcon(QtGui.QIcon("logo.ico"))

etiket1 = QtWidgets.QLabel(pencere01)
etiket1.setText("Username")
etiket1.move(30, 30)
etiket1.setFont(QtGui.QFont("Times", 10, QtGui.QFont.Bold))

etiket2 = QtWidgets.QLabel(pencere01)
etiket2.setText("Password")
etiket2.move(30, 60)
etiket2.setFont(QtGui.QFont("Times", 10, QtGui.QFont.Bold))

etiket3 = QtWidgets.QLabel(pencere01)
etiket3.setText("                                                  ")
etiket3.move(122, 150)
etiket3.setFont(QtGui.QFont("Times", 10, QtGui.QFont.ExtraBold))

yazi_alani1 = QtWidgets.QLineEdit(pencere01)
yazi_alani1.setText("")
yazi_alani1.move(125,27)
yazi_alani1.setEnabled(True)
yazi_alani1.setFont(QtGui.QFont("Times", 10))
yazi_alani1.setAlignment(Qt.AlignLeft)

yazi_alani2 = QtWidgets.QLineEdit(pencere01)
yazi_alani2.setText("")
yazi_alani2.move(125,57)
yazi_alani2.setEnabled(True)
yazi_alani2.setFont(QtGui.QFont("Times", 10))
yazi_alani2.setAlignment(Qt.AlignLeft)
yazi_alani2.setEchoMode(QtWidgets.QLineEdit.Password)

def serkan():
     conn = pyodbc.connect(
          r"Driver={Microsoft Access Driver (*.mdb)};"
          r"DBQ=tuzla.ser;"
          r"PWD=12345;")
     cursor = conn.cursor()
     cursor.execute(
                    "insert into KULLANICILAR (KULADI , SIFRE)"
                    "values ('" + yazi_alani1.text() + "','" + yazi_alani2.text() + "')"
                    )
     conn.commit()
     yazi_alani1.setText("")
     yazi_alani2.setText("")
     etiket3.setText("Kayıt İşlemi Tamamlandı.")

buton = QtWidgets.QPushButton(pencere01)
buton.setText("Kaydol")
buton.move(124, 97)
buton.setFixedSize(134, 30)
buton.setFont(QtGui.QFont("Times", 10, QtGui.QFont.Bold))
buton.clicked.connect(serkan)


pencere01.show()
sys.exit(uygulama.exec_())