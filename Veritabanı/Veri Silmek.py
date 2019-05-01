import pyodbc

baglan = pyodbc.connect(
          r"Driver={Microsoft Access Driver (*.mdb)};"
          r"DBQ=database.tml;"
          r"PWD=12345;")
islem = baglan.cursor()
islem.execute(
               "delete from KULLANICILAR where AD='EREN' "
             )
baglan.commit()