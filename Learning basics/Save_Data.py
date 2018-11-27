#Dictionares
num = {
    1: "one",
    2: "two",
    3: "three",
    "sheep": True
    
}
#print (1 in num)

#print(num[1])

# how to get value from object 2 methods
print(num["sheep"])
print(num.get("sheep"))

# get value and return something else than False
print(num.get("elephant","I don't see animal"))



#Tuples -> array but const, we cannot change the values, quicker than lists () > []
word = ("spam","eggs","sausages")

print(word[0])

""" Error - > -> object does not support item assigment """
 #word[1] = "cheese" 

 # the fastest way to create a tuples
my_tuple = "one","two", "three"

print(my_tuple[0])

