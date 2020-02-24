import pandas as pd
import mysql.connector

#create dataframe
df = pd.read_csv("Account_Details.csv")
print(df)

insertData = df[['ACCOUNT_ID','ACCOUNT_NAME']]   [df['MODE']=='I']
print(insertData)

updateData = df[['ACCOUNT_ID','ACCOUNT_NAME']]   [df['MODE']=='U']
print(updateData)

deletesData = df[['ACCOUNT_ID','ACCOUNT_NAME']]   [df['MODE']=='D']
print(deletesData)

myconn = mysql.connector.connect(host="localhost", user = "root", passwd="root", database="test")
mycursor = myconn.cursor()

#For insertion of data
cols = "`,`".join([str(i) for i in insertData.columns.tolist()])
for i,row in insertData.iterrows():
    sql = "INSERT INTO `account_detail` (`" +cols + "`) VALUES (" + "%s,"*(len(row)-1) + "%s)"
    mycursor.execute(sql, tuple(row))

    # the connection is not autocommitted by default, so we must commit to save our changes
    myconn.commit()
