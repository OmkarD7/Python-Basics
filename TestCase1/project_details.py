import pandas as pd
import mysql.connector

#create dataframe
df = pd.read_csv("Project_Details.csv")
print(df)

insertData = df[['ACCOUNT_ID','PROJECT_ID','PROJECT_NAME', 'START_DATE', 'END_DATE']]   [df['MODE']=='I']
print(insertData)

updateData = df[['PROJECT_NAME','START_DATE','END_DATE','PROJECT_ID']]   [df['MODE']=='U']
print(updateData)

deleteData = df[['PROJECT_ID']]   [df['MODE']=='D']
print(deleteData)

myconn = mysql.connector.connect(host="localhost", user = "root", passwd="root", database="test")
mycursor = myconn.cursor()

#For insertion of data
for i,row in insertData.iterrows():
    insertQuery = "INSERT INTO `project_detail` (ACCOUNT_ID, PROJECT_ID, PROJECT_NAME, START_DATE, END_DATE) VALUES (%s, %s, %s, %s, %s)"
    try: 
        mycursor.execute(insertQuery, tuple(row))
        print("Record Inserted Successfully.")
    except:
        print("Record Already Exist")
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