squares = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
#          0, 1, 2, 3,  4,  5,  6,  7,  8, 9
#print the range 2 - 5 but not include the index numer 5!
print(squares[2:5])
print(squares[2:3])
#it doesn't work on tuples



print(squares[:2]) # from index 0 to 1

print(squares[::2]) # show values from 0 index up to the end with a step of 2
print(squares[0::2]) # the same like below, but we can set the start index

print(squares[2:]) # from index 2nd to end
# print(squares[2::]) it doesn't have sense

print(squares[1:10:2]) # from the 1nd index up to the 8th with a step of 2 

""" It works also on string string -> array """
word = "fastest"

print(word[::2])

print(word[0:-2:1]) # cut the last two indexes

print(word[::-1]) # method to reverse array/list

print(word[4:0:-1]) # if we use the minus values as the last argument than we have to switch the first two arguments, cause we "counting" from end to start