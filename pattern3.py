n = int(input("enter the value of n : "))
num = 65

#handle rows
for i in range(0,n):
    #handle columns
    for j in range(0,i+1):
        #converting to character
        ch = chr(num)
        #printing char value
        print(ch,end=" ")
        #inserting at each column
        num+=1
    #end after each row
    print("")