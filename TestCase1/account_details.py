import pandas as pd
import mysql.connector

#create dataframe
df = pd.read_csv("Account_Details.csv")
print(df)

insertData = df[['ACCOUNT_ID','ACCOUNT_NAME']]   [df['MODE']=='I']
print(insertData)

updateData = df[['ACCOUNT_NAME','ACCOUNT_ID']]   [df['MODE']=='U']
print(updateData)

deleteData = df[['ACCOUNT_ID']]   [df['MODE']=='D']
print(deleteData)

myconn = mysql.connector.connect(host="localhost", user = "root", passwd="root", database="test")
mycursor = myconn.cursor()

#For insertion of data
for i,row in insertData.iterrows():
    insertQuery = "INSERT INTO `account_detail` (ACCOUNT_ID, ACCOUNT_NAME) VALUES (" + "%s,"*(len(row)-1) + "%s)"
    try:
        mycursor.execute(insertQuery, tuple(row))
        print("Record Inserted Successfully.")
    except:
        print("SQL insertion Error: Account already exists.")

#for updating data
for i ,row in updateData.iterrows():
    updateQuery = "UPDATE `account_detail` SET ACCOUNT_NAME = %s WHERE ACCOUNT_ID = %s"
    try:
        mycursor.execute(updateQuery, tuple(row))
        print("Record Updated Successfully")
    except:
        print("Syntax Error: ID not found.") 


#for deleting data
for i, row in deleteData.iterrows():
    deleteQuery = "DELETE FROM `account_detail` WHERE ACCOUNT_ID = %s"
    mycursor.execute(deleteQuery, tuple(row))

# the connection is not autocommitted by default, so we must commit to save our changes
myconn.commit()