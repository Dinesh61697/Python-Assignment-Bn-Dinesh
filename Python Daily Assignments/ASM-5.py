#Question no:1

for i in range(3):
    if i == 0:
        print("        *")
    elif i == 1:
        print("    *       *")
    else:
        print("*       *       *")


#Question no:2
        
stars = [1, 2, 3, 2, 1]

for i in stars:
    spaces = (3 - i) * 4   # calculate left spaces
    print(" " * spaces, end="")

    for j in range(i):
        print("*", end="")
        if j < i - 1:
            print("       ", end="")  # space between stars

    print(
