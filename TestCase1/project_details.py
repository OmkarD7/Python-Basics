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
        except mysql.connector.Error as Err:
            print("Error while inserting data: ", Err)
            #print(row)
    #for updating data
    for i ,row in updateData.iterrows():
        updateQuery = "UPDATE `project_detail` SET PROJECT_NAME = %s, START_DATE = %s, END_DATE = %s WHERE PROJECT_ID = %s"
        try:
            mycursor.execute(updateQuery, tuple(row))
            print("Record Updated Successfully")
        except mysql.connector.Error as Err:
            print("Error while updating data: ", Err)
            #print(row)

    #for deleting data
    for i, row in deleteData.iterrows():
        deleteQuery = "DELETE FROM `project_detail` WHERE PROJECT_ID = %s" 
        try:
            mycursor.execute(deleteQuery, tuple(row))
            print("Record Successfully Deleted")
        except mysql.connector.Error as Err:
            print("Error while deleting data: ", Err)
            #print(row)
    # the connection is not autocommitted by default, so we must commit to save our changes
    myconn.commit()
    
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

    
