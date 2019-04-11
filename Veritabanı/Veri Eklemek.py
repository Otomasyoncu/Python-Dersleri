import pyodbc

baglan = pyodbc.connect(
          r"Driver={Microsoft Access Driver (*.mdb)};"
          r"DBQ=tuzla.ser;"
          r"PWD=12345;")
kaydet = baglan.cursor()
kaydet.execute(
               "insert into KULLANICILAR (SIFRE)"
               "values ( 'Kemal'  )"
               )
baglan.commit()
