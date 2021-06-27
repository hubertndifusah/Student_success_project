import pandas
import pyodbc

server = 'hypv8669.hostedbyappliedi.net'
database = 'CCP'
username = 'ColaberryDB'
password = 'Iam4Colaberry!'
cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
cursor = cnxn.cursor()
query = cursor.execute("""SELECT		b.UserID,a.*
                        FROM		[dbo].[ADF_Indigo_DISC_Student] a
                        LEFT JOIN	dnnuser.users b
                        ON			a.[In-Email] = b.Email
                        WHERE		[In-Email] IS NOT NULL
                        AND			b.UserID IS NOT NULL"""
                       )

data = query.fetchall()
print(data)