###Introducing the string data type#

myString = "This is a string."
print(myString)
print(type(myString))
print(myString + " is of the data type " + str(type(myString)))

##Working with string concatenation
firstString = "water"
secondString = "fall"
thirdString = firstString + secondString
print(thirdString)

#Working with input string
name = input("what is your name? ")
print(name)

#Formating output strings
color = input("what is your favorite color? ")
animal = input("what is your favorite animal? ")
print("{}, you like a {} {}!".format(name, color, animal))