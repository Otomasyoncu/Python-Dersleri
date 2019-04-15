import sys,time,serial
from PyQt5 import QtWidgets
from PyQt5 import QtGui
app = QtWidgets.QApplication(sys.argv)

pencere = QtWidgets.QWidget()
pencere.setWindowTitle("Tuzla Mesleki ve Teknik Anadolu Lisesi")
pencere.setGeometry(400, 200, 400, 400)

etiket = QtWidgets.QLabel(pencere)
etiket.setText("Bir Butona Basmadınız")
etiket.move(100, 40)
etiket.setFont(QtGui.QFont("Times", 12, QtGui.QFont.Bold))

port = serial.Serial("COM4", baudrate=9600, timeout=2)

def serkan1():
    port.write(str.encode("A"))
    c = port.readline().decode("utf-8")
    etiket.setText(c)

buton1 = QtWidgets.QPushButton(pencere)
buton1.setText("Yak")
buton1.move(100, 80)
buton1.clicked.connect(serkan1)

def serkan2():
    port.write(str.encode("B"))
    c = port.readline().decode("utf-8")
    etiket.setText(c)

buton2 = QtWidgets.QPushButton(pencere)
buton2.setText("Söndür")
buton2.move(100, 120)
buton2.clicked.connect(serkan2)

def serkan3():
    port.write(str.encode("C"))
    c = port.readline().decode("utf-8")
    etiket.setText(c)

buton3 = QtWidgets.QPushButton(pencere)
buton3.setText("Flaşör")
buton3.move(100, 160)
buton3.clicked.connect(serkan3)

pencere.show()
sys.exit(app.exec_())