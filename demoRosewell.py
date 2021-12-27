from datetime import date
today = date.today()
from clrprint import *
import os
import sys
todo = ""
word = ("© Blake Gouthro | Rosewell OS DEMO | V1.3.4 | Rosewell Software | 2021 - " + str(today.year) + " Current Date = " + str(today) + " ©")
clrprint(word, clr='green')
clrprint("Contact Rosewell Software at rosewellsoftware@Gmail.com", clr='red')
print(" ")
clrprint("Type 'help' in the prompt for a list of things you can ask me. Type '///' in any document field to end writing the document", clr='red')
print(" ")
clrprint("Welcome to the Demo Version of Rosewell OS! My Name is CONRAD, i am here to help you! that was my created purpose.", clr='blue')
clrprint("What is Your Name?", clr='blue')
name = input()
clrprint("Welcome " + name + ". What would you like to do?", clr='blue')
while True:
    todo = input()
#help
    if todo == "Quit" or todo == "quit" or todo == "No" or todo == "no":
        os.system( " say Goodbye " + name )
        clrprint("Goodbye " + name, clr='red')
        clrprint("Thank you for trying out The DEMO  version of Rosewell  OS!", clr='red')
        break
    if todo == "Hello World" or todo == "hello world":
        clrprint("Hello World, " * 5, clr='yellow')
        clrprint("Hello " + name + ". Would You Like To Play A Game?", clr='yellow')
        clrprint("Anything Else " + name + "?", clr='red')
        continue
    if todo == "Help" or todo == "help":
        clrprint('''
Here is the List of Commands
Help - brings up the Help list
Calander - Opens the Calendar App
Open - Opens an external App
Kill - Closes an external App
Note - Lets you save a 1 line note
Review Note - prints your note out
Delete Note - Deletes the note and replaces it with a 0
Search - Opens a Google Search for what you type in
Stick - Opens the Game Of Sticks App
Calculator - Opens the Calculator
Quit - Quits the Demo OS
There will be LOTS more in the Full Release of Rosewell OS''', clr='green')
        clrprint("Anything Else " + name + "?", clr='red')
        continue
#Calculator
    if todo == "Calc" or todo == "calc" or todo == "Calculator" or todo == "calculator":
        clrprint("© Blake Gouthro | Calculator | V1.5.2 | Rosewell Software | Current Date = " + str(today) + " ©", clr='red')
        clrprint("© Welcome to Rosewell Calculator! If you save a calculation to a document, type '///' to end writing", clr='red')
        clrprint("Type equation here to see result. If you want to quit Calculator type '5'", clr='red')


            # This function adds two numbers
        def add(x, y):
            return x + y

                # This function subtracts two numbers


        def subtract(x, y):
            return x - y

                # This function multiplies two numbers


        def multiply(x, y):
            return x * y

                # This function divides two numbers


        def divide(x, y):
            return x / y

        def remainder(x, y):
            return x % y
        clrprint("Select operation.", clr='red')
        clrprint("[1] Add", clr='red')
        clrprint("[2] Subtract", clr='red')
        clrprint("[3] Multiply", clr='red')
        clrprint("[4] Divide", clr='red')
        clrprint("[5] Remainder", clr='red')
        clrprint("[6] Quit", clr='red')

        while True:
                # take input from the user
                
            choice = clrinput("Enter choice(1/2/3/4/5/6): ", clr='red')

                # check if choice is one of the four options
            if choice == '6':
                clrprint("Exiting Calculator App...", clr='red')
                clrprint(word, clr='green')
                clrprint("Anything Else " + name + "?", clr='blue')
                    
                break
            if choice in ('1', '2', '3', '4', '5'):
                    
                num1 = float(clrinput("Enter first number: ", clr='red'))
                    
                num2 = float(clrinput("Enter second number: ", clr='red'))

                if choice == '1':
                    clrprint(num1, "+", num2, "=", add(num1, num2), clr='red')

                elif choice == '2':
                    clrprint(num1, "-", num2, "=", subtract(num1, num2), clr='red')

                elif choice == '3':
                    clrprint(num1, "*", num2, "=", multiply(num1, num2), clr='red')

                elif choice == '4':
                    clrprint(num1, "/", num2, "=", divide(num1, num2), clr='red')
                elif choice == '5':
                    clrprint(num1, "%", num2, "=", remainder(num1, num2), clr='red')
                elif choice == '6':
                    clrprint("Exiting Calculator App...", clr='red')
                    clrprint(wprd, clr='green')
                    clrprint("Anythng Else " + name + "?", clr='blue')
                        
                    break
                    

                        # check if user wants another calculation
                        # break the while loop if answer is no
                    
                printcalc = clrinput("Save to .txt Document?[y/n]: ", clr='red' )
                if printcalc == "yes" or printcalc == "Yes" or printcalc == "Y" or printcalc == "y":
                        
                    newdoc = clrinput("New Document?[y/n]", clr='red')
                    if newdoc == "yes" or newdoc == "Yes" or newdoc == "Y" or newdoc == "y":
                            
                        head = "mathcalc"
                        file = open(head + ".txt", "w")
                        content = ""
                        clrprint("Enter Document Text: ", clr='red')
                        while True:
                            line = input()
                            if "///" in line:
                                break
                            content += line + "\n"
                        file.write(content)
                        file.close()
                        clrprint(". . . . . .File Saved!", clr='red')
                    elif newdoc == "No" or newdoc == "no" or newdoc == "N" or newdoc == "n":
                        while True:
                            head2 = "mathcalc"
                            try:
                                file = open(head2 + ".txt", "r")
                        
                                rulez = file.readlines()
                                clrprint("Enter Document Text: ", clr='red')
                                for i in rulez:
                                    print(i)
                                file = open(head2 + ".txt", "w")
                                break
                            except FileNotFoundError as e:
                                clrprint(e, clr='red')
                                continue
                        content = "\n".join(rulez) + "\n"
                        while True:
                            line = input()
                            if "///" in line:
                                break
                            content += line + "\n"
                        file.write(content)
                        file.close()
                        clrprint(". . . . . .File Saved!", clr='red')
                            
                        continue
                
                next_calculation = clrinput("Let's do next calculation? (yes/no): ", clr='red')
                if next_calculation == "no":
                    clrprint("Anything Else " + name + "?",clr='blue')
                        
                    break
        continue
#Calander
    if todo == "calendar" or todo == "Calander" or todo == "today's date" or todo == "Today's Date" or todo == "date" or todo == "Date":
        import calendar
        yy = int(input("Enter Year: " ))
        mm = int(input("Enter Month: " ))
        print(calendar.month(yy,mm))
        print("Anything Else " + name + "?")
        continue
    if todo == "load" or todo == "Load":
        import sys
        import os

        print("© JinHo Load | Rosewell Software | Rosewell OS | V1.2 | 2021 - " + str(today.year) + " ©")
        loading = input("Enter File name to load: ")
        importProgram(str(loading))
        
        print("Anything Else " + name + "?")
        continue
    if todo == "app" or todo == "App" or todo == "Open" or todo == "open" or todo == "Open App" or todo == "open app":
            print("What App Would you like to run " + name + "?")
            apprun = input()
            import os
            import subprocess

            subprocess.run(["/usr/bin/open", "-a" + str(apprun)])
            os.system("open -a " + str(apprun))
            print("Anything Else " + name + "?")
            continue
    if todo == "Kill App" or todo == "kill app" or todo == "kill" or todo == "Kill" or todo == "Close" or todo == "close":
            print("What app would you like to close " + name + "?")
            apprun = input()
            import os

            os.system("pkill " + str(apprun))
            print("Anything Else " + name + "?")
            continue
    if todo == "Note" or todo == "Write Note" or todo == "Notes" or todo == "notes" or todo == "note" or todo == "write note":
            print("Write your note here and it will be saved. NOTE; The Note will only be saved for the session of the OS currently open")
            note = input()
            print("Saving ... 1% ... 10% ... 25% ... 75& ... 100%")
            print("Your Note Has Been Saved " + name + "!")
            print("Anything Else " + name + "?")
            continue
    if todo == "Show Note" or todo == "show note" or todo == "review" or todo == "Review" or todo == "Review Note" or todo == "review note":
            print(note)
            print("Anything Else " + name + "?")
            continue
    if todo == "Delete Note" or todo == "delete note":
            print("Are You Sure " + name + "?")
            yn = input()
            if yn == "Yes" or yn == "yes" or yn == "y" or yn == "Y":
                note = "0"
                print("Erasing ... 1% ... 10% ... 25% ... 75% ... 100%")
                print("Your Note has been erased")
                print(note)
                print("Anything Else " + name + "?")
                continue
            elif yn == "No" or yn == "no" or yn == "n" or yn == "N":
                note = note
                print(rose)
                print("Anything Else " + name + "?")
                continue
    if todo == "Search" or todo == "search" or todo == "Google Search" or todo == "google search":
            print("What would you like to search on Google " + name + "?")
            gog = input()
            url = "https://www.google.com.tr/search?q={}".format(str(gog))
            webbrowser.open_new_tab(url)
            print(rose)
            print("Anything Else " + name + "?")
            continue
    
#Game of Sticks
    if todo == "Game of Sticks" or todo == "game of sticks" or todo == "Sticks" or todo == "sticks" or todo == "Stick" or todo == "stick":
       print("© Blake Gouthro | Game Of Sticks | V1.2 | Rosewell Software | 2021 - " + str(today.year))
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
       print("[4] Quit")
       game = int(input("Select Game Mode[1p/2p/3p/4p] (No need to type 'p'): " ))
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
                 print("Anything Else " + name + "?")
                 break
               if sticks < 0:
                 print("Illegal Move, Try Again")
                 sticks = sticks + remove
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
               
               print("Anything Else " + name + "?")
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
           if sticks == 0:
             print("Exiting App")
             print("Anything Else " + name +"?")
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
                 print("Anything Else " + name + "?")
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
                
                 print("Anything Else " + name + "?")
                 continue
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
                   print("Anything Else " + name + "?")
                   break
                 if count % 2 == 1:
                   print("User Wins!")
                   print("Sorry Computer You Lose")
                   print("Thanks for playing Game Of Sticks!")
                   
                   print("Anything Else " + name + "?")
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
                                
                   print("Anything Else " + name + "?")                           
                   break
                 if count % 2 == 1:
                   print("User Wins!")
                   print("Sorry Computer You Lose")
                   print("Thanks for playing Game Of Sticks!")
                                
                   print("Anything Else " + name + "?")
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
       if game == 4:
         print("Exiting")
                
         print("Anything Else " + name + "?")
         continue
       continue
    else:
      clrprint("Error (27), that Word You Typed Doesn't Exist, Try Again?", clr='red')
      continue
#Another Quit   
    if todo == "Quit" or todo == "quit" or todo == "No" or todo == "no":
        break
