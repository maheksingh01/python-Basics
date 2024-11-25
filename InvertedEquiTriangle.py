rows = int(input("Enter the number of rows: "))  
m = (2*rows)-2

#Outer for loop to handle number of rows  
for i in range(rows-1,-1,-1):  
    #Inner for loop to handle number of columns  
    #values change according to the outer loop  
        for j in range(m,0,-1):  
            print(end=" ")
        #incrementing m after each loop
        m += 1 
        for j in range(0, i+1):  
            #printing triangle pyramid using asterik
            print("*",end=" ")              
  
        #End line after each row  
        print()