import time #For time.sleep()
import os #To make the cls() function OS independent

def cls(): #Function to clear screen
    os.system('cls' if os.name =='nt' else 'clear') #Uses 'cls' for Windows (nt) and 'clear' for Linux and OSX

def editIntChecker(edit_to_check, list_iteration): #Checks to see if inputs are integers or not
    try:
        int(edit_to_check) #If it is not an int, it will produce an error, which will go into the 'except' branch

        if int(edit_to_check) < 1:
            print("That amount of time is too small. Come on now! Set the bar higher. The", timeName[list_iteration], "value remains at", timeValue[list_iteration],"minutes.")
        
        elif int(edit_to_check) > 300:
            print("That amount of time is too large. Be realistic! The", timeName[list_iteration], "timer remains at", timeValue[list_iteration],"minutes.")
        
        else:
            timeValue[list_iteration] = edit_to_check
            print("The", timeName[list_iteration], "timer has been set to",timeValue[list_iteration],"minutes.")

    except ValueError:
        print("Sorry, but that was not a valid input. The", timeName[list_iteration], "timer remains at", timeValue[list_iteration],"minutes.")

def timer(timer_Length, list_Iteration): #The actual timer portion of the program
    m = 0 #Calculates the number of minutes that have passed

    print("Starting", timeName[list_Iteration], "timer...")

    #The purpose of the try/except in this function is to allow the user to exit a pomodoro session at any time
    #By pressing CTRL C, the user enters a Keyboard Interrupt, which is handled by skipping the session
    try:
        for i in range(timer_Length*60):

            if i%60 == 0:
                m = m+1

            print("Time Remaining:", timer_Length - m, "minutes",59 - i%60,"seconds remaining ", end="\r")

            time.sleep(0.25)
        cls()
        return 1
    
    except KeyboardInterrupt: #This allows the user to skip their current session
        print("Session skipped                                 ") #Whitespace is to erase anything that may still be in the line
        return 0

timeValue = [25, 5, 25] #Get these from json file. Keep them as the previously programmed set of time values
timeName = ["work", "short break", "long break"] #Global list for use in printing during loops
sessions_completed = [0, 0, 0, 0] #Work, short break, long break, combined total (minutes)

print("Pomodoros set to", timeValue[0] ,"minutes of work,", timeValue[1] , "minutes of intermediate breaks, and", timeValue[2], "minutes of long breaks")

validInput = False

while validInput == False: #This loop checks to see if the input is valid or not

    print("What would you like to do?\nTo start the timer, press enter: \nTo edit the pomodoro settings, type 'EDIT'")
    userInput = str(input())
    cls()

    if userInput == '':
        cls()
        validInput = True

    elif userInput == 'EDIT' or userInput == 'edit': #Allows user to change the values of the pomodoro timer

        work_input = input("Enter the value you would like to set the work time to, in minutes: ")
        editIntChecker(work_input, 0)

        shortBreak_input = input("Enter the value you would like to set the short break time to, in minutes: ")
        editIntChecker(shortBreak_input, 1)

        longBreak_input = input("Enter the value you would like to set the long break time to, in minutes: ")
        editIntChecker(longBreak_input, 2)
    
    else:
        print("Sorry, but that's not a valid input. Try again.")

print("To skip a timer, press CTRL C. \n \n") #CTRL C is a keyboard interrupt

want_to_continue = True

while want_to_continue == True: #Pomodoros will continue as long as the user would like

    for a in range(0,4): #This loops the pomodoro structure 4 times

        for i in range(0,2): #This loops through the timer function 2 times, one for the work session and one for the break session
            #This line allows the number of sessions completed to be recorded
            sessions_completed[i] = sessions_completed[i] + timer(int(timeValue[i]), i)

    #This is a hardcoded long break, which only comes after 4 work and short break sessions have been completed
    sessions_completed[2] = sessions_completed[2] + timer(int(timeValue[2]), 2)

    for i in range(0,2): #This for loop simply adds up all the minutes spent working
        sessions_completed[3] = sessions_completed[3] + int(sessions_completed[i])*int(timeValue[i])

    validInput = False

    while validInput == False: #This loop checks to see if the inputs are valid

            print("You have been working for", sessions_completed[3], "minutes (including breaks). Would you like to continue? Y/N")

            userInput = input()

            if userInput == 'Y' or userInput == 'y':
                cls()
                print("Good choice. Lets get some work done!")
                validInput = True

            elif userInput == 'N' or userInput == 'n':
                cls()
                want_to_continue = False
                validInput = True

            else:
                print("Sorry, but that's not a valid input. Try again.")

print("Final Report:\nYou have completed", sessions_completed[0], "pomodoros, and have been working for", int(sessions_completed[3]*100/60)/100, "hours.")

input("Press enter to exit.")

# :)