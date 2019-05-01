import sys, pyodbc
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtCore import *
uygulama = QtWidgets.QApplication(sys.argv)

pencere01 = QtWidgets.QWidget()
pencere01.setWindowTitle("Veri Okumak")
pencere01.setGeometry(400, 50, 400, 400)
pencere01.setWindowIcon(QtGui.QIcon("logo.ico"))

etiket1 = QtWidgets.QLabel(pencere01)
etiket1.setText("Okul No")
etiket1.move(20, 33)
etiket1.setFont(QtGui.QFont("Times", 10, QtGui.QFont.Bold))

etiket2 = QtWidgets.QLabel(pencere01)
etiket2.setText("İsim")
etiket2.move(20, 63)
etiket2.setFont(QtGui.QFont("Times", 10, QtGui.QFont.Bold))

etiket3 = QtWidgets.QLabel(pencere01)
etiket3.setText("Soyisim")
etiket3.move(20, 93)
etiket3.setFont(QtGui.QFont("Times", 10, QtGui.QFont.Bold))

etiket4 = QtWidgets.QLabel(pencere01)
etiket4.setText("Sınıf")
etiket4.move(20, 123)
etiket4.setFont(QtGui.QFont("Times", 10, QtGui.QFont.Bold))

etiket5 = QtWidgets.QLabel(pencere01)
etiket5.setText("OKUL NO girin ve ARA Butonuna basınız")
etiket5.move(70, 190)
etiket5.setFont(QtGui.QFont("Times", 10, QtGui.QFont.ExtraBold))

yazi_alani1 = QtWidgets.QLineEdit(pencere01)
yazi_alani1.setText("")
yazi_alani1.setGeometry(100,30,150,25)
yazi_alani1.setEnabled(True)
yazi_alani1.setFont(QtGui.QFont("Times", 10))
yazi_alani1.setAlignment(Qt.AlignLeft)

yazi_alani2 = QtWidgets.QLineEdit(pencere01)
yazi_alani2.setText("")
yazi_alani2.setGeometry(100,60,200,25)
yazi_alani2.setEnabled(True)
yazi_alani2.setFont(QtGui.QFont("Times", 10))
yazi_alani2.setAlignment(Qt.AlignLeft)

yazi_alani3= QtWidgets.QLineEdit(pencere01)
yazi_alani3.setText("")
yazi_alani3.setGeometry(100,90,200,25)
yazi_alani3.setEnabled(True)
yazi_alani3.setFont(QtGui.QFont("Times", 10))
yazi_alani3.setAlignment(Qt.AlignLeft)

yazi_alani4 = QtWidgets.QLineEdit(pencere01)
yazi_alani4.setText("")
yazi_alani4.setGeometry(100,120,200,25)
yazi_alani4.setEnabled(True)
yazi_alani4.setFont(QtGui.QFont("Times", 10))
yazi_alani4.setAlignment(Qt.AlignLeft)

def serkan():
    baglan = pyodbc.connect(
                    r"Driver={Microsoft Access Driver (*.mdb)};"
                    r"DBQ=database.tml;"
                    r"PWD=12345;"
                           )
    islem = baglan.cursor()
    islem.execute("select * from KULLANICILAR where OKUL_NO='" + yazi_alani1.text() + "'")
    sonuc_tablom = islem.fetchall()

    if(sonuc_tablom == [] ):
        etiket5.setText("Eşleşen veri yok")
    else:
        etiket5.setText(" ")
        yazi_alani2.setText(sonuc_tablom[0][2])
        yazi_alani3.setText(sonuc_tablom[0][3])
        yazi_alani4.setText(sonuc_tablom[0][4])

buton = QtWidgets.QPushButton(pencere01)
buton.setText("Ara")
buton.move(252, 29)
buton.setFixedSize(48, 27)
buton.setFont(QtGui.QFont("Times", 10, QtGui.QFont.Bold))
buton.clicked.connect(serkan)

pencere01.show()
sys.exit(uygulama.exec_())