#register
# - first name, last name, password, email
# - generate user account


#login
# - account number & password

#blank operations

#initializing the system
import random


database = {} #dictionary


def init():

    
    print ("Welcome to BankZee")

   
    haveAccount = int(input("Do you have an account: 1 (yes) 2 (no) 3 (Cancel) \n"))

    if(haveAccount == 1):
        login()

    elif(haveAccount == 2):
        print(register())

    elif(haveAccount == 3):
        exit()

    else:
        print("Option selected invalid")

        init()


def login():

    print("login to your account")
        
    accountNumberFromUser = int(input("What is your account number? \n"))
    password = input("What is your password? \n")

    for accountNumber,userDetails in database.items():
            if(accountNumber == accountNumberFromUser):
                if(userDetails[3] == password):
                    bankOperation(userDetails)
                                

    print('Invalid account number or password')
    login()

        

def register():

    print("******New user? Register******")

    email = input("Email Adress \n")
    first_name = input("First Name \n")
    last_name = input("Last Name \n")
    password = input("Create Password \n")

    accountNumber = generatingAccountNumber()

    database[accountNumber] = [ first_name, last_name, email, password ]

    print("Account creation successful!")
    print(" == ==== ====== ===== ===")
    print("Your account number is: %d" % accountNumber)
    print("Remember to keep it safe")
    print(" == ==== ====== ===== === ")

    login()

def bankOperation(user):

    print("Welcome %s %s" % ( user[0], user[1] ))

    import datetime
    now = datetime.datetime.now()
    print ("Current date and time is:")
    print(now.strftime("%d-%m-%y %H:%M:%S"))
    
    selectedOption = int(input("What's your purpose? (1) deposit (2) withdrawal (3) Complaint (4) Logout (5) Exit \n"))

    if (selectedOption == 1):
        depositOperation()
    elif(selectedOption == 2):
        withdrawalOperation()
    elif(selectedOption == 3):
        comlplaintOperation()
    elif(selectedOption == 4):
        logout()
    elif(selectedOption == 5):
        exit()
    else:
        print("Invalid option selected")
        bankOperation(user)
         

def withdrawalOperation():
    withdrawal = input ("How much would you like to withdraw? \n")
    print("Please take your cash")
    logout()

def depositOperation():
    deposit = input ("How much would you like to deposit? \n")
    print("Your current account balance is:" + deposit)
    logout()

def comlplaintOperation():
    complaint = input ("What would you like to report? \n")
    print("Thank you for contacting us, we'll get back to you soon.")
    logout()

def generatingAccountNumber():

    return random.randrange(11111111111,99999999999)

def logout():
    login()
 

#### ACTUAL BANKING SYSTEM ####

init()
