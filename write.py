# Read the file and store all the lines in list
# Reverse the list
# Write the list back to the file

with open('text.txt', 'r') as reader:
    content = reader.readlines()        # [ant, bag, cat, dog, egg]
    reversed(content)                   # [egg, dog, cat, bag, ant]
    with open('text.txt', 'w')as writer:
        for line in reversed(content):
            writer.write(line)