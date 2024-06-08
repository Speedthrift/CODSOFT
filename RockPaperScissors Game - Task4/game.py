import random 

def show_result(outcome):       #function for displaying the user and computer choices and the result
    print(f"You chose {words[user]}, computer chose {words[comp]}.\nYou {outcome}!\n")

def disp_score():               #shows the scoreboard after every round
    print(f"---------------------------\nScoreboard\nUser: {user_score} || CPU: {comp_score}\nRounds played: {rounds}\n---------------------------\n")


options = ["r","p","s"]     #options for the computer to choose
comp_score = 0; user_score = 0; rounds=0  #variables for holding the score
resp = "y"              #variable for holding response of user, to continue the game or not
words = {"r":"Rock", "p":"Paper", "s":"Scissors"}   #for remapping the letters to respective words

print("Welcome!\n\n")

while (resp=="y"):          #main loop
    try:
        user = input("Enter choice: rock-r paper-p scissors-s ").lower()[0]     #taking user input
        print()
    except:
        print("Please enter a choice!\n")           #for handling blank input by user
        continue

    comp = random.choice(options)       #computer choice from list

    if (user==comp):        #if both chose the same option, then match is tie
        print(f"You both chose {words[user]}!\nThe match is a tie.\n")

    else:
        #user choose rock            
        if (user=="r"):     
            #rock v paper            
            if (comp=="p"):     
                show_result("lose")     #showing user and computer selected choice and results
                comp_score+=1           #updating computer score as computer win
                
            #rock v scissors
            else:               
                show_result("win")
                user_score+=1           #updating user score as user wins in this case
                

        #user choose paper        
        elif (user=="p"):   
            #paper v scissors            
            if (comp=="s"):     
                show_result("lose")
                comp_score+=1
                
            #paper v rock
            else:               
                show_result("win")
                user_score+=1
                

        #user chose scissors        
        elif (user=="s"): 

            #scissors v rock            
            if (comp=="r"):     
                show_result("lose")
                comp_score+=1
                
            #scissors v paper
            else:               
                show_result("win")
                user_score+=1
                
        #user chose something not in the list ie invalid option
        else:
            print("You did not select a valid choice! Please try again\n")
            continue

    rounds+=1   #updating round counter
    disp_score()    #displaying score
    try:
        resp = input("Do you wish to continue? (Yes-y/No-n): ").lower()[0]  #taking user input on whether to continue or not
        print()
    except:
        pass        #blank answer in above treated as user does not wish to continue

print(f"Thank you for playing!\n\nFinal score is\n---------------------------\nUser: {user_score} || CPU: {comp_score}\nRounds played: {rounds}\n---------------------------\n\n")