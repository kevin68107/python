#Defining a list
myFruitList = ["apple", "banana", "cherry"]
print(myFruitList)
print(type(myFruitList))

#Accessing a list by position
print(myFruitList[0])
print(myFruitList[1])
print(myFruitList[2])

#Changing the values in a list
myFruitList[2] = "orange"
print(myFruitList)

#The tuple is like a list, but it can't be changed. 
#A data type that can't be changed after it's created is said to be immutable. 
#To define a tuple, you use parentheses instead of brackets ([]).
myFinalAnswerTuple = ("apple", "banana", "pineapple")
print(myFinalAnswerTuple)
print(type(myFinalAnswerTuple))

#Accessing a tuple by position
print(myFinalAnswerTuple[0])
print(myFinalAnswerTuple[1])
print(myFinalAnswerTuple[2])

#Defining a dictionary
myFavoriteFruitDictionary = {
    "Akua" : "apple",
    "Saanvi" : "banana",
    "Paulo" : "pineapple"
}
print(myFavoriteFruitDictionary)
print(type(myFavoriteFruitDictionary))

#Accessing a dictionary by name
print(myFavoriteFruitDictionary["Akua"])
print(myFavoriteFruitDictionary["Saanvi"])
print(myFavoriteFruitDictionary["Paulo"])