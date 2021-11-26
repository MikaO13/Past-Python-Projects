"""
Calender
Programmer: Mika Okamoto
"""

from time import sleep, strftime

USER_FIRST_NAME = "Pixie"

calender = {}

def welcome():
  print "Welcome, " + USER_FIRST_NAME + "."
  print "Calendar starting..."
  sleep(1)
  print "Today is: " + strftime("%A %B %d, %Y") 
  print "The time is: " + strftime("%H:%M:%S") 
  sleep(1)
  print "What would you like to do?"
  
def start_calender():
  welcome()
  start = True
  while start:
    user_choice = raw_input("A to Add, U to Update, V to View, D to Delete, X to Exit: ")
    user_choice = user_choice.upper()
    if user_choice == 'V': 
      if len(calendar.keys()) < 1:
        print "Calendar empty."
      else:
        print calender
    elif user_choice == 'U':
      date = raw_input("Enter date (MM/DD/YYYY): ")
      update = raw_input("Enter the update: ")
      calendar[date] = update
      print "Update Successful!"
      print calender
    elif user_choice == 'A':
      event = raw_input("Enter event: ")
      date = raw_input("Enter date (MM/DD/YYYY): ")
      if(len(date) > 10) or int(date[6:]) < int(strftime("%Y"))):
        print("Invalid Date.")
        try_again = raw_input("Try Again? Y for Yes, N for No: ")
        try_again = try_again.upper()
        if try_again == 'Y':
          continue
        else:
          start = False
      else:
        calender[date] = event
        print "Adding Event Successful!"
        print calender
    elif user_choice == 'D':
      if len(calendar.keys()) < 1:
        print "Calender is empty."
      else:
        event = raw_input("Enter event: ")
        deleted = False
        for date in calendar.keys():
          if event == calendar[date]:
            del calendar[date]
            deleted = True
            print "Deleting Event Successful!"
            print calender
        if deleted == True:
          print "Incorrect Event Specified"
    elif user_choice == "X":
      start = False
    else:
      print "Invalid Command"

start_calender()
    
            
            
            