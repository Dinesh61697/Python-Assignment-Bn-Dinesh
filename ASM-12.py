class Student:

    def getdetails(self):
        self.name = input("Enter a name: ")
        self.dept = input("Enter a dept: ")
        self.mark = int(input("Enter a mark: "))
        self.fees = int(input("Enter a fees: "))

    def show(self):
        print(self.name, self.dept, self.mark, self.fees)


students = []

for i in range(1):
    s = Student()
    s.getdetails()
    students.append(s)

print("Student Details")

for s in students:
    s.show()
        
