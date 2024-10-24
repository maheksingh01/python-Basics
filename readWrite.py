file = open('text.txt')

# Read all the contents of file 
# Read n number of characters by passing parameter
# print(file.read(2))


# Read one single line at a time readLine()
# print(file.readline())
# print(file.readline())

# Print line by line using readline method
# line = file.readline()
# while line!="":
#     print(line)
#     line = file.readline()

# values = [ant, bag, cat, dog, egg]

# using for loop
for line in file.readlines():
    print(line)

file.close()