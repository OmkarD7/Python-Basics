import pandas as pd
import mysql.connector
import threading
import concurrent.futures
import logging

def data_handling(file_name):
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
        except mysql.connector.Error as Err:
            print("insertion Error: ", Err)
            #print(row)
    #for updating data
    for i ,row in updateData.iterrows():
        updateQuery = "UPDATE `account_detail` SET ACCOUNT_NAME = %s WHERE ACCOUNT_ID = %s"
        try:
            mycursor.execute(updateQuery, tuple(row))
            print("Record Updated Successfully")
        except mysql.connector.Error as Err:
            print("update error: ", Err) 
            #print(row)
    #for deleting data
    for i, row in deleteData.iterrows():
        deleteQuery = "DELETE FROM `account_detail` WHERE ACCOUNT_ID = %s"
        try:
            mycursor.execute(deleteQuery, tuple(row))
            print("Record deleted")
        except mysql.connector.Error as Err:
            print("deletation error: ", Err)
            #print(row)
    # the connection is not autocommitted by default, so we must commit to save our changes
    myconn.commit()

if __name__ == "__main__":
    threads = []
    for i in range(5):
        file_name = "Account_Details("+str(i)+").csv"
        try:
            t = threading.Thread(target=data_handling, args=(file_name,))
        except threading.ThreadError as ThreadEr:
            print("Error: unable to start thread", ThreadEr)
        threads.append(t)
        t.start()
    for thread in threads:
        thread.join()
