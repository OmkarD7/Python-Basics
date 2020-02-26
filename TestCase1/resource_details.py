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
        except:
            print("Error while inserting data into database")
        expt = mycursor.rowcount
        if expt == 0:
            raise TypeError("Invalid Data format")
    #for updating data
    for i ,row in updateData.iterrows():
        updateQuery = "UPDATE `resource_detail` SET RESOURCE_NAME = %s, TECHNOLOGY = %s, DOJ = %s WHERE RESOURCE_ID = %s"
        mycursor.execute(updateQuery, tuple(row))
        #print("Record Updated Successfully")
        expt = mycursor.rowcount
        if expt == 0:
            raise TypeError("Failed to update record") 
    #for deleting data
    for i, row in deleteData.iterrows():
        deleteQuery = "DELETE FROM `resource_detail` WHERE RESOURCE_ID = %s" 
        mycursor.execute(deleteQuery, tuple(row))
        print("Record Successfully Deleted")
    # the connection is not autocommitted by default, so we must commit to save our changes
    myconn.commit()
    
if __name__ == "__main__":
    try:
        thread1 = threading.Thread(target=data_handling, args=("Resource_Details.csv",))
        thread2 = threading.Thread(target=data_handling, args=("Resource_Details(1).csv",))
        thread3 = threading.Thread(target=data_handling, args=("Resource_Details(2).csv",))
        thread4 = threading.Thread(target=data_handling, args=("Resource_Details(3).csv",))
        thread5 = threading.Thread(target=data_handling, args=("Resource_Details(4).csv",))
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

    
