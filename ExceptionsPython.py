ItemsInCart = 0

# 2 items will be added to cart

# Basic way to through exception

# if ItemsInCart != 2:
#     raise Exception("Product Cart Count Not Matching")

if ItemsInCart != 2:   # Raise Exception ("Products Cart Count Do Not Match")
    pass

assert(ItemsInCart == 0 )       # Assertion Error


# try catch with customized exception

try:
    with open('text.txt', 'r') as reader:
        reader.read()
        

except:
    print('Somehow I reached this block of code because there is failure in try block.')

# try catch with actual exception printing 

try:
    with open('fileOpen.txt', 'r') as reader:
        reader.read()
    
except Exception as e:
    print(e)   
    
    
# try catch along with finally block

try:
    with open('fileOpen.txt', 'r') as reader:
        reader.read()
    
except Exception as e:
    print(e)   
    
finally:
    print("Cleaning Up The Records")

