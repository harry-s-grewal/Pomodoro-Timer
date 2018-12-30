# Pomodoro-Timer v 1.0
This application is a simple desktop Pomodoro timer based in Python.

Explaination of the Pomodoro Method:
  The Pomodoro method is a well known method of working efficiently without burning out.
    Essentially, a user works for 25 minutes, then takes a 5 minute break. 
    After performing 4 25-minute work sessions (aka pomodoros), the short break is supplemented with a long break, totalling 30 minutes.
    This continues until all the work is done (or the workday is over).

Usage:
  Using the Pomodoro method, the timer starts with preset values for pomodoros as defined by Francesco Cirillo himself.
    25 minutes working, 5 minutes of short break, 25 minutes of long break.
  The program gives the option for users to enter their own values for the timer, to their own preference (with some limitations). 
    Negative times are not accepted, and neither are times exceeding 300 minutes.
  The user can skip any given timer using the hotkey CTRL C
  After each long break, the user is prompted to choose whether they will continue working or quit
    Upon quitting, the user is able to see a brief report of the work they have completed.
