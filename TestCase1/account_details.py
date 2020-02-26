import pandas as pd
import mysql.connector
import threading

def data_handling(threadName, file_name):
    #create dataframe
    df = pd.read_csv(file_name)
    insertData = df[['ACCOUNT_ID','ACCOUNT_NAME']]   [df['MODE']=='I']
    updateData = df[['ACCOUNT_NAME','ACCOUNT_ID']]   [df['MODE']=='U']
    deleteData = df[['ACCOUNT_ID']]   [df['MODE']=='D']
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


try:
    thread1 = threading.Thread(target=data_handling, args=("Thread1", "Account_Details.csv"))
    thread2 = threading.Thread(target=data_handling, args=("Thread2", "Account_Details(1).csv"))
    thread3 = threading.Thread(target=data_handling, args=("Thread2", "Account_Details(2).csv"))
    thread4 = threading.Thread(target=data_handling, args=("Thread2", "Account_Details(3).csv"))
    thread5 = threading.Thread(target=data_handling, args=("Thread2", "Account_Details(4).csv"))

except:
   print ("Error: unable to start thread")

thread1.start()
thread2.start()
thread3.start()
thread4.start()
thread5.start()

thread1.join()
thread2.join()
thread3.join()
thread4.join()
thread5.join()