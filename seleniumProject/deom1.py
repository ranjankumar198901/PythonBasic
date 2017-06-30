

    # print in consol
#print("hello world")

    # to use help in python
#from builtins import int
#help(int)

    # swap two  VARIABLE

#x=10
#y=20
#x,y= y,x 
#print(x,y)

    # input value from console
#name = input("Enter the name ")
#print(name)

#age = input("Enter your Age")
#print(age)
#print(type(age))

#print(type(int(age)))

    # Example of Import 
#import math
#print(math.pi)    # 3.141592653589793

    #string
#name1 = str()
#print(name)

#s1="welcome"
#s2="welcome"

#print(id(s1))
#print(id(s2))

#s1+= " Mike"
#print(s1)
#print(id(s1))

    #To access characters in string

#n1= "Ranjan"
#print(n1[2])

# + is used for concatenation operation and * is repetition
s= "Tom and " + "Jerry"
print(s) 

s1 = "this is bad spam " * 3
print(s1) 

str1 = "welcome"
print(str1[1:3])

print(str1[:6])

print(str1[4:])

print(str1[1:-1])

print(str1[1:-3])

ch ="b"
print(ord(ch))

print(chr(97))

b = "Hello"
print(len(b))

print(max("abc"))
print(min("abc"))

print(max("123"))
print(min("123"))

s1 = "welcome"
print("come" in s1)

print("come" not in s1)


    # String comparison
print("tim" == "tie")
print("free" != "Freedom")
print("arrow" > "aron")
print("right" >= "left")
print("teeth" < "tee")
print("yellow" <= "fellow")
print("abc" > "")

s="hello"
for i in s:
    print(i,end="")  # this will not go to new line instead it will give a ""(no space blank in between two character 

s="hello"
for i in s:
    print(i,end="f") #after  each character it will type f 
    
# check if is alphanumric
a = "welcome to python"
print()
print(a.isalnum())

b = "as76df9787"
print(b.isalnum())  # returns true if it contains combination of alphabet and digit 

c= "Welcome"
print(c.isalpha())
print("abc".isalpha())  # returns true if string contains only alphabet

d="2017"
print(d.isdigit())  # Returns true if string contains only digits 


e= "ranjan"
print(e.isidentifier())  # Returns true if it is a identifier 
print("ranjan is".isidentifier())  # returns false as it is not a identifier


f= "ranjDan"
print(f.islower())  # returns true if the string is in lower case 
g= "RANJAN"
print(g.isupper())  # returns true if the string is in upper case 


h = " \t"
print(h.isspace())  # returns true if it contains white space 


    # search for substring which ends with
srt1="welcome to python"
print(srt1.endswith("th"))
print(srt1.endswith("python"))
print("hi")
    # searching for sub string which starts with
print(srt1.startswith("we"))

print(srt1.count("o"))  # returns the count of the occurrence of sub string (in this case it will check for number of o present

print(srt1.find("o")) # Returns lower index where the string is found ,if not found then returns -1
print(srt1.find("z"))

print(srt1.rfind("o"))  # Returns higher index of the string to be found
#--------------------------------------------------
    # Conversion Function
    #capitalize
a= "abcdef"
print(a.capitalize())   # returns with first character capitalize
print("hi")
    #Lower
L1="This IS LOWER"
print(L1.lower())
    #upper
L2="this is lower"
print(L2.upper())
    #title    returns first character of each word in capital
print(L2.title())

    #swap case   # lower   case letter will be converted to upper and upper case letter will be converter to upper
print(L1.swapcase())  

    #Replace   Replace old with new string
print(L2.replace("this", "converted"))









