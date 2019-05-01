import pyodbc

baglan = pyodbc.connect(
          r"Driver={Microsoft Access Driver (*.mdb)};"
          r"DBQ=database.tml;"
          r"PWD=12345;")
islem = baglan.cursor()
islem.execute(
               "update KULLANICILAR "
               "set AD='EREN' , SOYAD='CURE' , SINIF='12E'  where OKUL_NO='1214'"
               )
baglan.commit()