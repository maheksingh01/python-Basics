n = int(input("Enter the value of n : "))
alpha = 65
for i in range (0,n):
    print(" " * (n-i), end=" ")
    for j in range (0, i+1):
        print(chr(alpha), end=" ")
        alpha+=1
    print("")