# have python dict that has a key/value that represents a word and its definition 
# collect input
# check if theword is in the dict
# print the definition

#     FOR LIMITED
def main():
    word_dictionary = {
        "hi" : "a way to greet",
        "eyes" : "an organ",
        "earth" : "a planet in space"
    }

    while True:
        word = input("Enter a Word: ")
        if word == "":
            break
        if word in word_dictionary:
            print(word, ":", word_dictionary[word])
main()

#    FOR UNLIMITED
from PyDictionary import PyDictionary

dictionary = PyDictionary()

while True:
    word = input("Enter a word: ")
    if word == "":
        break
    
    print(dictionary.meaning(word))


# FOR BUNCH OF WORDS
from PyDictionary import PyDictionary

dictionary = PyDictionary("eyes", "head", "mobile")

print(dictionary.printMeanings()) #in line
print(dictionary.getMeanings())  #in library form 