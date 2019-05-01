import sys, pyodbc
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtCore import *
uygulama = QtWidgets.QApplication(sys.argv)

pencere01 = QtWidgets.QWidget()
pencere01.setWindowTitle("Veri Düzenlemek")
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
etiket5.setText("Bilgileri girin ve DÜZENLE ye basınız")
etiket5.move(70, 190)
etiket5.setFont(QtGui.QFont("Times", 10, QtGui.QFont.ExtraBold))

ya1 = QtWidgets.QLineEdit(pencere01)
ya1.setText("")
ya1.setGeometry(100,30,120,25)
ya1.setEnabled(True)
ya1.setFont(QtGui.QFont("Times", 10))
ya1.setAlignment(Qt.AlignLeft)

ya2 = QtWidgets.QLineEdit(pencere01)
ya2.setText("")
ya2.setGeometry(100,60,200,25)
ya2.setEnabled(True)
ya2.setFont(QtGui.QFont("Times", 10))
ya2.setAlignment(Qt.AlignLeft)

ya3= QtWidgets.QLineEdit(pencere01)
ya3.setText("")
ya3.setGeometry(100,90,200,25)
ya3.setEnabled(True)
ya3.setFont(QtGui.QFont("Times", 10))
ya3.setAlignment(Qt.AlignLeft)

ya4 = QtWidgets.QLineEdit(pencere01)
ya4.setText("")
ya4.setGeometry(100,120,200,25)
ya4.setEnabled(True)
ya4.setFont(QtGui.QFont("Times", 10))
ya4.setAlignment(Qt.AlignLeft)

def serkan():
    baglan = pyodbc.connect(
        r"Driver={Microsoft Access Driver (*.mdb)};"
        r"DBQ=database.tml;"
        r"PWD=12345;")
    islem = baglan.cursor()
    islem.execute(
        "update KULLANICILAR "
        "set AD='"+ya2.text() + "' , SOYAD='"+ya3.text() + "' , SINIF='" + ya4.text() + "'" 
        "where OKUL_NO='" + ya1.text() + "'"
    )
    baglan.commit()
    etiket5.setText("Düzenleme İşlemi Tamamlandı.")


buton = QtWidgets.QPushButton(pencere01)
buton.setText("Düzenle")
buton.move(222, 29)
buton.setFixedSize(78, 27)
buton.setFont(QtGui.QFont("Times", 10, QtGui.QFont.Bold))
buton.clicked.connect(serkan)

pencere01.show()
sys.exit(uygulama.exec_())