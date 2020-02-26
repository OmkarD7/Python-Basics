import pandas as pd
import mysql.connector
import threading

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
        insertQuery = "INSERT INTO `project_detail` (ACCOUNT_ID, PROJECT_ID, PROJECT_NAME, START_DATE, END_DATE) VALUES (%s, %s, %s, %s, %s)"
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
        updateQuery = "UPDATE `project_detail` SET PROJECT_NAME = %s, START_DATE = %s, END_DATE = %s WHERE PROJECT_ID = %s"
        mycursor.execute(updateQuery, tuple(row))
        #print("Record Updated Successfully")
        expt = mycursor.rowcount
        if expt == 0:
            raise TypeError("Failed to update record") 
    #for deleting data
    for i, row in deleteData.iterrows():
        deleteQuery = "DELETE FROM `project_detail` WHERE PROJECT_ID = %s" 
        mycursor.execute(deleteQuery, tuple(row))
        print("Record Successfully Deleted")
    # the connection is not autocommitted by default, so we must commit to save our changes
    myconn.commit()
    
if __name__ == "__main__":
    try:
        thread1 = threading.Thread(target=data_handling, args=("Project_Details.csv",))
        thread2 = threading.Thread(target=data_handling, args=("Project_Details(1).csv",))
        thread3 = threading.Thread(target=data_handling, args=("Project_Details(2).csv",))
        thread4 = threading.Thread(target=data_handling, args=("Project_Details(3).csv",))
        thread5 = threading.Thread(target=data_handling, args=("Project_Details(4).csv",))
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

    
