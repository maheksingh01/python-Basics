price = int(input("Enter the Amount : "))

# Amount Less Than 5000
if(price <= 5000):
    print("No Discount")

# Amount Less Than 10000 But Greater Than 5000
elif(price > 5000 and price <=10000):
    print("You are eligible for 10% discount")
    discount = float(price * 0.10)
    print("Your Discount Amount Is : ", discount)
    new_price = float(price - discount)
    print("Your Final Bill Amount Is After Discount : ", new_price)
    
# Amount Less Than 15000 But Greater Than 10000
elif(price > 10000 and price <=15000):
    print("You are eligible for 15% discount")
    discount = float(price * 0.15)
    print("Your Discount Amount Is : ", discount)
    new_price = float(price - discount)
    print("Your Final Bill Amount Is After Discount : ", new_price)
    
# Amount Less Than 20000 But Greater Than 15000
elif(price > 15000 and price <=20000):
    print("You are eligible for 20% discount")
    discount = float(price * 0.20)
    print("Your Discount Amount Is : ", discount)
    new_price = float(price - discount)
    print("Your Final Bill Amount Is After Discount : ", new_price)

# Amount Greater Than 20000
elif(price > 20000):
    print("You are eligible for 25% discount")
    discount = float(price * 0.25)
    print("Your Discount Amount Is : ", discount)
    new_price = float(price - discount)
    print("Your Final Bill Amount Is After Discount : ", new_price)