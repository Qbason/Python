
    ##### TESTING A INDEX PROPERTY


import time


##Recursion
def FindIndex(word,letter,begin_index=0,result=[]):
    
    try:
        index = word.index(letter,begin_index)
        result.append(index)
        return FindIndex(word,letter,index+1,result)
    except Exception:
        return result

##NoRecursion
def FindIndexNew(word,letter,begin_index=0,result=[]):
    
    while(True):
        try:
            index = word.index(letter,begin_index)
            result.append(index)
            begin_index = index+1
        except Exception:
            return result


phrase = "Giraffe Academy and econdfkjlghkdsfjhgkdjsfhgk jhdfighdjkf shdnniuweyhr3i2u4kj234nj32n4238 h4328 74h "

find_e_phrase = FindIndex(phrase,"e")
find_e_phrase_New = FindIndexNew(phrase,"e")

# ##Comparing recursion vs while
# before = time.time()
# print(find_e_phrase)
# after = time.time()

# print(after - before)
# ##Time to recursion


# before = time.time()
# print(find_e_phrase_New)
# after = time.time()

# print(after - before)
# ##Time to while

#REPLACE 
print(phrase.replace("Giraffe","Owca"))





