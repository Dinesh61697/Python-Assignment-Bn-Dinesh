students = [
    {"name": "Arun", "marks": [78, 82, 90]},
    {"name": "Bala", "marks": [65, 70, 60]},
    {"name": "Chitra", "marks": [88, 92, 95]}
]


# 1.calculate average for each student:


for student in students:
    Total=0
    for mark in student['marks']:
        Total = Total + mark

    average = Total / len(student['marks'])
    print(student['name'], 'average=',average)    
    


# 2.find highest average:



name = ''
highest_average = 0


for student in students:
    average = sum(student["marks"])/len(student["marks"])
    if average> highest_average:
        highest_average=average
        name = student['name']
print("highest average:", name, "=",highest_average)



#3.list student with average above 80

for student in students:
    if average>80:
        print(student['name'])




