"""--------------------------------------------------------------------------------
Title: Timer_v1.3.py
Description: Simple Python Pomodoro Timer
By: Harry Grewal
Date: Most recently updated on 12/01/2019
--------------------------------------------------------------------------------"""

import os # To make the cls() function OS independent
from pygame import mixer, time # Pygame mixer allows utilization of sounds, time allows time manipulation native to pygame
mixer.init()  # Initializes PyGame Mixer

class soundInit:

    # Set filepath to where .exe unpacks data
    #filePath = getattr(sys, '_MEIPASS', os.getcwd()) # Use for generating .exe's
    
    # Set filePath to locate music files regardless of where the user has saved the folder
    filePath = os.path.dirname(os.path.realpath(__file__)) # Use for debugging/running .py

    workBell = mixer.Sound(filePath + "\workBell.wav") # Travis Scott ad-lib
    shortbreakBell = mixer.Sound(filePath + "\shortBreakBell.wav") # Royalty free gong
    longbreakBell = mixer.Sound(filePath + "\longBreakBell.wav") # Royalty free chime
    AnothaOne = mixer.Sound(filePath + "\KhaledAnothaOne.wav") # DJ Khaled - Anotha one


    def playWorkBell(self):
        if soundOption == 0:
            return
        self.workBell.play()
        return
    
    def playShortBreakBell(self):
        if soundOption == 0:
            return
        self.shortbreakBell.play()
        return
    
    def playLongBreakBell(self):
        if soundOption == 0:
            return
        self.longbreakBell.play()
        return

    def playAnothaOne(self):
        if soundOption == 0:
            return
        self.AnothaOne.play()
        return

def cls(): # Function to clear screen
    os.system('cls' if os.name =='nt' else 'clear') # Uses 'cls' for Windows (nt) and 'clear' for Linux and OSX

def editIntChecker(edit_to_check, list_iteration): # Checks to see if inputs are integers or not
    try:
        int(edit_to_check) # If it is not an int, it will produce an error, which will go into the 'except' branch

        if int(edit_to_check) < 1:
            print("That amount of time is too small. Come on now! Set the bar higher. The {0} value remains at {1} minutes.".format(timeName[list_iteration], timeValue[list_iteration]))
        
        elif int(edit_to_check) > 300:
            print("That amount of time is too large. Be realistic! The {0} timer remains at {1} minutes.".format(timeName[list_iteration], timeValue[list_iteration]))
        
        else:
            timeValue[list_iteration] = edit_to_check
            print("The {0} timer has been set to {1} minutes.".format(timeName[list_iteration], timeValue[list_iteration]))

    except ValueError:
        print("Sorry, but that was not a valid input. The", timeName[list_iteration], "timer remains at", timeValue[list_iteration],"minutes.")

def timer(timer_Length, list_Iteration): # The actual timer portion of the program
    m = 0 # Calculates the number of minutes that have passed

    print("Starting {0} timer...".format(timeName[list_Iteration]))

    # The purpose of the try/except in this function is to allow the user to exit a pomodoro session at any time
    # By pressing CTRL C, the user enters a Keyboard Interrupt, which is handled by skipping the session
    try:
        for i in range(timer_Length*60): # timer_length*60 Converts minutes to Seconds

            # Increments number of minutes to show how many minutes remain
            if i%60 == 0:
                m = m+1
            
            # Updates time remaining
            print("Time Remaining: {0} minutes {1} seconds remaining ".format(timer_Length - m, 59 - i%60), end="\r")

            # The wait function suspends the execution of all code for 1000 ms 
            time.wait(1000) #(for debugging, set this value to 10)
        cls()
        return 1
    
    except KeyboardInterrupt: # This allows the user to skip their current session
        print("Session skipped                                 ") # Whitespace is to erase anything that may still be in the line
        return 0

def main():
    #Variables are initialized here to become global variables
    global timeValue
    global timeName
    global sessions_completed
    global soundOption

    timeValue = [25, 5, 25] # Get these from json file. Keep them as the previously programmed set of time values
    timeName = ["work", "short break", "long break"] # Global list for use in printing during loops
    sessions_completed = [0, 0, 0, 0] # Work, short break, long break, combined total (minutes)
    soundOption = 1 # Default: sounds are on
    
    # Initializes sound objects
    sound = soundInit()

    print("Pomodoros set to {0} minutes of work, {1} minutes of intermediate breaks, and {2} minutes of long breaks".format(timeValue[0], timeValue[1], timeValue[2]))

    validInput = False

    while validInput == False: # This loop checks to see if the input is valid or not

        print("What would you like to do?\nTo start the timer, press enter: \nTo edit the pomodoro settings, type 'EDIT'")

        # Gives user option to turn sound on and off. Default is on
        if soundOption == 1:
            print("To turn off sounds, type 'SOUND OFF'")
        elif soundOption == 0:
            print("To turn on sounds, type 'SOUND ON'")
        userInput = str(input())
        cls()

        if userInput == '':
            cls()
            validInput = True

        elif userInput.upper() == 'EDIT': # Allows user to change the values of the pomodoro timer

            work_input = input("Enter the value you would like to set the work time to, in minutes: ")
            editIntChecker(work_input, 0)

            shortBreak_input = input("Enter the value you would like to set the short break time to, in minutes: ")
            editIntChecker(shortBreak_input, 1)

            longBreak_input = input("Enter the value you would like to set the long break time to, in minutes: ")
            editIntChecker(longBreak_input, 2)
        
        elif userInput.upper().replace(" ","") == 'SOUNDOFF': # Turns sound off

            soundOption = 0
            print("Sounds have been turned off.")
        
        elif userInput.upper().replace(" ","") == 'SOUNDON':

            soundOption = 1
            print("Sounds have been turned on.")
        
        else:
            print("Sorry, but that's not a valid input. Try again.")

    print("To skip a timer, press CTRL C. \n \n") # CTRL C is a keyboard interrupt

    want_to_continue = True

    while want_to_continue == True: # Pomodoros will continue as long as the user would like

        for a in range(0,4): # This loops the pomodoro structure 4 times

            for i in range(0,2): # This loops through the timer function 2 times, one for the work session and one for the break session
                # This line allows the number of sessions completed to be recorded
                sessions_completed[i] = sessions_completed[i] + timer(int(timeValue[i]), i)

                if i == 0:
                    sound.playWorkBell()
                
                elif i == 1:
                    sound.playShortBreakBell()
                

        # This is a hardcoded long break, which only comes after 4 work and short break sessions have been completed.
        sessions_completed[2] = sessions_completed[2] + timer(int(timeValue[2]), 2)
        # This is to play the accompanying alarm bell
        sound.playLongBreakBell()

        for i in range(0,2): # This for loop simply adds up all the minutes spent working
            sessions_completed[3] = int(sessions_completed[3]) + int(sessions_completed[i])*int(timeValue[i])

        validInput = False

        while validInput == False: # This loop checks to see if the inputs are valid

                print("You have been working for {0} minutes (including breaks). Would you like to continue? Y/N".format(sessions_completed[3]))

                userInput = input()

                if userInput.upper() == 'Y':
                    cls()
                    sound.playAnothaOne()
                    print("Good choice. Lets get some work done!")
                    validInput = True

                elif userInput == 'N' or userInput == 'n':
                    cls()
                    want_to_continue = False
                    validInput = True

                else:
                    print("Sorry, but that's not a valid input. Try again.")

    print("Final Report:\nYou have completed {0} pomodoros, and have been working for {1} hours.".format(sessions_completed[0], int(sessions_completed[3]*100/60)/100))

    input("Press enter to exit.")

    # :)

cls()
main()