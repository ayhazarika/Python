"""HEADER
Name: Ayan
Date: 5/21/2020
Program: Multiple Choice Quiz
Description: This program will present a quiz about the NBA for the user, and
will output the final mark that they recieved, alongside which specific questions
the user got correct and incorrect
"""

#Variable Initialization
questionsList = []
allAnswersList = []
correctAnswersList = []

cont = ""
userAnswer = ""

#Setting up the lists of questions, their answers, and the correct answers
questionsList = ["Which NBA (National Basketball Association) team won the NBA Championship in the 2018-2019 Season?","Which NBA (National Basketball Association) team does Lebron James currently play for?","Which worldwide basketball icon won 6 championships with the Chicago Bulls, and is the logo of the ‘Jumpman’ Brand?","Which Los Angeles Lakers legend won 5 championships, and recently passed away in January of 2020?","What is the name of the NBA team that is located in Miami?","Which NBA Team from Dallas won the NBA Championship in 2011?"]
answersList = [" a. Toronto Raptors \n b. Los Angeles Lakers \n c. New England Patriots \n d. Golden State Warriors",
               " a. Colorado Avalanche \n b. Cleveland Cavaliers \n c. Los Angeles Clippers \n d. Los Angeles Lakers",
               " a. Michael Jackson \n b. Michael Jordan \n c. Lionel Messi \n d. Kobe Bryant",
               " a. Kobe Bryant \n b. Magic Johnson \n c. Jonathan Toews  \n d. Bill Russell",
               " a. Miami Celtics \n b. Inter Miami \n c. Miami Dolphins   \n d. Miami Heat",
               " a. Dallas Mavericks \n b. Dallas Stars \n c. Dallas Cowboys \n d. Dallas Raptors"]

correctAnswersList = ["a","d","b","a","d","a"]

#Description of Quiz to User
print("Hello and Welcome to the NBA Beginner's Quiz! \n")
print("This quiz is PURELY multiple choice and consists of 6 questions with 4 options each. You will then have to enter the assigned letter for whichever choice you believe is correct (e.g. Your Answer: a). At the end, you'll see what mark you got, and what level of NBA Fan you are (Super,Mediocre,Beginner)")
print("Best of Luck! \n\n")

#Loop that keeps running as long as the user wants to keep trying the quiz
while cont.lower() != "n":

    #Resetting Lists and Variables for the user if they deccide to try the quiz again
    listCountCorrect = 0
    percentageMark = 0

    incorrectOrCorrectList = []
    answerList = []
     
    #Loop that prints out all of the questions and asks the user for their answer
    for i in range(6):
        print(questionsList[i], "\n")
        print(answersList[i], "\n")
        userAnswer = input("Enter Your Answer Here (a,b,c or d): ")
        print()

        #Making the users input into lowercase
        lowAns = userAnswer.lower()
        
        #Validity Loop to decide if the user entered an acceptable input
        while lowAns != "a" and lowAns != "b" and lowAns != "c" and lowAns != "d":
            print("You Entered an Invalid Value...Try Again \n")
            userAnswer = input("Enter Your Answer Again Here (a,b,c or d): ")
            lowAns = userAnswer.lower()
            print()

        #Deciding if the user was correct or not, and putting "correct" or "incorrect" into the incorrectOrCorrectList
        if lowAns == correctAnswersList[i]:
            incorrectOrCorrectList.append("correct")
        else:
            incorrectOrCorrectList.append("incorrect")

    #Printing out which questions the user got correct and incorrect
    for i in range(6):
        print("Question Number",(i+1),"was")
        #Printing out whether question __ was correct or not
        print(incorrectOrCorrectList[i])
        
        #Deciding whether to show the user the correct answer or not
        if incorrectOrCorrectList[i] == "incorrect":
            print("The correct answer was",correctAnswersList[i],"\n")
        else:
            print()

    #Counting how many corrects the user got in the list, and displaying it
    listCountCorrect = incorrectOrCorrectList.count("correct")
    print("You got",listCountCorrect,"questions correct! \n")

    #Calculating the user's overall percentage that they achieved, and printing it out
    percentageMark = (listCountCorrect/6)
    print("This Makes Your Overall Percentage: ",((round(percentageMark,2))*100),"%")

    #Showing What Level of NBA Fan they are
    if listCountCorrect > 3:
        print("Wow! We're impressed")
        print("You Are a Super NBA Fan! \n")
    elif listCountCorrect > 1:
        print("Good Job! You did well")
        print("You Are a Mediocre NBA Fan! \n")
    else:
        print("A Good Starting Point For Your Future as an NBA Fan")
        print("You Are a Beginner NBA Fan! \n")

    #Asking the user if they want to try again
    print()
    cont = input("Would You Like To Try Again - Yes[y] or No[n]: ")
    print()
    
    #Validity loop to assure they entered a proper input
    while cont != "y" and cont != "n":
            print("It seems like you entered an invalid input...try again! \n")
            cont = input("Would You Like To Try Again - Yes[y] or No[n]: ")
            print()
    
#Last note to end it off for user
print()
print("Thanks for playing")

