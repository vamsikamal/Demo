import pyodbc
conn = pyodbc.connect('Driver={SQL Server Native Client 11.0};Server=DESKTOP-JPG196B\\SQLEXPRESS;Database=dbBooks;Trusted_Connection=yes;')

cursor = conn.cursor()
cursor.execute('SELECT * FROM [dbBooks].[dbo].[Book]')

for row in cursor:
    print(row)