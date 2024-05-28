import random
import string

chars=""; pwd = []; password = ""       #initializing variables 
strength = input("Select type of password:\n1. Simple\n2. Strong\n")    #taking input from user about type of password

while True:
        if (strength == "1" or strength.lower()=="simple"):     #if user chose simple password
            #error handling is user enters non-numeric value
            try:
                length = int(input("Enter length of password (minimum 5): "))
                if (length<5):      #checking length 
                    print("Please enter a number greater than 5\n")
                    continue    
            except:
                print("Please enter numeric value only!\n")
                continue

            #making a string of all the allowed characters (letters, numbers, special symbols)
            chars = string.ascii_letters + string.digits + string.punctuation 
            #choosing random character from the above list
            for i in range(length):
                pwd.append(random.choice(chars))

            random.shuffle(pwd)     #a shuffle for further security
            print(f"The generated password is:\n{password.join(pwd)}\n")    #printing the generated password
            chars = ""; pwd=[]
            break
            
        elif (strength == "2" or strength.lower()=="strong"):   #if user chose strong password option
            try:        #error handling
                length = int(input("Enter length of password (minimum 8): "))
                if (length<8):  
                    print("Please enter a number greater than 8\n")
                    continue
            except:
                print("Please enter numeric value only!\n")
                continue
            
            #making lists for the diffrent sets of characters
            l1 = string.ascii_letters
            l2 = string.digits
            l3 = string.punctuation
            mid = length//2

            #half will be letters
            for ch in range(mid):
                pwd.append(random.choice(l1))
            #other half will contain a mix of letters and special symbols
            for ch in range(length-mid):
                n = random.randint(0,1)     #for deciding between number and special characters
                if n==1: pwd.append(random.choice(l2))  
                else: pwd.append(random.choice(l3))
                random.shuffle(pwd)         #shuffling to ensure uniqueness

            print(f"The generated password is:\n{password.join(pwd)}\n")    #printing password
            pwd = []
            break

        else:       #in case user does not input a valid choice
            print("Please choose a valid choice!\n")
            strength = input("Select type of password:\n1. Simple\n2. Strong\n")
            continue


