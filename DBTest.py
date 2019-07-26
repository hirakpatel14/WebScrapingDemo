import pyodbc
conn = pyodbc.connect('Driver={SQL Server};'
                      # 'Server=II31-2KQX0X2\SQLEXPRESS;'
                      'Server=II31-2KQX0X2\SQLEXPRESS;'
                      'Database=LocalDBTest;'
                      'Trusted_Connection=yes;')

cursor = conn.cursor()
cursor.execute('SELECT * FROM [tblEmployee]')

for row in cursor:
    print(row)

