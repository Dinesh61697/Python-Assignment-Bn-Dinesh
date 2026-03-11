##1.Find the biggest number:

biggest = 0

for i in range(5):
    num = int(input("Enter a number: "))


    if num > biggest:
        biggest = num

print("biggest number is:", biggest)



##2.Factorial method:


n = int(input("Enter a number: "))
fact = 1

while n > 0:
    fact = fact*n
    n = n-1

print("Factorial is:", fact)


##3.checking a prime number:

n = int(input("enter a number: "))
for i in range(2, n):
    if n % i ==0:
        print("not a prime number")
        break
    else:
        print("prime number")

#4.Count Digits in a Number

number = int(input("Enter a number :"))

count =0
while number>0:
    number=number //10
    count=count+1
print(count)



#5.grade checker

mark = int(input("Enter a number: "))

if  mark<=100 and mark >=90:
    print("Grade A")
elif mark<90 and mark>=70:
    print("Grade B")
elif mark<=69 and mark>=50:
    print("Grade c")
elif mark<50:
    print("Fail")
else:
    print("Invalid")
    

