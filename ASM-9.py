##1.no parameter,no return type:

def total_price():
    price = float(input("enter product price:"))
    quantity = int(input("enter quantity:"))
    total = price*quantity
    print("total price=",total)


total_price()

##2.with para,no return type:

def total_price(price, quantity):
    total = price * quantity
    print("total price=",total)

price = float(input("enter the produt price:"))
quantity = int(input("enter the quantity:"))

total_price(price,quantity)
    

##3.no para,with return type:


def total_price():
    price = float(input("enter the product price:"))
    quantity = int(input("enter the quantity:"))
    return price*quantity

result = total_price()
print("total price",result)


##4.with para,with return type:

def total_price(price, quantity):
    return price * quantity

price = float(input("enter the product price: "))
quantity = int(input("enter the quantity: "))

result = total_price(price, quantity)
print("total price =", result)


    

