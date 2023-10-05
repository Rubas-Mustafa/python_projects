# a dictionary thatb stores q and a 
# variable to store players score
# loop through the dictionary using the key values pairs 
# display each question and answer
# tell them if they are wrong or right
# show the final result when quiz is completed

quiz = {
    "question1" : {
        "question" : "How many Chambers of Heart are there? ",
        "answer" : "4"
    }, 
    "question22" : {
        "question" : "How many Chambers of Heart are there? ",
        "answer" : "4"
    }, 
    "question3" : {
        "question" : "How many Chambers of Heart are there? ",
        "answer" : "4"
    }, 
    "question4" : {
        "question" : "How many Chambers of Heart are there? ",
        "answer" : "4"
    }, 
    "question5" : {
        "question" : "How many Chambers of Heart are there? ",
        "answer" : "4"
    }, 
"question6" : {
        "question" : "How many Chambers of Heart are there? ",
        "answer" : "4"
    }
}

score = 0
for key, value in quiz.items():
    print(value["question"])
    answer = input("Answer: ")

    if answer.lower() == value["answer"].lower():
        print("Correct")
        score = score + 1
        print("Your score is" + str(score))

    else:
        print("Wrong")
        print("The answer is " + value["answer"])
        print("Your score is " + str(score))

print("Your score is " + str(score) + " out of 6")
print("Percentage is " + str(score/6 * 7) + "% ")