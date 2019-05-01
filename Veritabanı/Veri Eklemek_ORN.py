import sys, pyodbc
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtCore import *
uygulama = QtWidgets.QApplication(sys.argv)

pencere01 = QtWidgets.QWidget()
pencere01.setWindowTitle("Kayıt Ol")
pencere01.setGeometry(400, 100, 400, 400)
pencere01.setWindowIcon(QtGui.QIcon("logo.ico"))

etiket1 = QtWidgets.QLabel(pencere01)
etiket1.setText("Okul No")
etiket1.move(30, 30)
etiket1.setFont(QtGui.QFont("Times", 10, QtGui.QFont.Bold))

etiket2 = QtWidgets.QLabel(pencere01)
etiket2.setText("İsim")
etiket2.move(30, 60)
etiket2.setFont(QtGui.QFont("Times", 10, QtGui.QFont.Bold))

etiket3 = QtWidgets.QLabel(pencere01)
etiket3.setText("Soyisim")
etiket3.move(30, 90)
etiket3.setFont(QtGui.QFont("Times", 10, QtGui.QFont.Bold))

etiket4 = QtWidgets.QLabel(pencere01)
etiket4.setText("Sınıfı")
etiket4.move(30, 120)
etiket4.setFont(QtGui.QFont("Times", 10, QtGui.QFont.Bold))

etiket5 = QtWidgets.QLabel(pencere01)
etiket5.setText("İlgili alanları doldurun ve KAYDOL butonuna basınız")
etiket5.move(32, 220)
etiket5.setFont(QtGui.QFont("Times", 10, QtGui.QFont.ExtraBold))

ya1 = QtWidgets.QLineEdit(pencere01)
ya1.setText("")
ya1.move(125,27)
ya1.setEnabled(True)
ya1.setFont(QtGui.QFont("Times", 10))
ya1.setAlignment(Qt.AlignLeft)

ya2 = QtWidgets.QLineEdit(pencere01)
ya2.setText("")
ya2.move(125,57)
ya2.setEnabled(True)
ya2.setFont(QtGui.QFont("Times", 10))
ya2.setAlignment(Qt.AlignLeft)

ya3 = QtWidgets.QLineEdit(pencere01)
ya3.setText("")
ya3.move(125,87)
ya3.setEnabled(True)
ya3.setFont(QtGui.QFont("Times", 10))
ya3.setAlignment(Qt.AlignLeft)

ya4 = QtWidgets.QLineEdit(pencere01)
ya4.setText("")
ya4.move(125,117)
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
                    "insert into KULLANICILAR (OKUL_NO , AD , SOYAD , SINIF )"
                    "values ('" + ya1.text() + "','" + ya2.text() + "','" + ya3.text() + "','" + ya4.text() + "' )"
                    )
     baglan.commit()
     etiket5.setText("Kayıt İşlemi Tamamlandı.")

buton = QtWidgets.QPushButton(pencere01)
buton.setText("Kaydol")
buton.move(124, 157)
buton.setFixedSize(134, 30)
buton.setFont(QtGui.QFont("Times", 10, QtGui.QFont.Bold))
buton.clicked.connect(serkan)

pencere01.show()
sys.exit(uygulama.exec_())