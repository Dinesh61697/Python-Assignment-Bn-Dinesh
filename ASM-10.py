#1.no para, no return type

def biggest_no():
    element=[100,200,300,400,550,600]
    biggest=element[0]

    for num in element:
        if num>biggest:
            biggest=num
    print("Biggest number is :",biggest)
    
biggest_no()


#2.with para , no return type

def biggest_no(elements):
    biggest= elements[0]

    for num in elements:
        if num>biggest:
            biggest= num
    print("Biggest numer is :",biggest)
    
elements=[100,2000,300,409,500]
biggest_no(elements)
    
    

#3.no para , with return type

def biggest_no():
    element=[10000,2000,3003,400,5000]
    biggest= element[0]

    for num in element:
        if num>biggest:
            biggest= num
    return biggest
result= biggest_no()
print("Biggest number is :",result)


#4.with para, with return type

def biggest_no(elements):
    biggest=elements[0]

    for num in elements:
        if num>biggest:
            biggest= num
    return biggest

elements=[2022,2023,2024,2025,2026,2027]
result = biggest_no(elements)
print("Biggest number is :",result)
