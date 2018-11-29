
""" counting the amount of specific letter """

#Base
def define_variable(letters):

    
    letters_array = letters.split(" ")
    letters_object = {}

    for letter in letters_array:
        #letters_object[letter] = 0
        letters_object.update({letter: 0})

    #alphabet object
    return letters_object


# read from file
def open_file(name = "textt.txt"):

    try:

        with open(name) as f:
            content  = f.read()
        # I do not have to close file
    except FileNotFoundError:
        content = ''
        print("Error -> I cannot read file, it doesn't exist")
    finally:
        return(content)




def counting(alphabet_object,content):
#counting ...checking that the letter in text is the letter in the object
    #save information about length in dictionary
    alphabet_object['length'] = len(content)
    
    for char in content:
        for letter in alphabet_object:
            if(char == letter):
                alphabet_object[letter] +=1
                break
    return alphabet_object

#showing information


def show_information(letters_dictionary):
    
    length_content = letters_dictionary['length']

    if(length_content>0):
        for letter in letters_dictionary:
            proportion = (letters_dictionary[letter]*100/length_content)
            proportion = round(proportion,2)
            print("Letter {} is the {:.2f} % of main text".format(letter,   proportion  ))
            #{:.2f} - > in the case of problem with rounding
            #the last letter "lenght" is a control sum of content
    else:
        print("Empty content")


letters = "a ą b c ć d e ę f g h i j k l ł m n ń o ó p r s ś t u w y z ź ż A Ą B C Ć D E Ę F G H I J K L Ł M N Ń O Ó P R S Ś T U W Y Z Ź Ż"

alphabet = define_variable(letters) #declarate a dictionary of each letter and set up the default value to 0
content = open_file()               # open kontent default text.txt
counted_letters = counting(alphabet,content)    #return the dictionary, which contains a counted letters in content

show_information(counted_letters)

