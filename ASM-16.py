import threading
import time

# Function to write student details into file
def write_student():
    with open("students.txt", "w") as f:
        roll = input("Enter Roll Number: ")
        name = input("Enter Student Name: ")
        f.write(roll + " " + name)
        print("Student data written to file")

# Function to read and display student details
def read_student():
    time.sleep(2)   # wait for writing to finish
    with open("students.txt", "r") as f:
        data = f.read()
        print("Student details from file:")
        print(data)

# Creating threads
t1 = threading.Thread(target=write_student)
t2 = threading.Thread(target=read_student)

# Starting threads
t1.start()
t2.start()

# Waiting for threads to finish
t1.join()
t2.join()

print("Program finished")
