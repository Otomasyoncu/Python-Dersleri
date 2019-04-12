import pyodbc

baglan = pyodbc.connect(
          r"Driver={Microsoft Access Driver (*.mdb)};"
          r"DBQ=veritabani.mdb;"
          r"PWD=1357;")
kaydet = baglan.cursor()
kaydet.execute(
               "insert into KULLANICILAR (KULADI , SIFRE)"
               "values ( 'serkan' , '12345'  )"
               )
baglan.commit()
