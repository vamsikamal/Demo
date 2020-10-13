import pyodbc
conn = pyodbc.connect('Driver={SQL Server Native Client 11.0};Server=DESKTOP-JPG196B\\SQLEXPRESS;Database=dbRohit;Trusted_Connection=yes;')

cursor = conn.cursor()
sql_command = """
CREATE TABLE employee ( 
staff_number INTEGER PRIMARY KEY, 
fname VARCHAR(20), 
lname VARCHAR(30), 
gender CHAR(1), 
joining DATE,
birth_date DATE);"""

cursor.execute(sql_command)

sql_command = """INSERT INTO employee (staff_number, fname, lname, gender, birth_date)
    VALUES (1, 'William', 'Shakespeare', 'm', '1961-10-25');"""

sql_command = """INSERT INTO employee (staff_number, fname, lname, gender, birth_date)
    VALUES (1, 'William', 'Shakespeare', 'm', '1961-10-25');"""
cursor.execute(sql_command)



# never forget this, if you want the changes to be saved:
conn.commit()
conn.close()