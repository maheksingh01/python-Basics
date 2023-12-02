t1 = (1,2,3,4)
t2 = (5,6,7,8)

#addition of two tuple
t3 = t1 + t2
print(t3)

#tuple unpacking
a,b,c,d = t1
print(a)
print(b)
print(c)
print(d)

#tuple slicing
str = ("Hello World")
rev = str[0:11:2]                   #[start:end:jump]
print(rev)

#finding element in tuple
fruits = ("Apple","Grapes","Mango","Orange","PineApple")
if("Apple" in fruits):                                  #if present in tuple
    print("Apple is available")
else:                                                   #if not present
    print("Apple is absent")