"""HEADER
Name: Ayan Hazarika
Date: 6/5/2020
Program: Choose Your Own Adventure Summative Assignment
Description: This program is essentially a user-driven short "Choose Your Own
Adventure" story. Based on the user's decisions, they will be presented with
another scenario, and there are overall more than 8 possible endings to this
story.
"""

#Importing Time Module
import time

#Initializing Variables and Lists
restartOrNot = "y"
userRating = ""
userRatingOrNot = ""
decisionsList = ["a) Left     b) Right","a) Attack the wolves     b)Run away",
                 "a) Eat the berries      b) Don't eat the berries",
                 "a) Grab the stick     b) Dodge the wolf","a) Left     b) Right",
                 "a) Drink the water     b) Don't drink the water",
                 "a) Try to find food     b) Keep going"]


#Defining the function - printing decisions and asking user for answer
def decisionAndInput(x):
    print(decisionsList[x])
    print()
    userAnswer = input("Enter Your Decision Here (a or b):  ")
    return userAnswer

#while Loop that runs as long as the user keeps wanting to try the story
while restartOrNot.lower() == "y":

    #Initializing variables within the loop
    answersList = []
    userAnswer = ""
    response = ""
    userName = ""

    print()
    print("Welcome to an Escape the Forest, Choose Your Own Adventure program! You will begin this story with a situation that has several possible outcomes, and based on your choices, you will end up with a unique outcome. Feel free to try this adventure as many times as you like! Your adventure begins now...Best of luck! \n")
    userName = input("Please enter what you would like to name your character: ")
    print()
    print("Your eyes flutter open to the sounds of hooting owls amidst the midnight haze. You find yourself laying on the ground and manage to gather yourself to look around. But there’s nothing. Just the pitch black darkness of the night. You manage to stand up, but that’s when you notice your phone laying down the path, covered in dirt. You try to walk over but come to realize the migraine crushing away at your skull, and the dizzying nausea clouding your vision. But you manage to fight through the pain and pick up your phone. You begin running forward, not knowing where you’re going, but you keep pushing only to be met by a dead end. You turn around once again and you begin running, but this time to be met by two paths. Which Side Do You Pick?")
    response = decisionAndInput(0)
    
    #Validity loop to ensure the user entered a proper value 
    while response.lower() != "a" and response.lower() != "b":
        print()
        print("Invalid Value Entered")
        response = decisionAndInput(0)
            
    answersList.append(response)

    #Level 1 of if statements
    if response.lower() == "a":

        #Time Suspense
        for i in range(4):
            time.sleep(0.5)
            print(".")

        print()
        print("You choose to take the left path and you begin stumbling down the rocky trail. After a few minutes of walking you notice a sudden movement to your left. But all you’re met by is a pair of menacing red eyes staring right back at you. You look away for a second in disbelief, but when you look back the eyes are getting closer, this time revealing the toned complexion of a grey wolf. This time though, your body freezes of fear, and all you can do is stare back into the wolf's eyes. But now, two more wolves appear right beside the original. You have to make a choice now, try and attack, or run?")
        response = decisionAndInput(1)
            
        #Validity loop to ensure the user entered a proper value 
        while response.lower() != "a" and response.lower() != "b":
            print()
            print("Invalid Value Entered")
            response = decisionAndInput(1)

        answersList.append(response)

        #Level 2 of if statements
        if response.lower() == "a":

            #Time Suspense
            for i in range(4):
                time.sleep(0.5)
                print(".")
                
            print()
            print("You, for some reason, decide that you will be able to take on three vicious wolves. And so you grab the two closest heavy rocks, and somehow manage to knock two of the wolves out. But the third one begins to sprint towards you. You notice a sharp twig to the left of you but the wolf is getting quite close. Do you grab the stick and attack, or run away?")
            response = decisionAndInput(3)

            #Validity loop to ensure the user entered a proper value 
            while response.lower() != "a" and response.lower() != "b":
                print()
                print("Invalid Value Entered")
                response = decisionAndInput(3)

            answersList.append(response)

            #Level 3 (final) of if statements
            if response.lower() == "a":

                #Time Suspense
                for i in range(4):
                    time.sleep(0.5)
                    print(".")
                
                print()
                print("You quickly grab the stick and smack it on the wolf’s head, but unfortunately it doesn’t faze the wolf at all. It keeps charging towards you and plants itself on top of you. You manage to push it off for a moment, but the other two wolves wake up from their short-term coma, and now you’re surrounded from all angles. There’s no chance of escape. It seems as if the wolves have found their dinner for the night")
                print()
                print("Eeek. Not the greatest ending for", userName ,"..but you can try again! And hopefully", userName ,"survives nextime!")
            else:
                                
                #Time Suspense
                for i in range(4):
                    time.sleep(0.5)
                    print(".")
                    
                print()
                print("You decide against fighting a third wolf, and so you dodge the wolf’s attempt at jumping on you. Your dodge forced the wolf to jump straight into a tree trunk and so it becomes dizzy for a few moments, allowing you to escape. You begin sprinting with all of your might, and ages later, you eventually don’t hear the wolf anymore. You still don’t trust your hearing senses, and so you keep running until you luckily run into a neighborhood. You use all the might and power in your body to sprint into the neighborhood, and you knock on the closest door you see. A nice elderly couple welcome you at the door, and out of desperation you ask for food and immediate medical assistance. You spend the next 30 minutes on the couch until the paramedics arrive, and you’re immediately taken to the nearest local hospital due to wolf scratches")
                print()
                print("Congrats", userName ,"! You made it out of the forest without being severely injured, just a couple of wolf bites and cuts. You accomplished the task with the 3rd best outcome! Would you like to try again, and hopefully have an even better ending for", userName ,"?")
                
        #Level 2 of if statements
        else:

            #Time Suspense
            for i in range(4):
                time.sleep(0.5)
                print(".")
                
            print()
            print("You spot the three wolves and realize there’s no chance of fending them off, and that running away is your only hope. You slowly turn your torso around and immediately bolt the opposite directions. You hear the wolves also begin to take off behind you, but by weaving through the tree lines you manage to lose one of them. As you hear the footsteps quiet a bit, you begin to slow down but the growl of the two other wolves get you going again. As you keep running, you come to another partition in the road, with two trails. Do you choose to go left or right?")
            response = decisionAndInput(4)

            #Validity loop to ensure the user entered a proper value 
            while response.lower() != "a" and response.lower() != "b":
                print()
                print("Invalid Value Entered")
                response = decisionAndInput(4)

            answersList.append(response)

            #Level 3 (final) of if statements
            if response.lower() == "a":

                #Time Suspense
                for i in range(4):
                    time.sleep(0.5)
                    print(".")
                
                print()
                print("You choose to go left yet again, and you keep sprinting with the wolves close behind. As you once again weave your way through the trees, you begin to lose both the wolves. And after a few minutes of vigorous running, you finally spot a neighborhood in the near distance, with a group of people staring into the forest. You run towards them and realize they are your friends you were hanging out with before you got knocked out. They quickly come over to you and comfort you, and soon explained how you had tripped over a fallen tree trunk and knocked your head on a rock. They came back looking for you, but you were hidden by the plants, and so they waited for you at the end of the trail. They then take you back to your home, where you are welcomed by the comforting arms of your parents. You come to realize that this will be one of the most scary experiences of your life, and you’re just thankful it ended how it did.")
                print()
                print("Congrats", userName ,"! You made it out of the forest without being severely injured, just a couple of wolf bites and cuts. You accomplished the task with the 2nd best outcome! Would you like to try again, and hopefully have an even better ending for", userName ,"?")
            else:
                                
                #Time Suspense
                for i in range(4):
                    time.sleep(0.5)
                    print(".")
                    
                print()
                print("You choose to go against your instinct and sprint along the right, discreet path. You keep running and running for ages, but there seems no end to the path. The wolves are still getting closer, and soon you realize you’re running straight towards a wall. You glance around to try and find a path to escape, but all you see is the wolves getting closer. You don’t want to accept your fate, but minutes later, you’re met by a brick wall. You try to climb the wall, but you hear a gripping mouth clench upon your leg. You’re immediately pulled back and there’s no chance of escape. It seems as if the wolves have found their dinner for the night")
                print()
                print("Eeek. Not the greatest ending for", userName ,"..but you can try again! And hopefully", userName ,"survives nextime!")
                
    #Level 1 of if statements
    else:
        
        #Time Suspense
        for i in range(4):
            time.sleep(0.5)
            print(".")
                
        print()
        print("You decide to pick the right path and you begin stumbling down the trail. After a few minutes of walking, you come to realize the unbearable hunger eating away at your stomach. You look around in search of any edible objects, when out of the corner of your eye you notice a bush of purple berries. You make your way towards the berries and feel them to make sure they aren’t dangerous. You take a quick whiff of them as well, but nothing points towards them being dangerous. Do you eat them?")
        response = decisionAndInput(2)

        #Validity loop to ensure the user entered a proper value 
        while response.lower() != "a" and response.lower() != "b":
            print()
            print("Invalid Value Entered")
            response = decisionAndInput(2)

        answersList.append(response)

        #Level 2 of if statements
        if response.lower() == "a":
            
            #Time Suspense
            for i in range(4):
                time.sleep(0.5)
                print(".")
                
            print()
            print("You grab a handful of the berries and shove them out of your mouth out of hunger. But as soon as the first berry reaches your stomach, a rumbling sensation lights up your stomach. Immediately the second wave of nausea hits you, but this time worse than ever. But you keep walking, and this time you come across a murky pond. Would you like to drink the water?")
            response = decisionAndInput(5)

            #Validity loop to ensure the user entered a proper value 
            while response.lower() != "a" and response.lower() != "b":
                print()
                print("Invalid Value Entered")
                response = decisionAndInput(5)

            answersList.append(response)


            #Level 3 (final) of if statements
            if response.lower() == "a":

                #Time Suspense
                for i in range(4):
                    time.sleep(0.5)
                    print(".")
                
                print()
                print("You cup your hand and stick it into the murky pond to grab a handful of water. You quickly drink the water, and immediately you taste the grainy dirt fill your mouth. But you power through it, yet somehow it cools down both your mind and stomach. This gives you a sense of clarity and you keep running down the path until you finally notice a neighborhood in the near distance. You use all the might and power in your body to sprint into the neighborhood, and you knock on the closest door you see. A nice elderly couple welcome you at the door, and out of desperation you ask for food and immediate medical assistance. You spend the next 30 minutes on the couch until the paramedics arrive, and you’re immediately taken to the nearest local hospital")
                print()
                print("Congrats", userName ,"! You made it out of the forest without being severely injured. You accomplished the task with the 2nd best outcome! Would you like to try again, and get an even better outcome for", userName ,"?")
            else:
                
                #Time Suspense
                for i in range(4):
                    time.sleep(0.5)
                    print(".")
                    
                print()
                print("You take a quick look into the pond, but the sheer amount of dirt and grass in the water is absolutely revolting to you. And so you continue stumbling down the path, but the nausea doesn’t get any better. You try to push through the pain, but your knees buckle under your body. You try to keep your eyes open, but the sheer dizziness puts you into a state of unconsciousness… You open your eyes the next day and find yourself sitting in a white bed in a white room. You finally come to your senses, and instinctively call out for help. Immediately two figures rush through the door, who you come to figure are your parents. They immediately start telling you how a person found you on the trail this morning, and how you had been diagnosed with food poisoning from those berries")
                print()
                print("Congrats", userName ,"! You made it out of the forest without being severely injured. You do have food poisoning, but that was the 3rd best outcome. Would you like to try again, and maybe get", userName ,"a better outcome?")
                    
        #Level 2 of if statements
        else:             
            #Time Suspense
            for i in range(4):
                time.sleep(0.5)
                print(".")
                    
            print()
            print("You decide against your wit, and choose to not eat the berries. You keep stumbling along the path but the hunger keeps gnawing away at your stomach. You look into the thick forestry to the left and the path ahead. Will you choose to look for food or keep going?")
            response = decisionAndInput(6)

            #Validity loop to ensure the user entered a proper value 
            while response.lower() != "a" and response.lower() != "b":
                print()
                print("Invalid Value Entered")
                response = decisionAndInput(6)
                
            answersList.append(response)


            #Level 3 (final) of if statements
            if response.lower() == "a":
                                
                #Time Suspense
                for i in range(4):
                    time.sleep(0.5)
                    print(".")
                    
                print()
                print("You choose to attempt to satisfy your hunger, and take a sharp turn into the woods to look for food. You run for a few minutes until you notice a sudden movement to your left. But all you’re met by is a pair of menacing red eyes staring right back at you. You look away for a second in disbelief, but when you look back the eyes are getting closer, this time revealing the toned complexion of a grey wolf. This time though, your body freezes of fear, and all you can do is stare back into the wolf's eyes. But now, two more wolves appear, surrounding you from all directions. There’s no chance of escape. It seems as if the wolves have found their dinner for the night")
                print()
                print("Eeek. Not the greatest ending for", userName ,"..but you can try again! And maybe even get a better outcome for", userName ,"!")
            else:
                                
                #Time Suspense
                for i in range(4):
                    time.sleep(0.5)
                    print(".")
                    
                print()
                print("You decide to fight your temptations and keep running along the path. After a few minutes of running down the path, you finally notice a neighborhood in the near distance. You use all the might and power in your body to sprint into the neighborhood, and you knock on the closest door you see. A nice elderly couple welcome you at the door, and out of desperation you ask for food and immediate medical assistance. You spend the next 30 minutes on the couch until the paramedics arrive, and you’re immediately taken to the nearest local hospital")
                print()
                print("Congrats", userName ,"! You made it out of the forest without being severely injured. You accomplished the task with the best outcome! Would you like to try again, and maybe get an even better outcome for", userName ,"?")

    print()
    
    #Printing out the decisions the user made
    for i in range(3):
        print("The Number",i,"Choice You Made Was: ",answersList[i])

    #Ask user for input about whether they would like to try again or not
    print()
    restartOrNot = input("Would You Like To Try Again? yes[y] or no[n]: ")

    #Validity Loop to assure they entered a proper value
    while restartOrNot.lower() != "y" and restartOrNot.lower() != "n":
        print()
        print("Invalid Value Entered \n")
        restartOrNot = input("Would You Like To Try Again? yes[y] or no[n]: ")

#Asking User to Rate The Story and End Off Note
print()
userRatingOrNot = input("Would You Like To Rate Our Story out of 5 Stars? yes[y] or no[n]: ")

#Validity Loop to assure they entered a proper value
while userRatingOrNot.lower() != "y" and userRatingOrNot.lower() != "n":
    print()
    print("Invalid Value Entered \n")
    userRatingOrNot = input("Would You Like To Rate Our Story out of 5 Stars? yes[y] or no[n]: ")

#Checking whether or not the user wants to rate the story or not
if userRatingOrNot.lower() == "n":
    print()
    print("That's Alright! Thanks for playing!")
else:
    print()
    userRating = input("Enter Your Rating Out Of Five Stars Here: ")

    #Validity Loop to assure they entered a proper value
    while userRating != "0" and userRating != "1" and userRating != "2" and userRating != "3" and userRating != "4" and userRating != "5":
        print()
        print("Invalid Value Entered \n")
        userRating = input("Enter Your Rating Out Of Five Stars Here: ")
                              
    #Printing a message based on the user's rating
    if userRating == "0" or userRating == "1" or userRating == "2" :
        print()
        print("Sorry you didn't enjoy it :(  Maybe if you try again, you'll get a better ending! Thank you for the feedback and for playing!")
    elif userRating == "3" or userRating == "4":
        print()
        print("Sorry that you didn't have the best experience..But hopefully next time you enjoy it more!")
    else:
        print()
        print("Great! Thank you for the feedback, we're happy that you enjoyed it! Thanks for playing!")











        
    

    



        


