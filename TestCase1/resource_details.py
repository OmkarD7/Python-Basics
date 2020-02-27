import pandas as pd
import mysql.connector
import threading

def data_handling(file_name):
    myconn = mysql.connector.connect(host="localhost", user = "root", passwd="root", database="test")
    mycursor = myconn.cursor()
    #create dataframe
    df = pd.read_csv(file_name)
    insertData = df[['RESOURCE_ID','PROJECT_ID','RESOURCE_NAME', 'TECHNOLOGY', 'DOJ']]   [df['MODE']=='I']
    updateData = df[['RESOURCE_NAME','TECHNOLOGY','DOJ', 'RESOURCE_ID']]   [df['MODE']=='U']
    deleteData = df[['RESOURCE_ID']]   [df['MODE']=='D']
    #For insertion of data
    for i,row in insertData.iterrows():
        insertQuery = "INSERT INTO `resource_detail` (RESOURCE_ID, PROJECT_ID, RESOURCE_NAME, TECHNOLOGY, DOJ) VALUES (%s, %s, %s, %s, %s)"
        try: 
            mycursor.execute(insertQuery, tuple(row))
            print("Record Inserted Successfully.")
        except Exception as Error:
            print("Error while inserting data:", Error)
    #for updating data
    for i ,row in updateData.iterrows():
        updateQuery = "UPDATE `resource_detail` SET RESOURCE_NAME = %s, TECHNOLOGY = %s, DOJ = %s WHERE RESOURCE_ID = %s"
        try:
            mycursor.execute(updateQuery, tuple(row))
            print("Record Updated Successfully")
        except Exception as Error:
            print("Error while updating data:"+str(Error))
    #for deleting data
    for i, row in deleteData.iterrows():
        deleteQuery = "DELETE FROM `resource_detail` WHERE RESOURCE_ID = %s" 
        mycursor.execute(deleteQuery, tuple(row))
        print("Record Successfully Deleted")
    # the connection is not autocommitted by default, so we must commit to save our changes
    myconn.commit()
    
if __name__ == "__main__":
    threads = []
    for i in range(5):
        file_name = "Resource_Details("+str(i)+").csv"
        try:
            t = threading.Thread(target=data_handling, args=(file_name,))
        except threading.ThreadError as ThreadErr:
            print("unable to start the thread as:",ThreadErr)
        threads.append(t)
        t.start()
    for thread in threads:
        thread.join()


    
