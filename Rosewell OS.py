from datetime import date
import webbrowser
import sys
import os
import random
import sys
import time

ans = ""
name = ""
rulez = ""
note = 0
f = ""
dirtory = ""
folder = ""
file = ""
todo = ""
import subprocess

def importProgram(dirtory):
    try:
        import dirtory
    except ModuleNotFoundError:
        try:
            exec(open(dirtory).read())
        except Exception as e:
            print(e)

def wordname():
    n = random.randint(1, 5)
    if n == 1:
        print("Welcome " + name + " What Would You Like to do?")
    if n == 2:
        print("Anything you Want to do Today " + name + "?")
    if n == 3:
        print("Have you Decided What to do Today " + name + "?")
    if n == 4:
        print("What Would you Perfer to do Today " + name + "?")
    if n == 5:
        print("Anything on your Mind " + name + "?")
def anyelse():
    b = random.randint(1, 6)
    if b == 1:
        print("Anything Else " + name + "?")
    if b == 2:
        print("Do you Want to do Anything Else " + name + "?")
    if b == 3:
        print("Do you Perfer Anything Else " + name + "?")
    if b == 4:
        print("Have you Decided to do Anything Else " + name + "?")
    if b == 5:
        print("Any other Tasks " + name + "?")
    if b == 6:
        print("Anything else todo " + name + "?")
def goodbye():
    c = random.randint(1, 3)
    if c == 1:
        os.system( " say Goodbye " + name )
        print("Goodbye " + name)
    if c == 2:
        os.system( " say Have a Nice Day " + name )
        print("Have a Nice day " + name)
    if c == 3:
        os.system( " say See you Later " + name )
        print("See you Later " + name )

res = ""
txtfile = ""
today = date.today()
rose = "© Blake Gouthro | Rosewell OS V1.3.5 | Rosewell Software | Nov. 9th 2021 - " + str(today.year) + " | Today's Date = " + str(today) + " ©"
while True:
    print(rose)
    
    print("Contact Rosewell Software at rosewellsoftware@Gmail.com")
    print(" ")
    print("Type 'Help' in the 'What would you like to do prompt' or 'Anything else prompt' for a list of commands you can type. Type 'setup' to install the modules required for running some programs in Rosewell OS. Type '///' in any Document to end writing that document.")
    print(" ")
    print("Welcome to Rosewell OS! My name is CONRAD. I am here to Help. What is your name?")
    name = input()
    wordname()
# Recovery Mode
    if name == "recovery" or name == "Recovery" or name == "recovery mode" or name == "Recovery Mode":
        print("Booting into Recovery mode . . . . .")
        print("© Recovery Mode | V 1.3.5 | Rosewell OS | 2021 - " + str(today.year))
        print("[1] Restart")
        print("[2] Options")
        rec = int(input("Please Enter a Number:"))
        if rec == 2:
            print("[1] Disk Repair")
            print("[2] File Reocvery")
            print("[3] Terminal")
            print("[4] Quit")
            opt = int(input("Please Enter a Number:"))

            if opt == 1:
                print("Booting Disk Utility. . . . .")
                import os
                import subprocess

                subprocess.run(["/usr/bin/open", "-a" + "Disk Utility"])
                os.system("open -a " + "Disk Utility")
                print("Returning to Normal Rosewell OS")
                print(rose)


            elif opt == 2:
                print("Booting Time Machine. . . . . ")
                import os
                import subprocess

                subprocess.run(["/usr/bin/open", "-a" + "Time Machine"])
                os.system("open -a " + "Time Machine")
                print("Returning to Normal Rosewell OS")
                print(rose)
            elif opt == 3:
                subprocess.run(["/usr/bin/open", "-a" + "Terminal"])
                os.system("open -a " + "Terminal")
                print("Returning to Normal Rosewell OS")
                print(rose)
            elif opt == 4:
                print("Exiting Recovery Mode . . . . .")
        elif rec == 1:
            print("Exiting Recovery Mode . . . . .")
            print(rose + " What would you like to do?")
    while True:
        todo = input()
#Quits OS
        if todo == "Quit" or todo == "quit" or todo == "No" or todo == "no":
            goodbye()
            break
#Help
        if todo == "Help" or todo == "help":
            print("Here is a List of Commands for Prompt")
            print("Help - See a List of commands for prompt")
            print("Internet or internet or Web Browsing or web browsing or Web or web - Opens your default web browser for the internet")
            print("Calculator or calculator or Calc or calc - Opens the Rosewell Calculator")
            print("Note or note - Opens a Note, Lets you write on it, and Saves it for later")
            print("Delete Note or delete note - Allows you to Delete the note you have created")
            print("Review or review or Review Note or review note lets you delete or not a note")
            print("Quit or quit - Quit an Application or Quit the OS(Operating System)")
            print("Open App or App or open app or app or Open or open - Open any app outside the system")
            print("Search or google search - enter a keyword to open google and search results for")
            print("load or load app - load an external compatible .py document to run a app inside the operating system.")
            print("Word - opens the new OpenOffice Word Processor")
            print("Email - Opens the New Email Client")
            print("Calendar - Opens the New Rosewell Calendar App")
            print("Chess - Open a new Game of Chess")
            print("Weather - shows weather of city for current city inputed")
            print("Music - Opens the Music app")
            print("Clock - Opens the Clock App")
            print("Disk Copy - Opens the Disk Copy Program to copy and convert files")
            print("Rosewell Tetris - Opens a new game of Rosewell Tetris")
            print("Stick - Opens a new Game Of Sticks session")
            print("Setup - Opens the Setup App for Installing Modules")
            print("Error (27) means you have either types a word incorrectly or the command for that word doesn't exist")
            print("Restart - Restarts the entire OS")
            anyelse()
            continue
#JinHo Secret
        if todo == "JinHo" or todo == "JinHo Mo" or todo == "jinho" or todo == "jinho mo":
            print("Congratulations " + name + "! You have found the JinHo Easter Egg!")
            print("© JinHo Load | Rosewell Software | Rosewell OS | V1.2 | 2021 - " + str(today.year) + " ©")
            print(
                "The Load app feature was coded by JinHo Mo to load apps in Rosewell and to code apps outside of the OS. we can still add in new features too!")
            print("This Easter Egg is for JinHo, Thanks for the Help! -Blake Gouthro")
            anyelse()
            continue
#Restart
        if todo == "Restart" or todo == "restart" or todo == "Restart System" or todo == "restart system":
            print("Restarting...")
            break
#Secret 1
        if todo == "Hello World" or todo == "hello world":
            print("Hello World, " * 5)
            print("Hello " + name + ". Would You Like To Play A Game?")
            anyelse()
            continue
#Secret 2
        if todo == "20050421":
            print("Congratulations " + name + "! You have found an Easter Egg!")
            print("I was given instructions once you found this Secret to tell you this...")
            print(rose)
            print(
                "Roswell is an Operating System from Geek and Computer Nerd Blake Gouthro. 90% of Rosewell OS Was codeded from Blake Gouthro with 10% from the Internet. JinHo Mo created the Import App Feature to import code into the system and run it")
            print("Rosewell 2021 - " + str(
                today.year) + " Conrad was an Idea of an Artifitical Intelligence and now is the Operating System you Talk to.")
            print("Rosewell OS was created on November 9th 2021")
            print(
                "Rosewell OS was Created for you to ask the OS(Operating System) what to do instead of typing in commands you will never remember.")
            print("Type Help or help into the 'What would you like me to do?' prompt to find a list of commands.")
            anyelse()
            continue
#Secrets
        if todo == "Secret" or todo == "secret":
            print("List of Secrets")
            print("20050421 - Blake Gouthro's Birthday, enter into prompt for test about Rosewell OS")
            print("Secret or secret - printsa list of secrets")
            print("Happy Birthday or happy birthday - sings you happy birthday")
            print("Rosewell or Creator - Rosewell Info")
            print("JinHo or jinho mo - type this to show a secret about who created the load app feature")
            anyelse()
            continue
#Secret 3
        if todo == "Creator" or todo == "creator" or todo == "Rosewell" or todo == "rosewell":
            print(rose)
            anyelse()
            continue
#Internet
        if todo == "Internet" or todo == "Safari" or todo == "Web Browsing" or todo == "internet":
            webbrowser.open("https://www.google.com")
            print(rose)
            anyelse()
            continue
#Google Search
        if todo == "Search" or todo == "search" or todo == "Google Search" or todo == "google search":
            print("What would you like to search on Google " + name + "?")
            gog = input()
            url = "https://www.google.com.tr/search?q={}".format(str(gog))
            webbrowser.open_new_tab(url)
            anyelse()
            continue
#Note
        if todo == "Note" or todo == "Write Note" or todo == "Notes" or todo == "notes" or todo == "note" or todo == "write note":

            print("Write your note here and it will be saved. NOTE; The Note will only be saved for the session of the OS currently open")
            
            note = input()
            print("Saving ... 1% ... 10% ... 25% ... 75& ... 100%")
            print("Your Note Has Been Saved " + name + "!")
            anyelse()
            
            continue
#Show Note
        if todo == "Show Note" or todo == "show note" or todo == "review" or todo == "Review" or todo == "Review Note" or todo == "review note":
            print(note)
            
            anyelse()
            continue
#Delete Note
        if todo == "Delete Note" or todo == "delete note":
            print("Are You Sure " + name + "?")
            
            yn = input()
            if yn == "Yes" or yn == "yes" or yn == "y" or yn == "Y":
                note = "0"
                print("Erasing ... 1% ... 10% ... 25% ... 75% ... 100%")
                print("Your Note has been erased")
                print(note)
                anyelse()
                
                continue
            elif yn == "No" or yn == "no" or yn == "n" or yn == "N":
                note = note
                print(rose)
                anyelse()
                
                continue
#JinHo Load
        if todo == "load" or todo == "Load":
            import sys
            import os

            print("© JinHo Load | Rosewell Software | Rosewell OS | V1.2 | 2021 - " + str(today.year) + " ©")
            
            loading = input("Enter File name to load: ")
            importProgram(str(loading))
            print(rose)
            anyelse()
            
            continue
#Email
        if todo == "Email" or todo == "email" or todo == "send email" or todo == "Send Email":
            from datetime import date
            today = date.today()
            import smtplib, ssl
            import email

            print("© Blake Gouthro | Rosewell Software | Email | Rosewell OS | V1.3 | 2021 - " + str(today.year) + " ©")
            print("Welcome to Email in Rosewell OS, Works with Both Gmail and Hotmail Accounts. Please Select an Option Below NOTE: no need to type @Gmail.com or @Hotmail.com")
            print("NOTE2: Hotmail can and will be buggy to send emails with, it depends on the SMTP AUTH settings of your Hotmail Account")
            

            while True:
                print("[1] Send a Gmail Email")
                print("[2] Send a Hotmail Email")
                print('[3] Manual')
                print("[4] Quit")
                choice = int(input("Please Enter a number here: " ))

                if choice == 1:
                    port = 587
                    smtp_server = "smtp.gmail.com"
                    sender_email = input("Put sender gmail account here: " )
                    sender_email = sender_email + "@Gmail.com"
                    receiver_email = input("Put reviever gmail account here: " )
                    receiver_email = receiver_email + "@Gmail.com"
        
        
                    password = input('Please enter your Sender Account Password: ')
                    message = input("Enter Text Email Here: " )

                    context = ssl.create_default_context()
                    with smtplib.SMTP(smtp_server, port) as server:
                        server.ehlo()  
                        server.starttls(context=context)
                        server.ehlo()  
                        server.login(sender_email, password)
                        server.sendmail(sender_email, receiver_email, message)
                        print("Email Has Been Sent")
                        print("Options Below: ")
                        
                        continue
                elif choice == 2:
                    port = 587
                    smtp_server = "smtp.live.com"
                    sender_email = input("Put sender Hotmail account here: " )
                    sender_email = sender_email + "@Hotmail.com"
                    receiver_email = input("Put reviever Hotmail account here: " )
                    receiver_email = receiver_email + "@Hotmail.com"
        
        
                    password = input('Please enter your Sender Account Password: ')
                    message = input("Enter Text Email Here: " )

                    context = ssl.create_default_context()
                    with smtplib.SMTP(smtp_server, port) as server:
                        server.ehlo()  
                        server.starttls(context=context)
                        server.ehlo()  
                        server.login(sender_email, password)
                        server.sendmail(sender_email, receiver_email, message)
                        print("Email Has Been Sent")
                        print("Options Below: ")
                        
                    continue
                elif choice == 3:
                  print('''Email is a Very Simple Application.
You can either Send a Hotmail Email or a Gmail Email.
the program will ask you for Sender Email in each one, then Reciever Email, then Sender Email Password, then you can type the message.
Once done, the email will be automatically sent frim the senderxemail to the recieber email.''')
                  print(' ')
                  print('Main Menu')
                  continue
                elif choice == 4:
                    print("Goodbye, thanks for using Rosewell Email!")
                    break
            print(rose)
            anyelse()
            
            continue
#Clock
        if todo == "clock" or todo == "Clock":
            
            import sys
            import calendar
            import os
            import time
            from datetime import date
            from datetime import datetime
            import pytz
            import re
            import requests
            today = date.today()
            
            def time_convert(sec):
              mins = sec // 60
              sec = sec % 60
              hours = mins // 60
              mins = mins % 60
              print("Time Lapsed = {0}:{1}:{2}".format(int(hours),int(mins),sec))
              input("Press Enter to start")
              start_time = time.time()
              input("Press Enter to stop")
              end_time = time.time()
              time_lapsed = end_time - start_time
              print(" ")
              print(round(time_lapsed, 2))
              print("Seconds")
              print(" ")

            def validate_time(alarm):
              if len(alarm) != 8:
                return "Invalid time format! Please try again..."
              else:
                if int(alarm[0:2]) > 24:
                  return "Invalid HOUR format! Please try again..."
                elif int(alarm[3:5]) > 59:
                  return "Invalid MINUTE format! Please try again..."
                elif int(alarm[6:8]) > 59:
                  return "Invalid SECOND format! Please try again..."
                else:
                  return "ok"

            print("© Blake Gouthro an=d JinHo Mo | Clock | V1.4 | Rosewell Software | 2021 - " + str(today.year) + " ©")
            print("Welcome to the Offical Clock app from Rosewell Software for Rosewell OS! Select a number from the options below")

            while True:
              print('''[1] Time and Date Check
[2] Alarm Clock
[3] World Clock
[4] StopWatch
[5] Manual
[6] Quit''')
              clock = int(input("Please enter a number: " ))
              if clock == 6:
                print("Exiting Clock App")
                print(rose)
                anyelse()
                break
              if clock == 5:
                print('''-----Clock App Manual-----
    The Clock app was designed with a number of things you can do with it in mind.
- The Time and Date check, will ask you forcthe month and year, then output the calendar, today's date, and the current time.
- The Alarm clock will alow to set an alarm, label it, then when the current time matches the alarm time, it will print the label and say the label.
- The World clock will allow you to list the different timezones, then you can use those to convert the current time to whatever time it is in that timezone.
- The Stopwatch is a feature where it will time you for how long the delay is between pressing enter to start and enter to end. it will round the Seconds to 2 Decimal Places.''')
              if clock == 1:
                yy = int(input("Enter Year Digits(yyyy): " ))
                mm = int(input("Enter Month Digits(mm): " ))
                print(calendar.month(yy,mm))
                print("Today's Date: " + str(today))
                current_time = time.strftime("%H:%M:%S", time.localtime())
                print("Current Time =", current_time)
                print(" ")
                print("Please Select an Option Below")
                continue
              if clock == 2:
                alarm = input("Enter Alarm Time (24 hour clock) [HH:MM:SS]: " )
                label = input("Enter Alarm Label(What you want the alarm to say when it goes off: " )


                while True:
                  validate = validate_time(alarm)
                  if validate != "ok":
                      print(validate)
                      continue
                  elif validate == "ok":
                      print(f"Setting alarm for {alarm}...")
                      break



                while True:
                  current_time = time.strftime("%H:%M:%S", time.localtime())
                  if current_time == alarm:
                    os.system( " say " + label )
                    print(label)
                    print("Main Menu")
                    break
                  else:
                    continue

              if clock == 4:

                time_convert(0)
                print("Main Menu")
                continue

                print("Main Menu")
                continue

              if clock == 3:
                timezones = pytz.all_timezones
                zones = {v:timezones[j] for j, v in enumerate((i.split("/")[-1:][0].lower().replace("_", " ") for i in timezones))}
                zones.update({v:timezones[j] for j, v in enumerate((i.split("/")[-1:][0].lower() for i in timezones))})
                print("\n[1] Convert Time\n[2] List all Time Zones\n[3] Quit to Main Menu")
                while True:
                  timz = int(input("Enter a Number: " ))
                  current_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                  if timz == 2:
                      for tz in timezones:
                          print(tz)
                  if timz == 1:
                    print("Check the world clock list for the timezone names Put quit to exit to main menu. ")
                    user = input("Put Place of Timezone to convert to or timezone Code(Ex. Canada/Atlantic): " )
                    key = ""
                    if user.lower() in zones.keys() or user in zones.keys():
                        key = zones[user.lower()]
                    else:
                        key = user
                    try:
                        tz = pytz.timezone(key)
                        cur_time = datetime.now(tz)
                        user.split("/")
                        print(f"Current time : {current_time}")
                        print(f"Current time of {key} : {str(cur_time).split('.')[0]}")
                    except pytz.exceptions.UnknownTimeZoneError:
                        print("NotFound")
                  if time == 3:
                    print("Going back to Main Menu...")
                    break
                  print("Main Menu")
                  break
                continue
              continue


            continue
              
#Calculator
        if todo == "Calc" or todo == "calc" or todo == "Calculator" or todo == "calculator":
            print("© Blake Gouthro | Calculator | V1.5.7 | Rosewell Software | Current Date = " + str(today) + " ©")
            print("© Welcome to Rosewell Calculator! If you save a calculation to a document, type '///' to end writing. ")
            print("Type equation here to see result. If you want to quit Calculator type '5'")
            ANS = ""
            bla = ""
            # This function adds two numbers
            def add(x, y):

                bla = x + y
                
                return bla
                # This function subtracts two numbers


            def subtract(x, y):

                bla = x - y
                return bla
                # This function multiplies two numbers


            def multiply(x, y):

                bla = x * y
                return bla
                # This function divides two numbers


            def divide(x, y):

                bla = x / y
                return bla
            def remainder(x, y):

                bla = x % y
                return bla
            
            while True:
                # take input from the user
                print('Main Menu')
                print(' ')
                
                print("Select operation.")
                print("[1] Add")
                print("[2] Subtract")
                print("[3] Multiply")
                print("[4] Divide")
                print("[5] Remainder")
                print("[6] Copy a Number to the Clipboard")
                print('[7] Manual')
                print("[8] Quit")
                print(' ')

                choice = input("Enter choice(1/2/3/4/5/6/7/8): ")
                if choice == '7':
                  
                  print('''-----Rosewell Calculator Manual-----
    The Rosewell Calculator was Designed as one of the First major Applications built-in to Rosewell OS with feature being added all the time.
- Addition. Adds the First Number to the Second Number.
- Subtraction. Subtracts the First number from the Second Number.
- Multiplication. Multiplys the First number by the Second Number
- Division. Divides the First Number by the Second Number.
- Remainder. The Remainder option finds the Remainder of the two Numbers.
- Copy to Clipboard. Allows You to save one number to the clipboard to use later.
- Save to Document. Allows you to save your work to a text document.''')
                  
                  continue

                # check if choice is one of the four options
                if choice == '8':
                    print(rose)
                    anyelse()
                    
                    break
                if choice in ('1', '2', '3', '4', '5', '6', '7', '8'):
                    if choice == '6':
                        lc2 = input("Enter a Number to be saved to the Clipboard. type 'menu' to go back to menu: " )
                        if lc2 == "Menu" or lc2 == "menu":
                            print("Main Menu")
                            continue
                        else:
                            lc2 = int(lc2)
                            lc2 = float(lc2)
                            ANS = lc2
                            print("Saved to the Clipboard")
                            print("Main Menu")
                            continue
                    num1 = input("Enter first number. Type 'ans' to enter a number from the clipboard: ")
                    if num1 == "Ans" or num1 == "ans" or num1 == "ANS":
                        num1 = ANS
                    else:
                        num1 = int(num1)
                        num1 = float(num1)
                    
                    num2 = input("Enter second number. Type 'ans' to enter a number from the clipboard: ")
                    if num2 == "Ans" or num2 == "ans" or num2 == "ANS":
                        num2 = ANS
                    else:
                        num2 = int(num2)
                        num2 = float(num2)
                    
                    if choice == '1':
                        print(num1, "+", num2, "=", add(num1, num2))

                    elif choice == '2':
                        print(num1, "-", num2, "=", subtract(num1, num2))

                    elif choice == '3':
                        print(num1, "*", num2, "=", multiply(num1, num2))

                    elif choice == '4':
                        print(num1, "/", num2, "=", divide(num1, num2))
                    elif choice == '5':
                        print(num1, "%", num2, "=", remainder(num1, num2))
                    
                    elif choice == '8':
                        print(rose)
                        anyelse()
                        
                        break
                    

                        # check if user wants another calculation
                        # break the while loop if answer is no
                    
                    printcalc = input("Save to .txt Document?[y/n]: " )
                    if printcalc == "yes" or printcalc == "Yes" or printcalc == "Y" or printcalc == "y":
                        
                        newdoc = input("New Document?[y/n]" )
                        if newdoc == "yes" or newdoc == "Yes" or newdoc == "Y" or newdoc == "y":
                            
                            head = "mathcalc"
                            file = open(head + ".txt", "w")
                            content = ""
                            print("Enter Document Text: ")
                            while True:
                                line = input()
                                if "///" in line:
                                    break
                                content += line + "\n"
                            file.write(content)
                            file.close()
                            print(". . . . . .File Saved!")
                        elif newdoc == "No" or newdoc == "no" or newdoc == "N" or newdoc == "n":
                            while True:
                                head2 = "mathcalc"
                                try:
                                    file = open(head2 + ".txt", "r")
                        
                                    rulez = file.readlines()
                                    print("Enter Document Text: ")
                                    for i in rulez:
                                       print(i)
                                    file = open(head2 + ".txt", "w")
                                    break
                                except FileNotFoundError as e:
                                    print(e)
                                    continue
                            content = "\n".join(rulez) + "\n"
                            while True:
                                line = input()
                                if "///" in line:
                                    break
                                content += line + "\n"
                            file.write(content)
                            file.close()
                            print(". . . . . .File Saved!")
                            
                            continue
                    
                    ans = input("Save Answer to Clipboard?[y/n]")
                    if ans == "Yes" or ans == "yes" or ans == "Y" or ans == "y":
                        ANS = float(num1 + num2)
                        print("Saved answer to Clipboard!")
                        continue
                    elif ans == "No" or ans == "no" or ans == "n" or ans == "N":
                        ANS = 0
                        ("Answer not saved to Clipboard")
                        continue
            
                            
                    
            

                else:
                    print("Invalid Input")
                    
            continue
        if todo == "typing" or todo == "Typing" or todo == "Word Processor" or todo == "word processor" or todo == "word" or todo == "Word" or todo == "Word Processing" or todo == "word processing" or todo == "Open Office" or todo == "open office":
            head = ""
#Word Processor
            while True:
                print("© Blake Gouthro and JinHo Mo | Open Office Word Processor | V1.5.2 | Rosewell Software | 2021 - " + str(today.year) + "©")
                print("Welcome to Open Office! Rosewell's Word Processor Now Saves to other files!")
                print("Type '///' at the end of document to end Writing")
                print(' ')
                print('Main Menu')
                while True:
                    try:
                       
                        print("[1] New Documnet")
                        print("[2] Open Document")
                        print('[3] Manual')
                        print("[4] Quit")
                        
                        choice = int(input("Enter a number to Continue: " ))
                        break
                    except Exception:
                        print("Choice not found, Try Again?")
                if choice == 3:
                  print('''-----Word Processor Manual-----
    The Word Processor is a very Basic Word Processor for typing and kind of Word Document
- Formats. You can save a document to any one of the Following File Formats; ".txt", ".docx", and ".pages".
- Type "/// after writing the Document to ende writing the document.
- The Word Processor can Create and Open Word Documents''')
                  print(' ')
                  print('Main Menu')
                if choice == 1:
                    
                    head = input("Choose a Name for the Document: " )
                    print("Document Extensions, No Need to Type '.'")
                    print(".txt")
                    print(".docx")
                    print(".pages")
                    
                    ext = input("Enter .Extension, don't need to enter the period: " )
                    
                    file = open(head + "." + ext, "w")
                    content = ""
                    print("Enter Document Text, Type '///' to end writing: ")
                    while True:
                        
                        line = input()
                        if "///" in line:
                            break
                        content += line + "\n"
                    file.write(content)
                    file.close()
                    print(". . . . . .File Saved!")
                elif choice == 2:
                    while True:
                        
                        head2 = input("Enter name of Document to open, Typing 'quit' will go back to the beginning: " )
                        if head2 == "quit" or head2 == "Quit":
                            break
                        print("Document Extensions, No Need to Type '.'")
                        print(".txt")
                        print(".docx")
                        print(".pages")
                        
                        ext2 = input("Enter .Extension, don't need to enter the period: " )
                        try:
                            file = open(head2 + "." + ext2, "r")
                        
                            rulez = file.readlines()
                            print("Enter Document Text, Type '///' to end writing: ")
                            for i in rulez:
                                print(i)
                            file = open(head2 + "." + ext2, "w")
                            break
                        except FileNotFoundError as e:
                            print(e)
                            continue
                    content = "\n".join(rulez) + "\n"
                    if head2 == "quit" or head2 == "Quit":
                        continue
                    while True:
                        
                        line = input()
                        if "///" in line:
                            break
                        content += line + "\n"
                    file.write(content)
                    file.close()
                    print(". . . . . .File Saved!")
                    continue
                elif choice == 4:
                    print("Exiting App . . . . .")
                    break
            print(rose)
            anyelse()
            
            continue
#Open App
        if todo == "app" or todo == "App" or todo == "Open" or todo == "open" or todo == "Open App" or todo == "open app":
            print("What App Would you like to run " + name + "?")
            
            apprun = input()
            import os
            import subprocess

            subprocess.run(["/usr/bin/open", "-a" + str(apprun)])
            os.system("open -a " + str(apprun))
            anyelse()
            
            continue
#Close App
        if todo == "Kill App" or todo == "kill app" or todo == "kill" or todo == "Kill" or todo == "Close" or todo == "close":
            print("What app would you like to close " + name + "?")
            
            apprun = input()
            import os

            os.system("pkill " + str(apprun))
            anyelse()
            
            continue
#Secret 5
        if todo == "Happy Birthday" or todo == "happy birthday":
            import time
            os.system( "say Happy Birthday to You" )
            print("Happy Birthday to you!")
            os.system( "say Happy Birthday to You" )
            print("Happy Birthday to you!")
            os.system( "say Happy Birthday to" + name )
            print("Happy Birthday to " + name + "!")
            os.system( "say Happy Birthday to You" )
            print("Happy Birthday to you!")
            time.sleep(1)
            anyelse()
            
            continue
#Calendar
        if todo == "Cal" or todo == "cal" or todo == "rcal" or todo == "Rcal" or todo == "Calendar" or todo == "calendar" or todo == "Calender" or todo == "calender":
            import calendar  
            from datetime import date
            today = date.today()
            while True:
                print("© Blake Gouthro | Rosewell Software | Calendar | Rosewell OS | V1.3 | 2021 - " + str(today.year) + " ©")
                print("Welcome to the Rosewell Calendar Program, Input Current Calander and Select from the Options Below")
                print("NOTE: for a Calendar File to open, it must be named 'Rcal.txt'")
                print("Type '///' to end writing text when making calendar text")
                
                yy = int(input("Enter Year Digits (yyyy): " ))
                
                mm = int(input("Enter Month Digits (mm): " ))
                print(calendar.month(yy,mm))
                print(" ")
                print(today)
                print(" ")
                
                while True:
                    print(' ')
                    print('Main Menu')
                    print("[1] New Calendar")
                    print("[2] Open Saved Calendar")
                    print('[3] Manual')
                    print("[4] Quit")
                    try:
                        
                        choice = int(input("Enter a Number: " ))
                        break
                    except Exception:
                        print("Choice not found, Try Again?")
                if choice == 1:
                    head = "Rcal"
                    file = open(head + ".txt", "w")
                    content = ""
                    print("Enter Calender Text: ")
                    while True:
                        
                        line = input()
                        if "///" in line:
                            break
                        content += line + "\n"
                    file.write(str(calendar.month(yy,mm)))
                    file.write(content)
                    file.close()
                    print(". . . . . .File Saved!")
                elif choice == 3:
                  print('''-----Calendar App Manual-----
    The Calendar app is a very Basic Calendar app for Rosewell OS.
- New Calendar. The App will automatically name the Calendar File; "Rcal.txt". It will then Print the current Calendar and then let you write any notrs you want.
- Open Calendar. This Option will open the existing "Rcal.txt" file. It will always save the new calendar to the txt file. Then allow you to take some notes.''')
                  print(' ')
                  continue
                elif choice == 2:
                    while True:
                        head2 = "Rcal"
                        try:
                            file = open(head2 + ".txt", "r")
                                            
                            rulez = file.readlines()
                            print("Enter Document Text: ")
                            for i in rulez:
                                print(i)
                            file = open(head2 + ".txt", "w")
                            break
                        except FileNotFoundError as e:
                            print(e)
                            continue
                    content = "\n".join(rulez) + "\n"
                    while True:
                        
                        line = input()
                        if "///" in line:
                            break
                        content += line + "\n"
                        file.write(content)
                        file.write(str(calendar.month(yy,mm)))
                        file.close()
                        print(". . . . . .File Saved!")
                        break
                    continue
                elif choice == 4:
                    print("Exiting Calendar . . . . .")
                    print(rose)
                    anyelse()
                    
                    break
            continue
#Game of Sticks
        if todo == "Game of Sticks" or todo == "game of sticks" or todo == "Sticks" or todo == "sticks" or todo == "Stick" or todo == "stick":
            print("© Blake Gouthro | Game Of Sticks | V1.3 | Rosewell Software | 2021 - " + str(today.year))
            import random
            count = 1
            print("Welcome to Game Of Sticks!")
            sticks = input("Enter Sticks amount (if no or 0 sticks is selected, 15 sticks is default): " )
            if sticks == "0" or sticks == "":
                sticks = 15
            sticks = int(sticks)
            print("Sticks:")
            print(sticks)
            print("[1] 1 Player")
            print("[2] 2 Players")
            print("[3] " + name + " Vs. Computer")
            print('[4] Manual')
            print("[5] Quit")
            game = int(input("Select Game Mode[1p/2p/3p/4p/5p] (No need to type 'p'): " ))
            if game == 4:
              print('''-----Game of Sticks Manual-----
    This Game was orginally created as a project for my Computer Programming 12 class.
- 1 Player. You can okay by yourself here. You can remove as little as 1 stick and as much as 3 Sticks.
- 2 Player. In this mode, If you are the last player to remove a stick, you lose! try to have fun and beat the other player.
- User Vs. Computer. In this mode, You have to be the one to beat the cputer before it beats You!''')
              print(' ')
              anyelse()
              continue
            if game == 1:
                print("1 Player")
                print("Sticks:")
                print(sticks)
                while True:
                    remove = int(input("How Many Sticks Would you Like to Remove?[1/2/3]: " ))
                    if remove > 3 or remove < 0:
                        print("Illegal Move, Try Again")
                        print("Sticks:")
                        print(sticks)
                        continue
                    sticks = sticks - remove
                    print("Sticks:")
                    print(sticks)
                    if sticks <= 2:
                        while True:
                            if sticks == 0:
                                print("Thanks for playing Game Of Sticks!")
                                
                                print(rose)
                                anyelse()
                                break
                            if sticks < 0:
                                print("Illegal Move, Try Again")
                                sticks = sticks + rev
                                continue
                            rev = int(input("How Many Sticks Would you Like to Remove?[1/2/3]: " ))
                            if rev == 2 or rev == 1:
                                sticks = sticks - rev
                                print("Sticks:")
                                print(sticks)
                                continue
                            if rev > 2:
                                print("Illegal Move, Try Again")
                                print("Sticks:")
                                print(sticks)
                                continue
                            if sticks == 1:
                                if rev == 1:
                                    sticks = sticks - rev
                                    print("Sticks:")
                                    print(sticks)
                                    continue
                            if rev > 1:
                                print("Illegal Move, Try Again")
                                print("Sticks:")
                                print(sticks)
                                continue
                    if sticks == 0:
                        break
                print("Exiting")
                print(rose)
                anyelse()
                continue
            if game == 2:
                print("2 Player")
                p1 = input("Please enter Player 1 name: " )
                p2 = input("Please enter Player 2 name: " )
                print("Sticks:")
                print(sticks)
                turn = int(input("Who Wants to Go First?[1p/2p] (No Need to type 'p'): " ))
                if turn == 1:
                    count = 1
                if turn == 2:
                    count = 2
                while True:
                    
                    if count % 2 == 0:
                        print(p2 + "'s Turn")
                    if count % 2 == 1:
                        print(p1 + "'s Turn")
                    

                    remove = int(input("How Many Sticks Would you Like to Remove?[1/2/3]: " ))
                    count = count + 1
                    if remove > 3 or remove < 0:
                        print("Illegal Move, Try Again")
                        print("Sticks:")
                        print(sticks)
                        continue
                    sticks = sticks - remove
                    print("Sticks:")
                    print(sticks)
                    if sticks <= 2:
                        while True:
                            if sticks == 0:
                                if count % 2 == 0:
                                    print(p2 + " Wins!")
                                    print("Sorry " + p1 + " You Lose")
                                if count % 2 == 1:
                                    print(p1 + " Wins!")
                                    print("Sorry " + p2 + " You Lose")
                                print("Thanks for playing Game Of Sticks!")
                                print(rose)
                                anyelse()
                                break
                            if sticks < 0:
                                print("Illegal Move, Try Again")
                                sticks = sticks + rev
                                continue
                            if count % 2 == 0:
                                print(p2 + "'s Turn")
                            if count % 2 == 1:
                                print(p1 + "'s Turn")
                            rev = int(input("How Many Sticks Would you Like to Remove?[1/2/3]: " ))
                            count = count + 1
                            if rev == 2 or rev == 1:
                                sticks = sticks - rev
                                print("Sticks:")
                                print(sticks)
                                continue
                            if rev > 2:
                                print("Illegal Move, Try Again")
                                print("Sticks:")
                                print(sticks)
                                continue
                            if sticks == 1:
                                if rev == 1:
                                    sticks = sticks - rev
                                    print("Sticks:")
                                    print(sticks)
                                    continue
                            if rev > 1:
                                print("Illegal Move, Try Again")
                                print("Sticks:")
                                print(sticks)
                                continue
                    if sticks == 0:
                        break
                print("Exiting")
                print(rose)
                anyelse()
                continue
            if game == 3:
                print("Player Vs. Computer")
                user = int(input("Who do you want to go first[1 User/2 Computer]: " ))
                if user == 1:
                    count = 1
                if user == 2:
                    count = 2
                while True:
                    if sticks > 0:
                        if count % 2 == 0:
                            print("Computer's Turn")
                        if count % 2 == 1:
                            print("User's Turn")
                    if count % 2 == 0:
                        if sticks == 0:
                            if count % 2 == 0:
                                print("Computer Wins!")
                                print("Sorry User You Lose")
                                print("Thanks for playing Game Of Sticks!")
                                print(rose)
                                anyelse()
                                break
                            if count % 2 == 1:
                                print("User Wins!")
                                print("Sorry Computer You Lose")
                                print("Thanks for playing Game Of Sticks!")
                                print(rose)
                                anyelse()
                                break

                        if sticks > 2:
                            n = random.randint(1, 3)
                            sticks = sticks - n
                            print("Computer Took Away " + str(n) + " Sticks")
                            print("Sticks:")
                            print(sticks)
                            count = count + 1
                            continue
                        if sticks <= 2:
                            sticks = sticks - 1
                            print("Computer Took Away 1 Sticks")
                            print("Sticks:")
                            print(sticks)
                            count = count + 1
                            continue
                        
                    if count % 2 == 1:
                        if sticks == 0:
                            if count % 2 == 0:
                                print("Computer Wins!")
                                print("Sorry User You Lose")
                                print("Thanks for playing Game Of Sticks!")
                                print(rose)
                                anyelse()                           
                                break
                            if count % 2 == 1:
                                print("User Wins!")
                                print("Sorry Computer You Lose")
                                print("Thanks for playing Game Of Sticks!")
                                print(rose)
                                anyelse()
                                break
                        remove = int(input("How Many Sticks Would you Like to Remove?[1/2/3]: " ))
                        count = count + 1
                        if remove > 3 or remove < 0:
                            print("Illegal Move, Try Again")
                            print("Sticks:")
                            print(sticks)
                            continue
                        sticks = sticks - remove
                        print("Sticks:")
                        print(sticks)
                        continue
            if game == 5:
                print("Exiting")
                print(rose)
                anyelse()
                continue
             
#Chess
        if todo == "Chess" or todo == "chess":
            """CONVENTIONS:
positions are done row-column from the bottom left and are both numbers. This corresponds to the alpha-number system in traditional chess while being computationally useful. they are specified as tuples
"""
            import itertools
            WHITE = "white"
            BLACK = "black"
            from datetime import date
            today = date.today()






            class Game:
                #ive decided since the number of pieces is capped but the type of pieces is not (pawn transformations), I've already coded much of the modularity to support just using a dictionary of pieces
                def __init__(self):
                    self.playersturn = BLACK
                    self.message = "this is where prompts will go"
                    self.gameboard = {}
                    self.placePieces()
                    print("© Blake Gouthro | Chess | V1.1 | Rosewell OS | 2021 - " + str(today.year) + "©")
                    print("Welcome to Chess! Your Chess pieces are on the Rigt Side Automatically type in move to spaces in this format[a7 a6]. the former digit is the position of a piece, and the later digit is the Move to Position. Then you play the right side using the same digit Format. Try to Win and have FUN! You Can Only moce one piece one spot per turn")
                    self.main()

                    
                def placePieces(self):

                    for i in range(0,8):
                        self.gameboard[(i,1)] = Pawn(WHITE,uniDict[WHITE][Pawn],1)
                        self.gameboard[(i,6)] = Pawn(BLACK,uniDict[BLACK][Pawn],-1)
                        
                    placers = [Rook,Knight,Bishop,Queen,King,Bishop,Knight,Rook]
                    
                    for i in range(0,8):
                        self.gameboard[(i,0)] = placers[i](WHITE,uniDict[WHITE][placers[i]])
                        self.gameboard[((7-i),7)] = placers[i](BLACK,uniDict[BLACK][placers[i]])
                    placers.reverse()

                    
                def main(self):
                    
                    while True:
                        self.printBoard()
                        print(self.message)
                        self.message = ""
                        startpos,endpos = self.parseInput()
                        try:
                            target = self.gameboard[startpos]
                        except:
                            self.message = "could not find piece; index probably out of range"
                            target = None
                            
                        if target:
                            print("found "+str(target))
                            if target.Color != self.playersturn:
                                self.message = "you aren't allowed to move that piece this turn"
                                continue
                            if target.isValid(startpos,endpos,target.Color,self.gameboard):
                                self.message = "that is a valid move"
                                self.gameboard[endpos] = self.gameboard[startpos]
                                del self.gameboard[startpos]
                                self.isCheck()
                                if self.playersturn == BLACK:
                                    self.playersturn = WHITE
                                else : self.playersturn = BLACK
                            else : 
                                self.message = "invalid move" + str(target.availableMoves(startpos[0],startpos[1],self.gameboard))
                                print(target.availableMoves(startpos[0],startpos[1],self.gameboard))
                        else : self.message = "there is no piece in that space"
                                
                def isCheck(self):
                    #ascertain where the kings are, check all pieces of opposing color against those kings, then if either get hit, check if its checkmate
                    king = King
                    kingDict = {}
                    pieceDict = {BLACK : [], WHITE : []}
                    for position,piece in self.gameboard.items():
                        if type(piece) == King:
                            kingDict[piece.Color] = position
                        print(piece)
                        pieceDict[piece.Color].append((piece,position))
                    #white
                    if self.canSeeKing(kingDict[WHITE],pieceDict[BLACK]):
                        self.message = "White player is in check"
                    if self.canSeeKing(kingDict[BLACK],pieceDict[WHITE]):
                        self.message = "Black player is in check"
                    
                    
                def canSeeKing(self,kingpos,piecelist):
                    #checks if any pieces in piece list (which is an array of (piece,position) tuples) can see the king in kingpos
                    for piece,position in piecelist:
                        if piece.isValid(position,kingpos,piece.Color,self.gameboard):
                            return True
                            
                def parseInput(self):
                    try:
                        a,b = input().split()
                        a = ((ord(a[0])-97), int(a[1])-1)
                        b = (ord(b[0])-97, int(b[1])-1)
                        print(a,b)
                        return (a,b)
                    except:
                        print("error decoding input. please try again")
                        return((-1,-1),(-1,-1))
                
                """def validateInput(self, *kargs):
                    for arg in kargs:
                        if type(arg[0]) is not type(1) or type(arg[1]) is not type(1):
                            return False
                    return True"""
                    
                def printBoard(self):
                    print("  1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |")
                    for i in range(0,8):
                        print("-"*32)
                        print(chr(i+97),end="|")
                        for j in range(0,8):
                            item = self.gameboard.get((i,j)," ")
                            print(str(item)+' |', end = " ")
                        print()
                    print("-"*32)
                        
                       
                    
                """game class. contains the following members and methods:
                two arrays of pieces for each player
                8x8 piece array with references to these pieces
                a parse function, which turns the input from the user into a list of two tuples denoting start and end points
                a checkmateExists function which checks if either players are in checkmate
                a checkExists function which checks if either players are in check (woah, I just got that nonsequitur)
                a main loop, which takes input, runs it through the parser, asks the piece if the move is valid, and moves the piece if it is. if the move conflicts with another piece, that piece is removed. ischeck(mate) is run, and if there is a checkmate, the game prints a message as to who wins
                """

            class Piece:
                
                def __init__(self,color,name):
                    self.name = name
                    self.position = None
                    self.Color = color
                def isValid(self,startpos,endpos,Color,gameboard):
                    if endpos in self.availableMoves(startpos[0],startpos[1],gameboard, Color = Color):
                        return True
                    return False
                def __repr__(self):
                    return self.name
                
                def __str__(self):
                    return self.name
                
                def availableMoves(self,x,y,gameboard):
                    print("ERROR: no movement for base class")
                    
                def AdNauseum(self,x,y,gameboard, Color, intervals):
                    """repeats the given interval until another piece is run into. 
                    if that piece is not of the same color, that square is added and
                     then the list is returned"""
                    answers = []
                    for xint,yint in intervals:
                        xtemp,ytemp = x+xint,y+yint
                        while self.isInBounds(xtemp,ytemp):
                            #print(str((xtemp,ytemp))+"is in bounds")
                            
                            target = gameboard.get((xtemp,ytemp),None)
                            if target is None: answers.append((xtemp,ytemp))
                            elif target.Color != Color: 
                                answers.append((xtemp,ytemp))
                                break
                            else:
                                break
                            
                            xtemp,ytemp = xtemp + xint,ytemp + yint
                    return answers
                            
                def isInBounds(self,x,y):
                    "checks if a position is on the board"
                    if x >= 0 and x < 8 and y >= 0 and y < 8:
                        return True
                    return False
                
                def noConflict(self,gameboard,initialColor,x,y):
                    "checks if a single position poses no conflict to the rules of chess"
                    if self.isInBounds(x,y) and (((x,y) not in gameboard) or gameboard[(x,y)].Color != initialColor) : return True
                    return False
                    
                    
            chessCardinals = [(1,0),(0,1),(-1,0),(0,-1)]
            chessDiagonals = [(1,1),(-1,1),(1,-1),(-1,-1)]

            def knightList(x,y,int1,int2):
                """sepcifically for the rook, permutes the values needed around a position for noConflict tests"""
                return [(x+int1,y+int2),(x-int1,y+int2),(x+int1,y-int2),(x-int1,y-int2),(x+int2,y+int1),(x-int2,y+int1),(x+int2,y-int1),(x-int2,y-int1)]
            def kingList(x,y):
                return [(x+1,y),(x+1,y+1),(x+1,y-1),(x,y+1),(x,y-1),(x-1,y),(x-1,y+1),(x-1,y-1)]



            class Knight(Piece):
                def availableMoves(self,x,y,gameboard, Color = None):
                    if Color is None : Color = self.Color
                    return [(xx,yy) for xx,yy in knightList(x,y,2,1) if self.noConflict(gameboard, Color, xx, yy)]
                    
            class Rook(Piece):
                def availableMoves(self,x,y,gameboard ,Color = None):
                    if Color is None : Color = self.Color
                    return self.AdNauseum(x, y, gameboard, Color, chessCardinals)
                    
            class Bishop(Piece):
                def availableMoves(self,x,y,gameboard, Color = None):
                    if Color is None : Color = self.Color
                    return self.AdNauseum(x, y, gameboard, Color, chessDiagonals)
                    
            class Queen(Piece):
                def availableMoves(self,x,y,gameboard, Color = None):
                    if Color is None : Color = self.Color
                    return self.AdNauseum(x, y, gameboard, Color, chessCardinals+chessDiagonals)
                    
            class King(Piece):
                def availableMoves(self,x,y,gameboard, Color = None):
                    if Color is None : Color = self.Color
                    return [(xx,yy) for xx,yy in kingList(x,y) if self.noConflict(gameboard, Color, xx, yy)]
                    
            class Pawn(Piece):
                def __init__(self,color,name,direction):
                    self.name = name
                    self.Color = color
                    #of course, the smallest piece is the hardest to code. direction should be either 1 or -1, should be -1 if the pawn is traveling "backwards"
                    self.direction = direction
                def availableMoves(self,x,y,gameboard, Color = None):
                    if Color is None : Color = self.Color
                    answers = []
                    if (x+1,y+self.direction) in gameboard and self.noConflict(gameboard, Color, x+1, y+self.direction) : answers.append((x+1,y+self.direction))
                    if (x-1,y+self.direction) in gameboard and self.noConflict(gameboard, Color, x-1, y+self.direction) : answers.append((x-1,y+self.direction))
                    if (x,y+self.direction) not in gameboard and Color == self.Color : answers.append((x,y+self.direction))# the condition after the and is to make sure the non-capturing movement (the only fucking one in the game) is not used in the calculation of checkmate
                    return answers

            uniDict = {WHITE : {Pawn : "♙", Rook : "♖", Knight : "♘", Bishop : "♗", King : "♔", Queen : "♕" }, BLACK : {Pawn : "♟", Rook : "♜", Knight : "♞", Bishop : "♝", King : "♚", Queen : "♛" }}
                    

                    


            Game()
            anyelse()
            continue
#Weather
        if todo == "weather" or todo == "Weather":

            from bs4 import BeautifulSoup
            import requests
            from datetime import date
            today = date.today()
            weekDays = ["sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday"]

            def weather(city, TF = False):
                city = city.replace(" ", "+")
                res = requests.get(
                    f'https://www.google.com/search?q={city}&oq={city}&aqs=chrome.0.35i39l2j0l4j46j69i60.6128j1j7&sourceid=chrome&ie=UTF-8', headers=headers)
                print("Searching...\n")
                soup = BeautifulSoup(res.text, 'html.parser')
                location = soup.select('#wob_loc')[0].getText().strip()
                time = soup.select('#wob_dts')[0].getText().strip()
                info = soup.select('#wob_dc')[0].getText().strip()
                weather = soup.select('#wob_tm')[0].getText().strip()
                print(location)
                print(time)
                print(info)
                print(weather+"°C")
                if TF:
                    return time

            def week(index):
                return weekDays[index]

            def weekDriver(dayOfWeek):
                length = len(weekDays)
                currently = weekDays.index(dayOfWeek) + 1
                if currently == len(weekDays):
                    currently = 0
                return week(currently)

            print("© Blake Gouthro and JinHo Mo | Weather | V1.2.3 | Rosewell Software | 2021 - " + str(today.year) + " ©")
            print("Use this weather tool to find out the Current Weather for your City. In Degrees")
            while True:

                headers = {
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

                city = input("Enter the Name of City. Enter 'Quit' to quit the app. Enter 'Manual' to see the Manual ->  " )
                if city == 'Manual' or city == 'manual' or city == 'M' or city == 'm':
                  print('''-----Weather App Manual-----
   The Weather App finds you the Current weather four your town. must be connected to wifi to work.
- Type in city name and Province or Territory and the App will output Weather for the current day and the next 2 days.''')
                  print(' ')
                  continue

                if city == "Quit" or city == "quit" or city == "No" or city == "no":
                    print("Exiting Weather App")
                    print(rose)
                    anyelse()
                    break

                try:
                    day = weather(city + " weather", True).split(" ")[0]
                    for i in range(2):
                        print()
                        day = weekDriver(day.lower())
                        weather(city + day + " weather")
                except Exception as e:
                    print("Enter City")
                    continue

                print(" ")
                print("Have a Nice Day:)\n")
                continue
            continue
#Music
        if todo == "Music" or todo == "music":
            while True:
                from datetime import date
                today = date.today()
                music = ""
                music2 = music
                from pygame import mixer  # Load the popular external library
                print(" ")
                print("© Blake Gouthro | Rosewell Music | V1.4.3 | Rosewell Software 2021 - " + str(today.year))
                print(' ')
                print("Rosewell Music app only supports WAV or OGG files")
                music = input("Enter Music Name and extension.[Music must be jn same folder as software to use] If Left Blank then previous name is saved: " )
                while True:
                    music2 = music
                    if music == " ":
                        music = music2
                    print('''[1] Play
[2] Pause
[3] UnPause
[4] Stop
[5] Loop
[6] Add to Queue
[7] Restart
[8] Manual
[9] Quit''')
                    play = input("Enter a Number(To stop playing music, music must be playing): " )
                    if play == '8' or play == 'Eight' or play == 'eight' or play == 'Manual' or play == 'manual' or play == 'M' or play == 'm':
                      print(' ')
                      print('''-----Music App Manual-----
    The Music app is great for listening to music while you are doing something else in Rosewell OS.
- Play. Starts playing the Loaded Music.
- Pause. Pauses the Current Playing Music.
- Unpause. Unpauses the Current Paused Music.
- Stop. Stops Playing the Music.
- Loop. Plays the Currently Loaded Music Forever.
- Add to Queue. Queues and Plays Multiple songs one after the other.
- Restart. Restarts the Music App.''')
                      print(' ')
                      print('Main Menu')
                    if play == '1' or play == 'play' or play == 'Play' or play == 'One' or play == 'one':
                        mixer.init()
                        mixer.music.load(music)
                        mixer.music.play()
                        print('Playing "' + music + '"')
                        print(' ')
                        print('Main Menu')
                        continue
                    if play == '6' or play == 'six' or play == 'Six' or play == 'Queue' or play == 'queue' or play == 'Add To Queue' or play == 'add To Queue' or play == 'Add to Queue' or play == 'Add To queue' or play == 'add to Queue' or play == 'Add to queue' or play == 'add to queue':
                       position = input('Enter File name for next song for Queue: ' )
                       mixer.music.queue(position)
                       print('Music "' + position + '" Has been Added to the Queue!')
                       print(' ')
                       print('Main Menu')
                       continue
                    if play == '2' or play == 'Two' or play == 'two' or play == 'Too' or play == 'too' or play == 'To' or play == 'to' or play == 'Pause' or play == 'pause':
                        mixer.music.pause()
                        print('Music has been Paused')
                        print(' ')
                        print('Main Menu')
                        continue
                    if play == '3' or play == 'Three' or play == 'three' or play == 'Unpause' or play == 'unpause' or play == 'unPause' or play == 'Un Pause' or play == 'UnPause' or play == 'un pause' or play == 'Un pause' or play == 'un Pause':
                        mixer.music.unpause()
                        print('Music has been UnPaused')
                        print(' ')
                        print('Main Menu')
                    if play == '4' or play == 'Four' or play == 'four' or play == 'Stop' or play == 'stop':
                        mixer.music.stop()
                        print('Music has stopped Playing')
                        print(' ')
                        print('Main Menu')
                        continue
                    if play == '5' or play == 'Five' or play == 'five' or play == 'Loop' or play =='loop':
                        mixer.init()
                        mixer.music.load(music)
                        mixer.music.play(-1)
                        print('Music Looped')
                        print(' ')
                        print('Main Menu')
                    if play == '7' or play == 'Seven' or play == 'seven' or play == 'Restart' or play == 'restart':
                        print("Restarting Music App. . . . . ")
                        break
                
                    if play == '9' or play == 'Nine' or play =='nine' or play == 'Quit' or play == 'quit' or play == 'No' or play == 'no' or play == 'N' or play == 'n' or play == 'q' or play == 'Q':
                        print("Exiting Music App. . . . .")
                        print(rose)
                        anyelse()
                        break
                if play == '7' or play == 'Seven' or play == 'seven' or play == 'Restart' or play == 'restart':
                    continue
                if play == '9' or play == 'Nine' or play =='nine' or play == 'Quit' or play == 'quit' or play == 'No' or play == 'no' or play == 'N' or play == 'n' or play == 'q' or play == 'Q':
                    break
            continue
#setup
        if todo == "Setup" or todo == "setup" or todo == "Set up" or todo == "set up":
            import os
            import sys
            import subprocess
            print("© Blake Gouthro | Set Up | V1.2 | Rosewell Software | 2021 - " + str(today.year) + " ©")
            print("Welcome to the Setup app. This App has been Designed mainly for First Time use of Rosewell OS to install any modules that the OS would use")
            while True:
                print('''[1] Install Modules
[2] Check for Modules
[3] Uninstall Modules
[4] Manual
[5] Quit''')
                setup = int(input("Please enter a Number: " ))
                if setup == 4:
                  print('''-----Set Up App Manual-----
    This App will Allow you to Setup up the Modules; "bs4", "pytz", "requests", "pygame", and "pickle-mixin". As well as uninstall and check for them.''')
                  print(' ')
                  print('Main Menu')
                  continue
                if setup == 1:
                    import pip

                    def install(package):
                        if hasattr(pip, 'main'):
                            pip.main(['install', package])
                        else:
                            pip._internal.main(['install', package])
                    install("bs4")
                    install("pytz")
                    install("requests")
                    install("pygame")
                    install("pickle-mixin")

                    
                    print("Modules Installed")
                    print(" ")
                    continue
                if setup == 2:
                    
                    try:
                        import bs4
                        print("bs4 module is installed")
                    except ModuleNotFoundError:
                        print("bs4 module is not installed")

                    try:
                        import pytz
                        print("pytz module is installed")
                    except ModuleNotFoundError:
                        print("pytz module is not installed")
                    try:
                        import requests
                        print("requests module is installed")
                    except ModuleNotFoundError:
                        print("requests module is not installed")
                    try:
                        import pygame
                        print("pygame module is installed")
                    except ModuleNotFoundError:
                        print("pygame module is not installed")
                    try:
                        import pickle
                        print("Pickle-mixin is installed")
                    except ModuleNotFoundError:
                        print("Pickle-mixin is not installed")
                    print(" ")
                    continue
                if setup == 3:
                    import pip
                    def uninstall(package):
                        if hasattr(pip, 'main'):
                            pip.main(['uninstall', package])
                        else:
                            pip._internal.main(['uninstall', package])
                    uninstall("bs4")
                    uninstall("pytz")
                    uninstall("requests")
                    uninstall("pygame")
                    uninstall("pickle-mixin")

                    print("Modules uninstalled")
                    print(" ")
                    continue
                if setup == 5:
                    print("Exiting Setup App")
                    print(rose)
                    anyelse()
                    break
            continue
#Basic
        if todo == "Basic" or todo == "basic" or todo == "Code" or todo == "code":
            print("© Blake Gouthro and JinHo Mo | Rosewell BASIC | V1.3 | Rosewell Software | 2021 - " + str(today.year))
            print("NOT full version of Rosewell BASIC")
            print("Ready")
            save = ""
            def Go(num):
    
                for i in range(num):
                    exec(save)

            def findNum(word):
                for i in word:
                    if i.isdigit():
                        return True
                return False

            def eliminate(word):
                return " ".join(word.split()[1:])
            def imports(dirtory):
                try:
                    import dirtory
                except ModuleNotFoundError:
                    try:
                        exec(open(dirtory).read())
                    except Exception as e:
                        print(e)
            content = ""
            while True:
                line = input()
                if "manual" in line.lower():
                  print('''-----Rosewell OS BASIC Manual
    The Basic OS for everyone!
- GoTo. means repeat.
- Run. Runs the saved code.
- 10 print... The number means it saves to the save variable.
- Basic can load and run Programs.
- Basic can list the stored code.
- Clear. Clears the system memory.
''')
                  print(' ')
                  print('Ready')
                  continue
                if "goto" in line.lower():
                    Go(int(line.split()[-1:][0]))
                    continue
                    
                if findNum(line):
                    save += eliminate(line) + "\n"
                    continue
                    
                if line == "Run" or line == "run":
                    exec(save)
                    continue
                if line == "quit" or line == "Quit" or line == "No" or line == "no":
                    
                    break
                if line == "list" or line == "List":
                    print(save)
                    continue
                if line == "load" or line == "Load":
                    nerd = input("Enter PROGRAM name: " )
                    imports(nerd)
                    print("Ready")

                if line == "clear" or line == "Clear":
                    print("Are You Sure you want to clear the PROGRAM from memory?[y/n]")
                    abc = input()
                    if abc == "Yes" or abc == "yes" or abc == "Y" or abc == "y":
                        save = ""
                        print("Your PROGRAM has been erased from memory!")
                        continue
                    elif abc == "No" or abc == "no" or abc == "N" or abc == "n":
                        save = save
                        print("Your PROGRAM has not been erased from memory!")
                        continue
                        
                           
                else:
                    print("?Syntax Error?")
                    continue
                content += line + "\n"
            print(rose)
            anyelse()
            continue
#Disk Copy
        if todo == "Disk" or todo == "disk" or todo == "Disk Copy" or todo == "disk copy" or todo == "Disk copy" or todo == "disk Copy" or todo == "Copy" or todo == "copy":
            from datetime import date
            import os
            save = ""

            today = date.today()
            print("© Disk Copy | Rosewell OS | V1.2.3 | Blake Gouthro | 2021 - " + str(today.year) + " ©")
            print("Welcome to Disk Copy! Choose your Options Below")
            while True:
                print("[1] Copy File")
                print("[2] Disk Converter")
                print("[3] Delete file")
                print('[4] Manual')
                print("[5] Quit")

                choice = int(input("Enter a number to Continue: " ))
                if choice == 4:
                  print('''-----Disk Copy Manual-----
    Disk Copy can convert, Copy and Delete your Files.
- Copy Files. Allows you to copy files in same folder.
- Disk Converter. Can convert files to another extension file.
- Delete File. Allows you to delete Files.''')
                  print(' ')
                  print('Main Menu')
                if choice == 1:        
                    print("© JinHo Load for Disk Copy | V1.2 | 2021 - " + str(today.year) + " ©")
                    print("To Duplicate file, the file must be in the same folder as Rosewell OS")
                    loading = input("Enter File name to search for(File to copy must be in the same folder as this Program): ") 
                    with open(loading, "r") as file:
                        save = "".join(file.readlines())
                    loader = input("Enter name for Duplicate file: " )
                    print("""Extensions
'.txt'
'.py'
'.docx'
'.pages'
Choose the Extension for the copy""")
                    load = input()
                    file = open(loader + load, "w")
                    file.write(save)
                    file.close()
                    print("Your File has been Saved!")
                    
                    print("Choose from the Options Below")
                    continue
                if choice == 2:
                    loading = input("Enter File name to convert(no extensions): ")
                    cload = input("Enter file extension: " )
                    print("""Extensions
'.txt'
'.py'
'.docx'
'.pages'
Choose the Extension for the copy""")
                    load = input()
                    fileread = open(loading + cload, "r")
                    file = open(loading + load, "w")
                    file.write("".join(fileread.readlines()))
                    fileread.close()
                    file.close()
                    print("File converted!")

                    print("Choose from the Options Below")
                    continue
                if choice == 3:
                    enternam = input("Please enter the name and extension for the file to be deleted. type quit to go back to menu(file must be in same folder): " )
                    if enternam == "Quit" or enternam == "quit" or enternam == "No" or enternam == "no":
                        print("Main Menu")
                        continue
                    else:
                        print("Are you sure you want to delete that file? " )
                        nas = input("[y/n]: " )
                        if nas == "Yes" or nas == "yes" or nas == "Y" or nas == "y":
                            os.remove(enternam)
                            print("File Deleted . . . . .")
                            print("Main Menu")
                            continue
                        if nas == "No" or nas == "no" or nas == "N" or nas == "n":
                            print("Main Menu")
                            continue
                        
                if choice == 5:
                    print("Exiting Disk Copy . . . . . ")
                    print(rose)
                    anyelse()
                    break
            continue
#Rosewell Tetris
        if todo == "Rosewell Tetris" or todo == "rosewell tetris" or todo == "tetris" or todo == "Tetris" or todo == "T" or todo == "t" or todo == "Rosewell tetris" or todo == "rosewell Tetris":
            from datetime import date
            from random import randrange as rand
            import pygame, sys
            from pygame import mixer
            today = date.today()
            print(" ")
            print("© Blake Gouthro | Rosewell Tetris | V1.2 | Rosewell Software | 2021 - " + str(today.year) + " ©")
            print(" ")
            while True:
              print('''[1] Play Tetris
[2] Manual
[3] Quit''')
              tetris = int(input("Please Enter a Number: " ))
              if tetris == 2:
                print('''-----Rosewell Tetris Manual-----
    In Tetris your goal is to clear as many lines as possible using the Falling Puzzle Pieces/Blocks
- Escape. Allows you to quit the App.
- Left Arrow. Allows you to move your falling piece to the left.
- Right Arrow. Allows you to move the falling piece to the Right.
- Up Arrow. Rotates the falling Piece. 
- P. Will Pause the Game.
- Space. Will start the game.
- Enter/Return. Instantly drops the falling Piece.''')
                print(' ')
                print('Main Menu')
              if tetris == 1:
                print('''
[1] Tetris Music A
[2] Tetris Music B
[3] No Tetris Music
[4] Main Menu''')
                print(" ")
                mix = input("Enter a Number Above: " )
                if mix == "1" or mix == "a" or mix == "A" or mix == "one" or mix == "One":
                    mixer.init()
                    mixer.music.load('Game Boy Tetris Music A.ogg')
                    mixer.music.play(-1)
                if mix == "2" or mix == "B" or mix == "b" or mix == "Two" or mix == "two" or mix == "Too" or mix == "too" or mix == "To" or mix == "to":
                    mixer.init()
                    mixer.music.load('Game Boy Tetris Music B.ogg')
                    mixer.music.play(-1)
                if mix == "4" or mix == "D" or mix == "d" or mix == "Four" or mix == "four" or mix == "Menu" or mix == "menu" or mix == "Main Menu" or mix == "Main menu" or mix == "main Menu" or mix == "main menu":
                    print(" ")
                    print("Main Menu")
                    print(" ")
                    continue
                else:
                    
                    pygame.display.set_caption('Rosewell Tetris')
                    # The configuration
                    cell_size = 18
                    cols =      10
                    rows =      22
                    maxfps =    30

                    colors = [
                    (0,   0,   0  ),
                    (255, 85,  85),
                    (100, 200, 115),
                    (120, 108, 245),
                    (255, 140, 50 ),
                    (50,  120, 52 ),
                    (146, 202, 73 ),
                    (150, 161, 218 ),
                    (35,  35,  35) # Helper color for background grid
                    ]

                    # Define the shapes of the single parts
                    tetris_shapes = [
                        [[1, 1, 1],
                         [0, 1, 0]],

                        [[0, 2, 2],
                         [2, 2, 0]],

                        [[3, 3, 0],
                         [0, 3, 3]],

                        [[4, 0, 0],
                         [4, 4, 4]],

                        [[0, 0, 5],
                         [5, 5, 5]],

                        [[6, 6, 6, 6]],

                        [[7, 7],
                         [7, 7]]
                    ]

                    def rotate_clockwise(shape):
                        return [
                            [ shape[y][x] for y in range(len(shape)) ]
                            for x in range(len(shape[0]) - 1, -1, -1)
                        ]

                    def check_collision(board, shape, offset):
                        off_x, off_y = offset
                        for cy, row in enumerate(shape):
                            for cx, cell in enumerate(row):
                                try:
                                    if cell and board[ cy + off_y ][ cx + off_x ]:
                                        return True
                                except IndexError:
                                    return True
                        return False

                    def remove_row(board, row):
                        del board[row]
                        return [[0 for i in range(cols)]] + board

                    def join_matrixes(mat1, mat2, mat2_off):
                        off_x, off_y = mat2_off
                        for cy, row in enumerate(mat2):
                            for cx, val in enumerate(row):
                                mat1[cy+off_y-1 ][cx+off_x] += val
                        return mat1

                    def new_board():
                        board = [
                            [ 0 for x in range(cols) ]
                            for y in range(rows)
                        ]
                        board += [[ 1 for x in range(cols)]]
                        return board

                    class TetrisApp(object):
                        def __init__(self):
                            pygame.init()
                            pygame.key.set_repeat(250,25)
                            self.width = cell_size*(cols+6)
                            self.height = cell_size*rows
                            self.rlim = cell_size*cols
                            self.bground_grid = [[ 8 if x%2==y%2 else 0 for x in range(cols)] for y in range(rows)]

                            self.default_font =  pygame.font.Font(
                                pygame.font.get_default_font(), 12)

                            self.screen = pygame.display.set_mode((self.width, self.height))
                            pygame.event.set_blocked(pygame.MOUSEMOTION) # We do not need
                                                                         # mouse movement
                                                                         # events, so we
                                                                         # block them.
                            self.next_stone = tetris_shapes[rand(len(tetris_shapes))]
                            self.init_game()

                        def new_stone(self):
                            self.stone = self.next_stone[:]
                            self.next_stone = tetris_shapes[rand(len(tetris_shapes))]
                            self.stone_x = int(cols / 2 - len(self.stone[0])/2)
                            self.stone_y = 0

                            if check_collision(self.board,
                                               self.stone,
                                               (self.stone_x, self.stone_y)):
                                self.gameover = True

                        def init_game(self):
                            self.board = new_board()
                            self.new_stone()
                            self.level = 1
                            self.score = 0
                            self.lines = 0
                            pygame.time.set_timer(pygame.USEREVENT+1, 1000)

                        def disp_msg(self, msg, topleft):
                            x,y = topleft
                            for line in msg.splitlines():
                                self.screen.blit(
                                    self.default_font.render(
                                        line,
                                        False,
                                        (255,255,255),
                                        (0,0,0)),
                                    (x,y))
                                y+=14

                        def center_msg(self, msg):
                            for i, line in enumerate(msg.splitlines()):
                                msg_image =  self.default_font.render(line, False,
                                    (255,255,255), (0,0,0))

                                msgim_center_x, msgim_center_y = msg_image.get_size()
                                msgim_center_x //= 2
                                msgim_center_y //= 2

                                self.screen.blit(msg_image, (
                                  self.width // 2-msgim_center_x,
                                  self.height // 2-msgim_center_y+i*22))

                        def draw_matrix(self, matrix, offset):
                            off_x, off_y  = offset
                            for y, row in enumerate(matrix):
                                for x, val in enumerate(row):
                                    if val:
                                        pygame.draw.rect(
                                            self.screen,
                                            colors[val],
                                            pygame.Rect(
                                                (off_x+x) *
                                                  cell_size,
                                                (off_y+y) *
                                                  cell_size,
                                                cell_size,
                                                cell_size),0)

                        def add_cl_lines(self, n):
                            linescores = [0, 40, 100, 300, 1200]
                            self.lines += n
                            self.score += linescores[n] * self.level
                            if self.lines >= self.level*6:
                                self.level += 1
                                newdelay = 1000-50*(self.level-1)
                                newdelay = 100 if newdelay < 100 else newdelay
                                pygame.time.set_timer(pygame.USEREVENT+1, newdelay)

                        def move(self, delta_x):
                            if not self.gameover and not self.paused:
                                new_x = self.stone_x + delta_x
                                if new_x < 0:
                                    new_x = 0
                                if new_x > cols - len(self.stone[0]):
                                    new_x = cols - len(self.stone[0])
                                if not check_collision(self.board,
                                                       self.stone,
                                                       (new_x, self.stone_y)):
                                    self.stone_x = new_x
                        def quit(self):
                            self.center_msg("Exiting...")
                            pygame.display.update()
                            sys.exit()

                        def drop(self, manual):
                            if not self.gameover and not self.paused:
                                self.score += 1 if manual else 0
                                self.stone_y += 1
                                if check_collision(self.board,
                                                   self.stone,
                                                   (self.stone_x, self.stone_y)):
                                    self.board = join_matrixes(
                                      self.board,
                                      self.stone,
                                      (self.stone_x, self.stone_y))
                                    self.new_stone()
                                    cleared_rows = 0
                                    while True:
                                        for i, row in enumerate(self.board[:-1]):
                                            if 0 not in row:
                                                self.board = remove_row(
                                                  self.board, i)
                                                cleared_rows += 1
                                                break
                                        else:
                                            break
                                    self.add_cl_lines(cleared_rows)
                                    return True
                            return False

                        def insta_drop(self):
                            if not self.gameover and not self.paused:
                                while(not self.drop(True)):
                                    pass

                        def rotate_stone(self):
                            if not self.gameover and not self.paused:
                                new_stone = rotate_clockwise(self.stone)
                                if not check_collision(self.board,
                                                       new_stone,
                                                       (self.stone_x, self.stone_y)):
                                    self.stone = new_stone

                        def toggle_pause(self):
                            self.paused = not self.paused

                        def start_game(self):
                            if self.gameover:
                                self.init_game()
                                self.gameover = False

                        def run(self):
                            key_actions = {
                                'ESCAPE':   self.quit,
                                'LEFT':     lambda:self.move(-1),
                                
                                'RIGHT':    lambda:self.move(+1),
                                
                                'DOWN':     lambda:self.drop(True),
                                
                                'UP':       self.rotate_stone,
                                
                                'p':        self.toggle_pause,
                                'SPACE':    self.start_game,
                                'RETURN':   self.insta_drop,
                                
                            }

                            self.gameover = False
                            self.paused = False

                            dont_burn_my_cpu = pygame.time.Clock()
                            while 1:
                                self.screen.fill((0,0,0))
                                if self.gameover:
                                    self.center_msg("""Game Over!\nYour score: %d
                    Press space to continue""" % self.score)
                                else:
                                    if self.paused:
                                        self.center_msg("Paused")
                                    else:
                                        pygame.draw.line(self.screen,
                                            (255,255,255),
                                            (self.rlim+1, 0),
                                            (self.rlim+1, self.height-1))
                                        self.disp_msg("Next:", (
                                            self.rlim+cell_size,
                                            2))
                                        self.disp_msg("Score: %d\n\nLevel: %d\
                    \nLines: %d" % (self.score, self.level, self.lines),
                                            (self.rlim+cell_size, cell_size*5))
                                        self.draw_matrix(self.bground_grid, (0,0))
                                        self.draw_matrix(self.board, (0,0))
                                        self.draw_matrix(self.stone,
                                            (self.stone_x, self.stone_y))
                                        self.draw_matrix(self.next_stone,
                                            (cols+1,2))
                                pygame.display.update()

                                for event in pygame.event.get():
                                    if event.type == pygame.USEREVENT+1:
                                        self.drop(False)
                                    elif event.type == pygame.QUIT:
                                        self.quit()
                                    elif event.type == pygame.KEYDOWN:
                                        for key in key_actions:
                                            if event.key == eval("pygame.K_"
                                            +key):
                                                key_actions[key]()

                                dont_burn_my_cpu.tick(maxfps)

                    if __name__ == '__main__':
                        App = TetrisApp()
                        App.run()
                
                
                continue
              if tetris == 3:
                print("Exiting Rosewell Tetris")
                anyelse()
                break
            continue
        else:
            print("Sorry " + name + ". I Couldn't find a Program called " + todo + ". Try Again?(Error 27)")
            
            continue
#Another Quit
    if todo == "Quit" or todo == "quit" or todo == "No" or todo == "no":
        break
