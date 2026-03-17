Day-14 Assignment:

question no:1
if else:

num = int(input("enter a number: "))

if num % 2 == 0:
    print("The number is even")
else:
    print("The number is odd")


Question no:2

Match case:

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
operator = input("Enter a operator (+,-,*,/):")

match opreator:

    case "+":
        print("addition=", num1+num2)
    case"-":
        print("subraction=", num1+num2)
    case"*":
        print("Multiplication", num1+num2)
    case"/":
        print("Division", num1+num2)
  
    case _:
        print("Invalid operator")


Question no:3
while loop:

i = 1
while i <=5:
    print(i)
    i = i+1


Question no:4
for loop:

vowels = ["a", "e", "i", "o", "u"]
for v in vowels:
    print(v)


Question no:5
lists:

stores = ["Toys", "snacks","fruits", "Home acceseries"]

print("stores list:")

for s in stores:
    print(s)

Question no:6
Function with Parameter and Return Type:

def division (a, b):
    return a/b
num1 = int(input("enter number 1: "))
num2 = int(input("enter number 2: "))

result = division(num1, num2)

print("result=", result)






