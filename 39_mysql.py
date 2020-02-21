Learn more or give us feedback
import mysql.connector

#setup connection
connection = mysql.connector.connect(host= "localhost", user = "root", password = "root", database="pythonfeb2020")
print(connection)

#setup cursor to execute queries
cursor = connection.cursor()
#cursor.execute("create database pythonfeb2020")

#cursor.execute("create table friends(name varchar(32), score int(16))")

#query = "insert into friends(name, score) values(%s, %s)"
#friendList = [("obb", 20), ("uber", 18), ("kia", 40)]

#cursor.executemany(query, friendList)

#connection.commit()
cursor.execute("select * from friends")
allfriends = cursor.fetchall()
for f in allfriends: