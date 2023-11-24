def amount(cost, day):
    if(day == "Sunday"):
        discount = cost * 0.15
        new_amount = cost - discount
        return(new_amount)
    else:
        tax = cost * 0.15
        new_amount1 = cost + tax
        return(new_amount1)
    
#main

cost = int(input("Enter the cost : "))
day = input("Enter the day : ")
a = amount(cost,day)
print(a)