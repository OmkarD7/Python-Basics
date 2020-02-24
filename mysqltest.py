import mysql.connector
connection = mysql.connector.connect(host= "localhost", user = "root", password = "root", database="omkar")

myscursor = connection.cursor()
myscursor.execute("select * from test")
result = myscursor.fetchall()
for i in result:
    print(i)
