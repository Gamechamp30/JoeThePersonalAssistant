#This script was created by Liam Quinn in Python 3.9.4
#Some of the code in this script may have been created by other programmers and/or authors

#Imports
import math
import time
import datetime
from datetime import date
import sys
#Variables

#Booleans
running = bool(True)
noValidInput = bool (True)
#Strings
action = str("null")
userName = str("null")
sqrtResult = str("null")
devPassword = str("")
password = str ("null")
todaysDate = str("null")
#Floats
number = float(0)
#Intergers
counter = int(0)
counter2 = int(0)
numberOne =  int(0)
numberTwo = int(0)
numberThree = int(0)
#Functions

#Function List
def funclist():
    print("what can i ask you (This command)")
    print("find square root")
    print("multiply")
    print("what time is it")
    print("what is the date")
    print("who made you")
    print("technical info")
    print("link to source code")

    print("exit")

#Square Root function
def squareRoot():
    number = float(input("Of what number? "))
    sqrtResult = math.sqrt(number)
    print(sqrtResult)
    print("There you go!")
    return


#Developer Panel Function
def devPanel():
    password = input("What is the developer password? ")

    if password == devPassword :
        print("Welcome to the developer panel")
                
    if password != devPassword:
        print("Incorrect Password")
    return


#Time Function
def whatTimeIsIt():
    print("The current time is:")
    print((time.strftime("%I:%M:%S")))
    return


#Date Function
def whatDayIsIt():
    todaysDate = date.today()
    print("Today's date is:", todaysDate)
    return


#Multiplication Function
def multiply():
    numberOne = int(input("What is the first number of the equation? "))
    numberTwo = int(input("What is the second number of the equation? "))
    numberThree = numberOne * numberTwo
    print("The product is:")
    print(numberThree)
    return

#Credits Function
def credits():
    print("I was made by Liam Quinn")

#More About Me Function
def techinfo():
    print("I was made by Liam Quinn in Python 3.9.4")
    moreInfo = input("Would you like to know more? (y/n) ")
    if moreInfo == "y":
        print("\nThis project was started on 11/10/21")
        print("The imports Liam used are as follows:")
        print("math")
        print("datetime")
        print("time")
        print("sys")
        print("My internal programing contains over 200 lines as of 11/12/21")
        print("I am also completly open source")
        print("You can use the 'link to source code' command to find my code")

    if moreInfo == "n":
        return

#Source Code Function


#Exit Function
def exit():
    
    areYouSure = str(input("Are you sure you want to leave? "))
    if areYouSure == "Yes":
        print("Don't Lea...")
        time.sleep(1)
        sys.exit()
    if areYouSure == "yes":
        print("Don't Lea...")
        time.sleep(1)
        sys.exit()
    if areYouSure == "y":
        print("Don't Lea...")
        time.sleep(1)
        sys.exit()
    if areYouSure == "Y":
        print("Don't Lea...")
        time.sleep(1)
        sys.exit()

    if areYouSure == "No":
        print("Returning...")
        return

    if areYouSure == "no":
        print("Returning...")
        return

    if areYouSure == "n":
        print("Returning...")
        return

    if areYouSure == "N":
        print("Returning...")
        return


#Start of script
#Saying hello and asking for the user's name
print("Hello!")
userName = input("What's your name? ")
print("Hi " + userName + ", I am Jeff, your personal assistant.") #And no, we aren't Jeff Bezos; we aren't going to steal your personal data


while running == True:

        action = input("\nYou can ask me (almost) anything: ")

        #Function List
        if action == "what can i ask you":
            funclist()
            counter = counter2 + 1

        #Square Root
        if action == "find square root":
            squareRoot()
            counter = counter2 + 1

        #Dev Panel
        if action == "opendevpanel":
            devPanel()
            counter = counter2 + 1

        #Time
        if action == "what time is it":
            whatTimeIsIt()
            counter = counter2 + 1

        if action == "multiply":
            multiply()
            counter = counter2 + 1

        #Day
        if action == "what is the date":
            whatDayIsIt()
            counter = counter2 + 1

        #Exit
        if action == "exit":
            exit()   
            counter = counter2 + 1    

        #Info
        if action == "who made you":
            credits()
            counter = counter2 + 1
        #More info
        if action == "technical info":
            techinfo()
            counter = counter2 + 1

        

        #If user input isn't valid:    
        if counter == 0:
            print("Sorry, I can't help with that")
