#Day-2

#1.question

a=int(input("Enter first nubmer"))
b=int(input("Enter 2 nubmer"))
c=int(input("Enter 3 nubmer"))

if a>=b and a>=c:
    print("biggest number of",a)
elif b>=a and b>=c:
    print("biggest number of",b)
else :
    print("biggest number of",c)




#2.question

username=input("enter a username")
password=input("enter a password")
if username=="admin" and password=="pass@123":
    print("valid")
else:
    print("invalid")
