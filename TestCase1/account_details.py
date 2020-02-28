import pandas as pd
import mysql.connector
import threading
#import logging
#import concurrent.futures
from mysql.connector import errorcode
from datetime import datetime
from pandas import ExcelWriter
from pandas import ExcelFile
import numpy as np

#function for writing errornous data to file
def writeError(ErRow):
    with open ("Account_Error_File.csv", "a") as fh:
        fh.write("\n"+ErRow)

#function for multithreading
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
        currentTime = datetime.now()
        formatted_date = currentTime.strftime('%Y-%m-%d %H:%M:%S')
        
        rowList = list(row)
        rowList.append(formatted_date)
        #print(rowList)

        insertQuery = "INSERT INTO `account_detail` (ACCOUNT_ID, ACCOUNT_NAME, LAST_UPDATED) VALUES (%s, %s, %s)"

        try:
            mycursor.execute(insertQuery, rowList)
            print("Record Inserted Successfully.")
        except mysql.connector.DatabaseError as DErr:
            if errorcode.ER_DUP_ENTRY == DErr.errno:
                print("Data Already Exists ")
            else:
                print("Invalid Data: ", DErr)
                writeError(str(rowList)+", I")
                #print(rowList)
    
    #for updating data
    for i, row in updateData.iterrows():
        currentTime = datetime.now()
        formatted_date = currentTime.strftime('%Y-%m-%d %H:%M:%S')
        
        rowList = list(row)
        rowList.insert(1,formatted_date)
        #print(rowList)

        updateQuery = "UPDATE `account_detail` SET ACCOUNT_NAME = %s, LAST_UPDATED = %s WHERE ACCOUNT_ID = %s"
        
        try:
            mycursor.execute(updateQuery, rowList)
            print("Record Updated Successfully")
        except mysql.connector.IntegrityError:
            print("Foreign Key constraint failed.")
            writeError(str(rowList))
        except mysql.connector.DatabaseError as DErr:
            print("Invalid Data: ", DErr)
            writeError(str(rowList)+", U")
    
    #for deleting data
    for i, row in deleteData.iterrows():
        
        deleteQuery = "DELETE FROM `account_detail` WHERE ACCOUNT_ID = %s" 
        
        try:
            mycursor.execute(deleteQuery, tuple(row))
            print("Record Successfully Deleted")
        except mysql.connector.ProgrammingError as PErr:
            print("Error while deleting data: ", PErr)
            writeError(str(rowList)+", D")
    
    # the connection is not autocommitted by default, so we must commit to save our changes
    myconn.commit()

#main function
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
