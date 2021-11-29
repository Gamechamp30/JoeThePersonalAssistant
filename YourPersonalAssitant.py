#This script was created by Liam Quinn in Python 3.9.4
#Some of the code in this script may have been created by other programmers and/or authors

#Imports
import math
import time
import random
from datetime import date
import sys
import webbrowser
#Variables

#Booleans
running = bool(True)
noValidInput = bool (True)
#Strings
action = str("null")
devAction = str("null")
userName = str("null")
sqrtResult = str("null")
devPassword = str("")
password = str ("null")
todaysDate = str("null")
#Floats
number = float(0)
#Intergers
randomNumber = int()
counter = int(0)
counter2 = int(0)
subtractionOne = int(0)
subtractionTwo = int(0)
subtractionThree = int(0)
multiplicationOne =  int(0)
multiplicationTwo = int(0)
numberThree = int(0)
#Functions

#Function List
def funclist():
    print("what can i ask you (This command)")
    print("square root")
    print("multiply")
    print("subtract")
    print("encode")
    print("open spotify")
    print("open youtube music")
    print("open google")
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

#Subtraction Function
def subtraction():
    subtractionOne = int(input("What is the first number of the equation? "))
    subtractionTwo = int(input("What is the second number of the equation? "))
    subtractionThree = subtractionOne - subtractionTwo
    print("The difference is:")
    print(subtractionThree)


#Multiplication Function
def multiply():
    multiplicationOne = int(input("What is the first number of the equation? "))
    multiplicationTwo = int(input("What is the second number of the equation? "))
    numberThree = multiplicationOne * multiplicationTwo
    print("The product is:")
    print(numberThree)
    return

#Encoder Function
def encode():
    encode1 = str(input("What do you want me to encode? "))
    codec = str(input("What codec would you like to use? (Press enter for default and type 'codec list' for a list of codecs) "))
    encode2 = encode1.encode(encoding=codec, errors="strict")
    print(encode2)
    return

#Decoder Function
def decode():
    print("placeholder")

#Developer Panel Function
def devPanel():
    password = input("What is the developer password? ")

    if password == devPassword :
        print("Welcome to the developer panel")
                
    if password != devPassword:
        print("Incorrect Password")

    devAction = input("What do you need to do? ")

    if devAction == "debug":
        print("Starting Debugger...\n")
        time.sleep(5)
        print("No errors found, exiting")
    
    if devAction == "Clear cache": 
        print("Clearing cache...")
        print("Current cache: (0MB/250MB)")
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


#Spotify Function
def openSpotify():
    print("This feature is still under development, try 'open google'")

#Youtube Music
def openYTMusic():
    print("Opening YouTube Music in your default browser...")
    webbrowser.open("https://music.youtube.com/")

#Google function:
def openChrome():
    print("Launching Chrome...")
    webbrowser.open("google.com")

#Insult Me Function
def insultMe():
    randomNumber = random.randint(0,10)

    if randomNumber == 0:
        print("You are more disapointing than an unsalted pretzel.")
    
    if randomNumber == 1:
        print("Don’t be ashamed of who you are. That’s your parents’ job.")
    
    if randomNumber == 2:
        print("Someday you’ll go far… and I really hope you stay there.")

    if randomNumber == 3:
        print("I’m busy right now; can I ignore you another time?")

    if randomNumber == 4:
        print("You are like a cloud. When you disappear, it’s a beautiful day.")

    if randomNumber == 5:
        print("You’re the reason this country has to put directions on shampoo.")

    if randomNumber == 6: 
        print("I never forget a face, but in your case, I'll make an exception.")

    if randomNumber == 7:
        print("Only two things are infinite: the universe and your stupidity, and I'm not so sure about the first.")

    if randomNumber == 8:
        print("You look like you came from a donation pile.")

    if randomNumber == 9:
        print("*Thumbs down*")

    if randomNumber == 10:
        print("You're the gray sprinkle on a rainbow cupcake.")

#Report a bug
def reportBug():
    print("Click on the 'New Issue' button")
    print("(It's near the top right)")
    webbrowser.open("https://github.com/Gamechamp30/JoeThePersonalAssistant/issues")

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
        print("time")
        print("random")
        print("datetime")
        print("sys")
        print("webbrowser")
        print("My internal programing contains over 300 lines as of 11/15/21")
        print("I am also completly open source")
        print("You can use the 'link to source code' command to find my code")

    if moreInfo == "n":
        return


#Source Code Function
def sourceCode():
    print("The link to my source code is 'https://github.com/Gamechamp30/JoeThePersonalAssistant'")

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


#Saying hello and asking for the user's name
print("Hello!")
userName = input("What's your name? ")
print("Hi " + userName + ", I am Jeff, your personal assistant.") #And no, we aren't Jeff Bezos; we aren't going to steal your data
print("To get started type: 'what can i ask you' ")


while running == True:

        action = input("\nYou can ask me (almost) anything: ")

        #Function List
        if action == "what can i ask you":
            funclist()
            counter = counter2 + 1

        #Square Root
        if action == "square root":
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

        #Multiply
        if action == "multiply":
            multiply()
            counter = counter2 + 1

        #Encode
        if action == "encode":
            encode()
            counter = counter2 + 1

        #Day
        if action == "what is the date":
            whatDayIsIt()
            counter = counter2 + 1
        
        #Insult Me
        if action == "insult me":
            insultMe()
            counter = counter2 + 1

        #Spotify
        if action == "open spotify":
            openSpotify()
            counter = counter2 + 1

        #YouTube Music
        if action == "open youtube music":
            openYTMusic()
            counter = counter2 + 1

        #Chrome
        if action == "open google":
            openChrome()
            counter = counter2 + 1
        
        #Report a bug
        if action == "report a bug":
            reportBug()
            counter = counter2 + 1

        #Exit
        if action == "exit":
            exit()   
            counter = counter2 + 1    

        #Info
        if action == "who made you":
            credits()
            counter = counter2 + 1

        #Source Code
        if action == "link to source code":
            sourceCode()
            counter = counter2 + 1

        #More info
        if action == "technical info":
            techinfo()
            counter = counter2 + 1



        #If user input isn't valid:    
        if counter == 0:
            print("Sorry, I can't help with that")


