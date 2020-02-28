import pandas as pd
import mysql.connector
import threading
from mysql.connector import errorcode
from datetime import datetime

#function for writing errornous data to file
def writeError(ErRow):
    with open ("Project_Error_File.csv", "a") as fh:
        fh.write("\n"+ErRow)

#function for multithreading
def data_handling(file_name):
    
    myconn = mysql.connector.connect(host="localhost", user = "root", passwd="root", database="test")
    mycursor = myconn.cursor()
    
    #create dataframe
    df = pd.read_csv(file_name)
    
    insertData = df[['ACCOUNT_ID','PROJECT_ID','PROJECT_NAME', 'START_DATE', 'END_DATE']]   [df['MODE']=='I']
    updateData = df[['PROJECT_NAME','START_DATE','END_DATE','PROJECT_ID']]   [df['MODE']=='U']
    deleteData = df[['PROJECT_ID']]   [df['MODE']=='D']
    
    #For insertion of data
    for i,row in insertData.iterrows():
        
        currentTime = datetime.now()
        formatted_date = currentTime.strftime('%Y-%m-%d %H:%M:%S')
        
        rowList = list(row)
        rowList.append(formatted_date)

        insertQuery = "INSERT INTO `project_detail` (ACCOUNT_ID, PROJECT_ID, PROJECT_NAME, START_DATE, END_DATE, LAST_UPDATED) VALUES (%s, %s, %s, %s, %s, %s)"
        
        try:
            mycursor.execute(insertQuery, rowList)
            print("Record Inserted Successfully.")
        except mysql.connector.DatabaseError as DErr:
            if errorcode.ER_DUP_ENTRY == DErr.errno:
                print("Data Already Exists ")
            else:
                print("Invalid Data: ", DErr)
                writeError(str(rowList)+", I")
    
    #for updating data
    for i ,row in updateData.iterrows():
        
        currentTime = datetime.now()
        formatted_date = currentTime.strftime('%Y-%m-%d %H:%M:%S')
        
        rowList = list(row)
        rowList.insert(3,formatted_date)
        #print(rowList)

        updateQuery = "UPDATE `project_detail` SET PROJECT_NAME = %s, START_DATE = %s, END_DATE = %s, LAST_UPDATED = %s WHERE PROJECT_ID = %s"
        
        try:
            mycursor.execute(updateQuery, rowList)
            print("Record Updated Successfully")
        except mysql.connector.IntegrityError:
            print("Foreign Key constraint failed.")
            writeError(str(rowList)+", U")
        except mysql.connector.DatabaseError as DErr:
            print("Invalid Data: ", DErr)
            writeError(str(rowList)+", U")
    
    #for deleting data
    for i, row in deleteData.iterrows():
        
        deleteQuery = "DELETE FROM `project_detail` WHERE PROJECT_ID = %s" 
        
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
        file_name = "Project_Details("+str(i)+").csv"
        try:
            t = threading.Thread(target=data_handling, args=(file_name,))
        except threading.ThreadError as threadEr:
            print("Error while deleting data: ", threadEr)
        threads.append(t)
        t.start()
    
    for thread in threads:
        thread.join()

    
