n = int(input("Enter the value of n : "))
num = 1
for i in range (0,n):
    print(" " * (n-i), end=" ")
    for j in range (0, i+1):
        print(num, end=" ")
        num+=1
    print("")