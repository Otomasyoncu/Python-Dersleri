import pyodbc

baglan = pyodbc.connect(
          r"Driver={Microsoft Access Driver (*.mdb)};"
          r"DBQ=database.tml;"
          r"PWD=12345;")
islem = baglan.cursor()
islem.execute(
               "select * from KULLANICILAR where AD='EMRE' "
               )
sonuc_tablom = islem.fetchall()

print(sonuc_tablom)
print(sonuc_tablom[0][3])




