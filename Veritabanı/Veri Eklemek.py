import pyodbc

baglan = pyodbc.connect(
          r"Driver={Microsoft Access Driver (*.mdb)};"
          r"DBQ=database.tml;"
          r"PWD=12345;")
islem = baglan.cursor()
islem.execute(
               "insert into KULLANICILAR (OKUL_NO , AD , SOYAD , SINIF )"
               "values ( '1238' , 'SERKAN' , 'KOSE' , '11H' )"
               )
baglan.commit()
