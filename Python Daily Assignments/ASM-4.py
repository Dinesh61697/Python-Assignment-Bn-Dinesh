"""5 x 1 = 5
5 x 2 = 10
5 x 3 = 15
...
5 x 10 = 50
1.
n=5
for i in range(n,n+1):
    for j in range(1,11):
        print(i,"*",j,"=",i*j)


#2.1 2 4 5 7 8 10 11 13 14 16 17 19 20

for i in range(1,21):
    if i%3 !=0:
        print(i,end="")
        

3.1
1 2
1 2 3
1 2 3 4
1 2 3 4 5
for i in range(1,6):
    for j in range(1,i+1):
        print(j,end=" ")
    print("\n")    

4.
1 2 3 4 5
1 2 3 4
1 2 3
1 2
1

for i in range(6,0,-1):
    for j in range(1,i):
        print(j,end=" ")
    print("\n")   
"""
