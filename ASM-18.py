#Update query

import mysql.connector

conn = mysql.connector.connect(host ="localhost", database ="mydb",user="root", password="Dinesh@123")

cursor = conn.cursor()


uid = int(input("Enter user id to update :"))
new_name =input("Enter new username :")

query ="update userlogin set username=%s where userid=%s;"

values=(new_name, uid)

cursor.execute(query, values)

conn.commit()

print("Recor updated successfully!")



#Search query


import mysql.connector

conn = mysql.connector.connect(host="localhost", database ="mydb", user="root", password="Dinesh@123")

cursor= conn.cursor()

uid =int(input("Enter user id to search :"))

query ="select * from userlogin where userid=%s;"

values=(uid,)

cursor.execute(query , values)

result= cursor.fetchall()

if result:
    for row in result:
        print("User ID :",row[0])
        print("User name :",row[1])
        print("User password :",row[2])
else:
    print("No record found")
