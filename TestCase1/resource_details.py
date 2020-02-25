import pandas as pd
import mysql.connector

#create dataframe
df = pd.read_csv("Resource_Details.csv")
print(df)

insertData = df[['PROJECT_ID','RESOURCE_ID','RESOURCE_NAME', 'TECHNOLOGY', 'DOJ']]   [df['MODE']=='I']
print(insertData)

updateData = df[['RESOURCE_NAME','TECHNOLOGY','DOJ','RESOURCE_ID']]   [df['MODE']=='U']
print(updateData)

deleteData = df[['RESOURCE_ID']]   [df['MODE']=='D']
print(deleteData)

myconn = mysql.connector.connect(host="localhost", user = "root", passwd="root", database="test")
mycursor = myconn.cursor()

#For insertion of data
for i,row in insertData.iterrows():
    insertQuery = "INSERT INTO `resource_detail` (PROJECT_ID, RESOURCE_ID, RESOURCE_NAME, TECHNOLOGY, DOJ) VALUES (%s, %s, %s, %s, %s)" 
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