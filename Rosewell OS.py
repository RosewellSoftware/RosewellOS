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
rose = "© Blake Gouthro | Rosewell OS V1.4.3 | Rosewell Software | Nov. 9th 2021 - " + str(today.year) + " | Today's Date = " + str(today) + " ©"
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
            print('ShotPut - Opens a new ShotPut game session')
            print('BASIC Demo - Opens the Rosewell BASIC DEMO')
            print('Solitare - Opens a New Game of Solitare')
            print("Error (27) means you have either types a word incorrectly or the command for that word doesn't exist")
            print("Restart - Restarts the entire OS")
            anyelse()
            continue


# Solitare
        if todo in ['Solitare','solitare','SOLITARE']:
            print("© Blake Gouthro and Game Creator Danny | Rosewell Solitare | V1.1 | Rosewell Software | 2022 - " + str(today.year) + " ©")

            import random
            BREAK_STRING = "-------------------------------------------------------------------"

            class Card():
                card_to_name = {1:"A", 2:"2", 3:"3", 4:"4", 5:"5", 6:"6", 7:"7",
                                            8:"8", 9:"9", 10:"10", 11:"J", 12:"Q", 13:"K"}

                def __init__(self, value, suit):
                    self.name = self.card_to_name[value]
                    self.suit = suit
                    self.title = "%s%s" % (self.name, self.suit)
                    self.value = value

                def isBelow(self, card):
                    return self.value == (card.value - 1)

                def isOppositeSuit(self, card):
                    if self.suit == "club" or self.suit == "spade":
                            return card.suit == "heart" or card.suit == "diam"
                    else:
                            return card.suit == "spade" or card.suit == "club"

                def canAttach(self, card):
                    if card.isBelow(self) and card.isOppositeSuit(self):
                            return True
                    else:
                            return False

                def __str__(self):
                    return self.title

            class Deck():
                unshuffled_deck = [Card(card, suit) for card in range(1, 14) for suit in ["club", "diam", "heart", "spade"]]

                def __init__(self, num_decks=1):
                    self.deck = self.unshuffled_deck * num_decks
                    random.shuffle(self.deck)

                def flip_card(self):
                    return self.deck.pop()

                def deal_cards(self, num_cards):
                    return [self.deck.pop() for x in range(0, num_cards)]

                def __str__(self):
                    return str(self.deck)
                                        
            class Tableau():
                    # Class that keeps track of the seven piles of cards on the Tableau

                    def __init__(self, card_list):
                            self.unflipped = {x: card_list[x] for x in range(7)}
                            self.flipped = {x: [self.unflipped[x].pop()] for x in range(7)}

                    def flip_card(self, col):
                            """ Flips a card under column col on the Tableau """
                            if len(self.unflipped[col]) > 0:
                                    self.flipped[col].append(self.unflipped[col].pop())

                    def pile_length(self):
                            """ Returns the length of the longest pile on the Tableau """
                            return max([len(self.flipped[x]) + len(self.unflipped[x]) for x in range(7)])

                    def addCards(self, cards, column):
                            """ Returns true if cards were successfully added to column on the Tableau. 
                                                Returns false otherwise. """
                            column_cards = self.flipped[column]
                            if len(column_cards) == 0 and cards[0].value == 13:
                                column_cards.extend(cards)
                                return True
                            elif len(column_cards) > 0 and column_cards[-1].canAttach(cards[0]):
                                column_cards.extend(cards)
                                return True
                            else:
                                return False

                    def tableau_to_tableau(self, c1, c2):
                            """ Returns True if any card(s) are successfully moved from c1 to c2 on
                                    the Tableau, returns False otherwise. """
                            c1_cards = self.flipped[c1]

                            for index in range(len(c1_cards)):
                                    if self.addCards(c1_cards[index:], c2):
                                        self.flipped[c1] = c1_cards[0:index]
                                        if index == 0:
                                                self.flip_card(c1)
                                        return True
                            return False

                    def tableau_to_foundation(self, foundation, column):
                            """ Moves a card from the Tableau to the appropriate Foundation pile """
                            column_cards = self.flipped[column]
                            if len(column_cards) == 0:
                                    return False

                            if foundation.addCard(column_cards[-1]):
                                    column_cards.pop()
                                    if len(column_cards) == 0:
                                            self.flip_card(column)
                                    return True
                            else:
                                    return False

                    def waste_to_tableau(self, waste_pile, column):
                            """ Returns True if a card from the Waste pile is succesfully moved to a column
                                    on the Tableau, returns False otherwise. """
                            card = waste_pile.waste[-1]
                            if self.addCards([card], column):
                                    waste_pile.pop_waste_card()
                                    return True
                            else:
                                    return False

            class StockWaste():
                    """ A StockWaste object keeps track of the Stock and Waste piles """

                    def __init__(self, cards):
                            self.deck = cards
                            self.waste = []

                    def stock_to_waste(self):
                            """ Returns True if a card is sucessfully moved from the Stock pile to the
                                    Waste pile, returns False otherwise. """
                            if len(self.deck) + len(self.waste) == 0:
                                    print("There are no more cards in the Stock pile!")
                                    return False

                            if len(self.deck) == 0:
                                    self.waste.reverse()
                                    self.deck = self.waste.copy()
                                    self.waste.clear()

                            self.waste.append(self.deck.pop())
                            return True

                    def pop_waste_card(self):
                            """ Removes a card from the Waste pile. """
                            if len(self.waste) > 0:
                                    return self.waste.pop()

                    def getWaste(self):
                            """ Retrieves the top card of the Waste pile. """
                            if len(self.waste) > 0:
                                    return self.waste[-1]
                            else:
                                    return "empty"

                    def getStock(self):
                            """ Returns a string of the number of cards in the stock. """
                            if len(self.deck) > 0:
                                    return str(len(self.deck)) + " card(s)"
                            else:
                                    return "empty"

            class Foundation():

                    def __init__(self):
                            self.foundation_stacks = {"club":[], "heart":[], "spade":[], "diam":[]}

                    def addCard(self, card):
                            """ Returns True if a card is successfully added to the Foundation,
                                                otherwise, returns False. """
                            stack = self.foundation_stacks[card.suit]
                            if (len(stack) == 0 and card.value == 1) or stack[-1].isBelow(card):
                                    stack.append(card)
                                    return True
                            else:
                                    return False

                    def getTopCard(self, suit):
                            """ Return the top card of a foundation pile. If the pile
                                                is empty, return the letter of the suit."""
                            stack = self.foundation_stacks[suit]
                            if len(stack) == 0:
                                    return suit[0].upper()
                            else:
                                    return self.foundation_stacks[suit][-1]

                    def gameWon(self):
                            """ Returns whether the user has won the game. """
                            for suit, stack in self.foundation_stacks.items():
                                    if len(stack) == 0:
                                            return False
                                    card = stack[-1]
                                    if card.value != 13:
                                            return False
                            return True

            def printValidCommands():
                    """ Provides the list of commands, for when users press 'h' """
                    print("Valid Commands: ")
                    print("\tmv - move card from Stock to Waste")
                    print("\twf - move card from Waste to Foundation")
                    print("\twt #T - move card from Waste to Tableau")
                    print("\ttf #T - move card from Tableau to Foundation")
                    print("\ttt #T1 #T2 - move card from one Tableau column to another")
                    print("\th - help")
                    print("\tq - quit")
                    print("\t*NOTE: Hearts/diamonds are red. Spades/clubs are black.")

            def printTable(tableau, foundation, stock_waste):
                    """ Prints the current status of the table """
                    print(BREAK_STRING)
                    print("Waste \t Stock \t\t\t\t Foundation")
                    print("{}\t{}\t\t{}\t{}\t{}\t{}".format(stock_waste.getWaste(), stock_waste.getStock(), 
                            foundation.getTopCard("club"), foundation.getTopCard("heart"), 
                            foundation.getTopCard("spade"), foundation.getTopCard("diam")))
                    print("\nTableau\n\t1\t2\t3\t4\t5\t6\t7\n")
                                # Print the cards, first printing the unflipped cards, and then the flipped.
                    for x in range(tableau.pile_length()):
                            print_str = ""
                            for col in range(7):
                                    hidden_cards = tableau.unflipped[col]
                                    shown_cards = tableau.flipped[col]
                                    if len(hidden_cards) > x:
                                            print_str += "\tx"
                                    elif len(shown_cards) + len(hidden_cards) > x:
                                            print_str += "\t" + str(shown_cards[x-len(hidden_cards)])
                                    else:
                                            print_str += "\t"
                            print(print_str)
                    print("\n"+BREAK_STRING)

            if __name__ == "__main__":
                d = Deck()
                t = Tableau([d.deal_cards(x) for x in range(1,8)])
                f = Foundation()
                sw = StockWaste(d.deal_cards(24))

                print("\n" + BREAK_STRING)
                            #Opening string
                print("Welcome to Rosewell Solitaire!\n")
                print('Ported to Rosewell OS by Blake Gouthro')
                print("Original game name: Danny's Solitare")
                print(' ')
                            
                printValidCommands()
                printTable(t, f, sw)

                while not f.gameWon():
                    command = input("Enter a command (type 'h' for help): ")
                    command = command.lower().replace(" ", "")
                    if command == "h":
                            printValidCommands()
                    elif command == "q":
                            print("Game exited.")
                            break
                    elif command == "mv":
                            if sw.stock_to_waste():
                                    printTable(t, f, sw)
                    elif command == "wf":
                            if f.addCard(sw.getWaste()):
                                    sw.pop_waste_card()
                                    printTable(t, f, sw)
                            else:
                                    print("Error! No card could be moved from the Waste to the Foundation.")
                    elif "wt" in command and len(command) == 3:
                            col = int(command[-1]) - 1
                            if t.waste_to_tableau(sw, col):
                                    printTable(t, f, sw)
                            else:
                                    print("Error! No card could be moved from the Waste to the Tableau column.")
                    elif "tf" in command and len(command) == 3:
                            col = int(command[-1]) - 1
                            if t.tableau_to_foundation(f, col):
                                    printTable(t, f, sw)
                            else:
                                    print("Error! No card could be moved from the Tableau column to the Foundation.")
                    elif "tt" in command and len(command) == 4:
                            c1, c2 = int(command[-2]) - 1, int(command[-1]) - 1
                            if t.tableau_to_tableau(c1, c2):
                                    printTable(t, f, sw)
                            else:
                                    print("Error! No card could be moved from that Tableau column.")
                    else:
                            print("Sorry, that is not a valid command.")

                if f.gameWon():
                    print("Congratulations! You've won!")

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
            print("20211109 - Rosewell OS Creation Date Secret")
            anyelse()
            continue
#Creation Secret
        if todo == '20211109':
          print('Hello ' + name + '! You have found the November 9th 2021 Secret! The Creation Date of Rosewell OS Happened on this date! Never Forget it JinHo Mo or Blake Gouthro')
          print(' ')
          print('-- Blake Gouthro and CONRAD')
          print(' ')
          print(rose)
          print(' ')
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
#Shot Put
        if todo == "ShotPut" or todo == "shotput" or todo == "Shotput" or todo == "shotPut" or todo == "Shot Put" or todo == "shot put" or todo == "Shot put" or todo == "shot Put" or todo == "SP" or todo == "sp" or todo == "Sp" or todo == "sP" or todo == "S P" or todo == "s p" or todo == "S p" or todo == "s P":

            def rankings():
    
                #Rankings End Screen
                print('''-----Rankings-----
Score        Attempt''')
                print(" ")
                print(str(att1) + "            " + "Attempt 1")
                print(" ")
                print(str(att2) + "            " + "Attempt 2")
                print(" ")
                print(str(att3) + "            " + "Attempt 3")
                print(" ")
                print(str(att1 + att2 + att3) + "            " + "High Score")
                print(" ")
                if att1 > att2 > att3:
                    print(str(att1) + "            " + "Your Highest Attempt")
                if att1 == att2 == att3:
                    print(str(att1) + "            " + "Your Highest Attempt")
                if att1 < att2 > att3:
                    print(str(att2) + "            " + "Your Highest Attempt")
                if att1 > att2 < att3:
                    print(str(att3) + "            " + "Your Highest Attempt")
                if att1 < att2 < att3:
                    print(str(att3) + "            " + "Your Highest Attempt")
                print(" ")
            def dice():
                global n
                n = random.randint(1, 6)
                return n
            def block():
                if n == 1:
                    print (u"\u2680")
                    
                if n == 2:
                    print (u"\u2681")
                    
                if n == 3:
                    print (u"\u2682")
                    
                if n == 4:
                    print (u"\u2683")
                    
                if n == 5:
                    print (u"\u2684")
                    
                if n == 6:
                    print (u"\u2685")

            play = """In this game your objective is to roll 8 Dice and score the total amount of dice you have thrown.
You can score anytime, just make sure you don't land on the 1.
If you land on the 1 your attempt is considered a invalid attempt.
you have 3 attempts to get the highest score you can.
The game will output your highest score.
You can now select Background Music to play in the background. The file must be a '.ogg' file to work.
And you can now save Notes per session in the game."""

            def copyright():
                print("© Blake Gouthro | Shot Put | V1.5.3C | 2021 - " + str(today.year) + " ©")


            print(" ")
            copyright()
            print(" ")

            #Welcome Screen
            print("Welcome to Shot Put! Type '3' to view the instructions on how to play the game")
            print(" ")

            # Menu System
            while True:
                print("Main Menu")
                print(" ")
                print('''[1] Play Game
[2] View Copyright and Update/Patch Notes
[3] View Instructions/Manual
[4] Background Music
[5] Built-in Notes
[6] Quit Program''')
                print(" ")
                macbook = input("Enter a Number to Continue: " )
                
                #View the Copyright Function
                if macbook == "2" or macbook == "Copyright" or macbook == "copyright" or macbook == "C" or macbook == "c" or macbook == "Copy Right" or macbook == "Copy right" or macbook == "copy Right" or macbook == "copy right":
                    print(" ")
                    copyright()

                    #View Patch Notes
                    print(" ")
                    print('''-----Update/Patch Notes-----
Newest Update adds;
--Rephrasing-- Rephrased some words for the user to understand better.
--In Game Score Counter-- Added some in game score counter so the person can keep track of the score
--Moved in game score counter-- Moved the ingame score counter to before the question
--Bug Fix-- Fixed a bug where the game would count the current attempt score as zero
--Version 1.5.2C-- This Version is for Rosewell OS.
Brewing Coffee For Next Update.....''')

                    print(" ")
                    continue

                #Instruction Manual
                if macbook == "3" or macbook == "I" or macbook == "i" or macbook == "Instructions" or macbook == "instructions" or macbook == "Manual" or macbook == "manual" or macbook == "M" or macbook == "m":
                    print(" ")
                    print(play)
                    print(" ")
                    continue
                #20050421 Secret
                if macbook in ['20050421']:
                    copyright()
                    print(" ")
                    print(''' Shot Put was originally created for the purpose of a school project that was later brought into Rosewell OS and/or kept a seperate version.
-----Credits-----
--Blake Gouthro-- Creator of this Version of Shot Put.
--JinHo Mo-- Helped with the creation of Shot Put and is part of the Rosewell Software team devolping Rosewell OS and Rosewell BASIC.
''')
                    continue
                #Secrets Menu
                if macbook in ['secret', 'Secret', 'S', 's', 'Secrets', 'secrets']:
                    print(" ")
                    print('''-----Secret Menu-----
Congratulations User, you have found the Secret Menu. This menu contains a list of all built in secrets.
--Secret-- Opens the Secret Menu.
--20050421-- Opens the Credits Menu.
--Version-- Opens the Shot Put Version History.
            ''')
                    print(" ")
                    continue
                #Version History Secret
                if macbook in ['Version', 'Versions', 'version', 'versions', 'V', 'v']:
                    print('''-----Version History-----
Version 1.1 - The Very First Version
Version 1.2
Version 1.3
version 1.4
version 1.4.3
Version 1.4.4
Version 1.5
Version 1.5.2
Version 1.5.2C - We are Here. Brewing some coffee for the next update.....''')
                    print(" ")
                    continue
                #Main Gameplay
                if macbook == "1" or macbook == "Yes" or macbook == "yes" or macbook == "y" or macbook == "Y" or macbook == "Play" or macbook == "play" or macbook == "P" or macbook == "p":
                    print(" ")


                    #resets turn counter back to zero
                    count = 0

                    while count < 3:
                        print(" ")
                        print("Attempt", count+ 1)
                        print(" ")
                        attempt = []
                        for i in range(8):

                            #dice roll
                            roll = dice()
                            
                            #save the attempts
                            attempt.append(roll)
                            
                            print(roll)
                            block()

                            #detect the invaild roll
                            if roll == 1:
                                print("Invaild Attempt")
                                time.sleep(1)
                                attempt = []
                                scores = 0
                                break
                            #Save the Score counter Variable
                            
                            scores = scores + roll
                            
                            #ask user to save the score or not, but the score can only save once for now
                            print(" ")
                            print("Current Score For Attempt: " + str(scores))
                            user = input("Save your Score for this Attempt?[y/n]")

                            #if the user wants to save, it saves index of the roll
                            if user.lower() == "yes" or user.lower() == "Yes" or user.lower() == "Y" or user.lower() == "y" or user.lower() == "Ok" or user.lower() == "ok":
                                break
                            
                            
                            print(" ")
                        
                        #Calculating Scores for Attempts
                        if count == 0:
                            att1 = sum(attempt)
                            
                        if count == 1:
                            att2 = sum(attempt)

                        if count == 2:
                            att3 = sum(attempt)

                        print(attempt)
                        print("Score This Attempt:")
                        score.append(sum(attempt))
                        print(scores)
                        score[count]
                        print(" ")
                        count += 1
                        scores = 0

                    #Print Rankings
                    time.sleep(1)
                    rankings()
                    time.sleep(1)
                    continue

                #Background Music
                if macbook in ["4", 'Four', 'four', 'Music', 'music', 'M', 'm', 'Background Music', 'background Music', 'Background music', 'background music', 'BGM', 'bGM', 'BGm', 'Bgm', 'bGm', 'bgM', 'bgm', 'BM', 'bM', 'Bm', 'bm']:


                    #Music Modules
                    try:
                        import pygame
                        from pygame import mixer
                    except ModuleNotFoundError as e:
                        print(e)
                        
                    #music menu
                    while True:
                        print(" ")
                        print("Music Menu")
                        print(" ")
                        print('''[1] Play Background Music
[2] Stop Background Music
[3] Main Menu''')
                        print(" ")

                        #Play Background Music
                        l1 = input("Enter a number above: " )
                        if l1 in ['1', 'one', 'One', 'Music', 'music', 'm', 'M', 'Play', 'play', 'P', 'p']:
                            
                            print("Enter Music Name  and extension to use for Background Song[Type 'Menu' to go back to Main Menu]:")
                            #Music Input
                            music = input()

                            if music == "menu" or music == 'Menu' or music == 'M' or music == 'm':
                                
                                continue

                            #Plays Music
                            mixer.init()
                            mixer.music.load(music)

                            #Loops Music
                            mixer.music.play(-1)
                            print(" ")
                            print("Background Music is Playing")
                            print(" ")
                            
                            
                            #Back to Music Menu
                            continue

                        #Stop Background Music
                        if l1 in ['2', 'two', 'Two', 'To', 'to', 'Too', 'too', 'Stop', 'stop', 'S', 's']:

                            #Stops Playing the Music
                            mixer.music.stop() 

                            print(" ")
                            print("Music has stoped Playing")
                            print(" ")
                            continue

                        #Go back to Main Menu
                        if l1 in ['3', 'Three', 'three', 'Quit', 'quit', 'Q', 'q', 'Menu', 'menu', 'M', 'm', 'Main Menu', 'main Menu', 'Main menu', 'main menu']:
                            print(" ")
                            break
                            
                        
                    continue
                
                #Built in Notes for storing info
                if macbook in ['5', 'Five', 'five', 'Notes', 'notes', 'N', 'n']:
                    print(" ")
                    note = ""
                    #Notes Menu
                    while True:
                        
                        print('''-----Notes Menu-----
[1] New/Delete Note
[2] Review Note
[3] Add to/Open Note
[4] Main Menu''')
                        #Notes menu input
                        notes = input("Enter a Number to continue: " )
                        if notes in ['1', 'one', 'One', 'New', 'new', 'n', 'N', 'New Note', 'new Note', 'New note', 'new note']:
                            print(" ")
                            print("Are You Sure?[This Action will Destroy the Previous Note][y/n]")
                            notex = input()
                            #if user doesn't want to delete note
                            if notex in ['no', 'No', 'N', 'n', '2', 'Two', 'two']:
                                print("Note Not Deleted")
                                print(" ")
                                continue
                            if notex in ['Yes', 'yes', 'Y', 'y', '1', 'One', 'one']:
                                print("Noted Has beed Deleted(No Going Back...)")
                                note = ""
                                print("--New Note--")
                                print("Enter Note Contents[1 line]:")
                                note = input()
                                print(" ")
                                print("Saving Note. . . . . ")
                                time.sleep(1)
                                print("Your Note has been saved!")
                                print(" ")
                                continue
                        #Review Note
                        if notes in ['2', 'Two', 'two', 'Review', 'review', 'r', 'R', 'Review Note', 'review Note', 'Review note', 'review note']:
                            print(" ")
                            print("Loading. . . . . ")
                            time.sleep(1)
                            print("--Review Note--")
                            print("Your note Contents:")
                            print(" ")
                            print(note)
                            print(" ")
                            continue
                        #Add to note
                        if notes in ['3', 'Add', 'add', 'A', 'a', 'Edit', 'edit', 'E', 'e', 'Add Note', 'Add note', 'add Note', 'add note', 'Edit Note', 'Edit note', 'edit Note', 'edit note']:
                            print(" ")
                            print("--Edit Note--")
                            print(note)
                            print(" ")
                            print("Enter more Contents for Note[1 line]:")
                            nas = input()
                            note = note + "\n"
                            note = note + nas
                            print(" ")
                            print("Saving Note. . . . . ")
                            time.sleep(1)
                            print("Note Saved!")
                            continue
                    


                        #Main Menu
                        if notes in ['4', 'Main Menu','Main menu', 'main Menu', 'main menu', 'Menu', 'menu', 'M', 'm']:
                            print(" ")
                            break
                    
                            
                    
                #Quit The Program
                if macbook == "6" or macbook == "Quit" or macbook == "quit" or macbook == "Q" or macbook == "q" or macbook == "No" or macbook == "no" or macbook == "n" or macbook == "N":
                    print(" ")
                    print("Thank you for playing Shot Put!")

                    copyright()
                    break
            print(" ")
            print(rose)
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
                    print("Error (27) Name Error")
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
        if todo == "Basic" or todo == "basic" or todo == "BASIC" or todo == "Code" or todo == "code":
            from datetime import date
            import os, sys, time, calendar, datetime
            from time import sleep
            saves = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890' + u"\u2680" + u"\u2681" + u"\u2682" + u"\u2683" + u"\u2684" + u"\u2685" + u"\u2588" + "@&# !" + '"' + "$%'()*+,-./:;>=<?\[]{}^_" + u"\u0060" + "|~" + u"\u00A1" + u"\u00A2" + u"\u00A3" + u"\u00A4" + u"\u00A5" + u"\u00A6" + u"\u00A7" + u"\u00A8" + u"\u00A9" + u"\u00AA" + u"\u00AB" + u"\u00AC" + u"\u00AE" + u"\u00AF" + u"\u00B0" + u"\u00B6" + u"\u00BB" + u"\u00BC" + u"\u00BD" + u"\u00BE" + u"\u00BF" + u"\u00D7" + u"\u00F7" + u"\u2580" + u"\u2581" + u"\u2582" + u"\u2583" + u"\u2584" + u"\u2585" + u"\u2586" + u"\u2587" + u"\u2588" + u"\u2589" + u"\u258A" + u"\u258B" + u"\u258C" + u"\u258D" + u"\u258E" + u"\u258F" + u"\u2590" + u"\u2591" + u"\u2592" + u"\u2593" + u"\u2594" + u"\u2595" + u"\u2596" + u"\u2597" + u"\u2598" + u"\u2599" + u"\u259A" + u"\u259B" + u"\u259C" + u"\u259D" + u"\u259E" + u"\u259F"
            today = date.today()
            save = ""
            note = ''

            def atsciiprint():
              for i in range(157):
                print(saves[i], sep='', end='', flush=True); time.sleep(0.000000000000000001)
            def clearConsole():
                command = 'clear'
                if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
                    command = 'cls'
                os.system(command)
            def cls():
              print('\n' * 100)

            name = ""
            nerd = ""
            load = 'BASIC Memory.prg'
            line = ""
            pokes = ""
            apple = ""
            atscii = dict(
                dice1 = u"\u2680",
                dice2 = u"\u2681",
                dice3 = u"\u2682",
                dice4 = u"\u2683",
                dice5 = u"\u2684",
                dice6 = u"\u2685",
                block = u"\u2588",
                at = u"\u0040",
                And = u'\u0026',
                hashtag = u'\u0023',

                space = u'\u0020',
                exclmark = u'\u0021',
                quotes = u'\u0022',
                dollar = u'\u0024',
                percent = u'\u0025',
                quote = u'\u2019',
                openbracket = u'\u0028',
                closebracket = u'\u0029',
                star = u'\u002A',
                plus = u'\u002B',
                comma = u'\u002C',
                minus = u'\u002D',
                period = u'\u002E',
                forwardslash = u'\u002F',
                zero = u'\u0030',
                one = u'\0031',
                two = u'\0032',
                three = u'\0033',
                four = u'\0034',
                five = u'\0035', 
                six = u'\0036',
                seven = u'\0037',
                eight = u'\0038',
                nine = u'\0039',
                colon = u'\u003a',
                semicolon = u'\u003B',
                lessthan = u'\u003C',
                equal = u'\u003D',
                greaterthan = u'\u003E',
                questionmark = u'\u003F',

                uppera = u'\u0041',
                upperb = u'\u0042',
                upperc = u'\u0043',
                upperd = u'\u0044',
                uppere = u'\u0045',
                upperf = u'\u0046',
                upperg = u'\u0047',
                upperh = u'\u0048',
                upperi = u'\u0049',
                upperj = u'\u004A',
                upperk = u'\u004B',
                upperl = u'\u004C',
                upperm = u'\u004D',
                uppern = u'\u004E',
                uppero = u'\u004F',
                upperp = u'\u0050',
                upperq = u'\u0051',
                upperr = u'\u0052',
                uppers = u'\u0053',
                uppert = u'\u0054',
                upperu = u'\u0055',
                upperv = u'\u0056',
                upperw = u'\u0057',
                upperx = u'\u0058',
                uppery = u'\u0059',
                upperz = u'\u005A',
                sqopen = u'\u005B',
                backslash = u'\u005C',
                sqclose = u'\u005D',
                upaccent = u'\u005E',
                lowline = u'\u005F',
                graveaccent = u'\u0060',
                lowera = u'\u0061',
                lowerb = u'\u0062',
                lowerc = u'\u0063',
                lowerd = u'\u0064',
                lowere = u'\u0065',
                lowerf = u'\u0066',
                lowerg = u'\u0067',
                lowerh = u'\u0068',
                loweri = u'\u0069',
                lowerj = u'\u006A',
                lowerk = u'\u006B',
                lowerl = u'\u006C',
                lowerm = u'\u006D',
                lowern = u'\u006E',
                lowero = u'\u006F',
                lowerp = u'\u0070',
                lowerq = u'\u0071',
                lowerr = u'\u0072',
                lowers = u'\u0073',
                lowert = u'\u0074',
                loweru = u'\u0075',
                lowerv = u'\u0076',
                lowerw = u'\u0077',
                lowerx = u'\u0078',
                lowery = u'\u0079',
                lowerz = u'\u007A',
                cropen = u'\u007B',
                verticalbar = u'\u007C',
                crclose = u'\u007D',
                tilde = u'\u007E',
                inexcelmark = u'\u00A1',
                cent = u'\u00A2',
                pound = u'\u00A3',
                currency = u'\u00A4',
                yen = u'\u00A5',
                brokenbar = u'\u00A6',
                sectionsign = u'\u00A7',
                diaeresis = u'\u00A8',
                copyrights = u'\u00A9',
                femord = u'\u00AA',
                leftquotes = u'\u00AB',
                notsign = u'\u00AC',
                registered = u'\u00AE',
                macron = u'\u00AF',
                degree = u'\u00B0',
                pilcrow = u'\u00B6',
                rightquotes = u'\u00BB',
                onedfour = u'\u00BC',
                onedtwo = u'\u00BD',
                threedfour = u'\u00BE',
                inquestionmark = u'\u00BF',
                multiply = u'\u00D7',
                divide = u'\u00F7',
                upperhalf = u'\u2580',
                loweronedeight = u'\u2581',
                loweronedfour = u'\u2582',
                lowerthreedeight = u'\u2583',
                lowerhalf = u'\u2584',
                lowerfivedeight = u'\u2585',
                lowerthreedfour = u'\u2586',
                lowersevendeight = u'\u2587',
                leftsevendeight = u'\u2589',
                leftthreedfour = u'\u258A',
                leftfivedeight = u'\u258B',
                lefthalf = u'\u258C',
                leftthreedeight = u'\u258D',
                leftonedfour = u'\u258E',
                leftonedeight = u'\u258F',
                righthalf = u'\u2590',
                lightshade = u'\u2591',
                mediumshade = u'\u2592',
                darkshade = u'\u2593',
                upperonedeight = u'\u2594',
                rightonedeight = u'\u2595',
                quadlowerleft = u'\u2596',
                quadlowerright = u'\u2597',
                quadupperleft = u'\u2598',
                quadulpllplr = u'\u2599',
                quadulplr = u'\u259A',
                quadulpurpll = u'\u259B',
                quadulpurplr = u'\u259C',
                quadupperright = u'\u259D',
                quadurpll = u'\u259E',
                quadurpllplr = u'\u259F'
                )
            def Go(num):
                
                for i in range(num):
                    exec(save)

            def repeatchr(num):
                for i in range(num):
                    atsciiprint()
                print(' ')
                print('Ready')
                    
            def findNum(word):
                for i in word:
                    if i.isdigit():
                        return True
                return False



            def poke(word):
                
                try:
                    
                    print(atscii.get(word[0], "No Character to Poke"))
                    
                except Exception as e:
                    print(e) 
            rose = "© Blake Gouthro and JinHo Mo | Rosewell BASIC DEMO | V1.5.4 | Rosewell Software | 2021 - " + str(today.year) + " ©"
            roses = "Today's Date is: " + str(today)

            while True:
              print(rose)
              print(roses)
              print(' ')
              print("Contact Rosewell Software at rosewellsoftware@Gmail.com")
              print("Enough Basic Bytes Free")
              print(' ')
              print("Ready")

              import subprocess, os, sys, random, webbrowser


                          
                         
                      
              content = ""
              while True:
                  line = input()



                  #Load 8
                  if line == 'Load,8' or line == 'load,8' or line == 'load, 8' or line == 'Load, 8' or line == 'l8' or line == 'L8' or line == 'Load*8' or line == 'load*8':
                    programs = '/Volumes/'
                    print(" ")
                    load8 = input("Enter External DISK name. [If Left Blank, it Defaults to UNTITLED. Type 'Exit' to return to Ready Prompt]: " )
                    if load8 in ['Exit', 'exit', 'E', 'e', 'Quit', 'quit', 'Q', 'q']:
                      print(" ")
                      print("Ready")
                      continue
                    elif load8 == '' or load8 == ' ':
                      load8 = 'UNTITLED'

                    programs = programs + load8 + '/'
                    load8s = input("Enter PROGRAM Name including the extension. [ex.'.ext'. type 'Exit to return to Ready Prompt]: " )
                    if load8s in ['Exit', 'exit', 'E', 'e', 'Quit', 'quit', 'Q', 'q']:
                      print(" ")
                      print("Ready")
                      continue
                    programs = programs + load8s

                    print("Loading . . . . .")
                    
                    try:
                      with open(programs, "r") as file:
                        save = "".join(file.readlines())
                      stats = os.stat(programs)
                      time.sleep(1)
                      print('''-----Directory-----
            memory   PROGRAM   ext''')
                      print(stats.st_size, 'Bytes' + '    ' + programs)
                      print(str(sys.getsizeof(save)) + " Bytes" + "     System Memory.prg")
                      print(str(sys.getsizeof(load)) + " Bytes" + '     ' + str(load))
                      print('Back to BASIC')
                      print('Ready')
                    except:
                      print("?Dir Error? - The PROGRAM Either Doesn't Exist, or was Typed in Wrong or, is not in the same Folder.")


                    continue
              #20211109

                  if line == '20211109':
                      print('Hello User! You have found the November 9th 2021 Secret! The Creation Date of Rosewell OS Happened on this date! We are talking about Rosewell OS not Rosewell BASIC. Never Forget it JinHo Mo or Blake Gouthro')
                      print(' ')
                      print('-- Blake Gouthro and CONRAD')
                      print(' ')
                      print("Ready")
                      continue
              #20050421
                  if line == '20050421':
                    print('Hi My name is CONRAD! You Look Familiar. Have we met somewhere? Whta is your name?')
                    names = input()
                    print(" ")
                    print("Welcome " + names + "! This Secret is Famillar because it is from Rosewell OS! Not Rosewell BASIC. Anyways Both Operating Systems are Cool Operating Systems.")
                    print(" ")
                    print(rose)
                    print(" ")
                    print("That is the Rosewell BASIC Copyright line. it is important that all of Blake's OSes have them. Rosewell OS was created on November 9th 2021.")
                    print(" ")
                    print('You can Contact the creator at: rosewellsoftware@Gmail.com')
                    print(' ')
                    print('Brewing Coffee for Next Update.....')
                    print(' ')
                    print('Have a Good day ' + names + '!')
                    print(' ')
                    print('Ready')
                    continue
                      
              #goto
                  if "goto" in line.lower():
                      Go(int(line.split()[-1:][0]))
                      print(" ")
                      print("Ready")
                      continue
              #Repeat chr
                  if line in ['Repeat Character', 'Repeat Chr', 'repeat Character', 'repeat Chr', 'Repeat chr', 'Repeat character', 'repeat character', 'repeat chr', 'RC', 'rC', 'Rc', 'rc']:
                      
                      enterx = input('Enter amount to Repeat Program(Type "Quit" to go to main menu): ')
                      if enterx in ['Quit', 'quit', 'no', 'No', 'Q', 'q', 'N', 'n']:
                          print(' ')
                          print("Ready")
                          continue
                      else:
                        enterx = int(enterx)
                        repeatchr(enterx)
                      
                      continue
              # Poke Characters to screen
                  if "poke" in line.lower():
                      
                      pokes = line.split()[1:]
                      
                      poke(pokes)
                      time.sleep(1)
                      print(" ")
                      print("Ready")
                      
                      
                      
                      continue
              #peek
                  if "peek" in line.lower():
                    print("ord or chr?[1/2]")
                    print("Return ATSCII Value or Printed ATSCII?")
                    peekz = int(input())
                    sub = line.split()[-1]
                    if peekz == 1:
                      
                      for i in sub:
                          print(ord(i), end = "\n\n")
                      print("Ready")
                      
                      continue
                    if peekz == 2:
                      sub = line.split()[-1]
                      for i in sub:
                          print(chr(int(i)), end = "\n\n")
                      print("Ready")

            #FindLine
                  if findNum(line):
                      
                      spaces = ''
                      space = ''
                      varc = ''
                      space = line.split()[0]
                      varc = str(space) + ' '
                      spaces = line.replace(varc, '')

                      save += spaces + "\n"
                      continue

              #Help
                  if line == "Help" or line == "help" or line == 'H' or line == 'HELP' or line == 'Manual' or line == 'manual' or line == 'MANUAL':
                    print('''-----Help Commands-----
GoTo (num) - runs and repeats code (num) amount of times
Help - list all the features of BASIC
Save - Allows you to save BASIC programs to a file
Run - allows you to run BASIC programs
quit - Quits Rosewell BASIC
List - list the PROGRAM saved in memory
Load - loads an external PROGRAM from the Same folder
Load 8 - Loads a program from an External Disk
Clear - Allows you to clear your PROGRAM code from memory
Dir - Lists the PROGRAM Directory
ATSCII - Prints the Built-in ATSCII characters for poke/peek commands
all chr - Prints all of the characters at once
Repeat Chr - can print All Chr PROGRAM if given a number
Poke - Print an ATSCII Character to the Screen
Peek - Return the value of an ATSCII Character
Music - Opens the Music Menu to play Background Music of your Choice
Note - Opens the Note Built in menu
Time/Date/Calendar/Clock - Tells the current time and date
Restart - Restarts Rosewell BASIC
49 Bytes - Means that the SYSTYEM MEMORY or any other BASIC MEMORY is empty.(Don't know why it says 49 for 0)
?Syntax Error? - means something was typed in wrong
?Dir Error? - The PROGRAM Either Doesn't Exist, or was Typed in Wrong or, is not in the same Folder.''')
                    print(" ")
                    print("Ready")
                    continue
              #Secrets
                  if line in ['Secrets', 'secret', 'S', 's']:
                      print('''-----Secrets Menu-----
Rosewell BASIC - Lists Copyright and System Info
20050421 - Rosewell OS Secret
20211109 - Rosewell OS Secret
Happy Birthday - Sings Happy Birthday to You!
Dev - Opens the Credits Secret''')
                      print(" ")
                      print("Ready")
                      continue
                  if line in ['Dev', 'dev', 'D', 'd', 'developer', 'Developer', 'Credits', 'credits', 'Credit', 'credit', 'CREDIT', 'DEV', 'DEVELOPER']:
                    print('''-----Credits-----
Blake Goythro - Rosewell BASIC and Rosewell OS Developer, C.E.O of Rosewell Software, rosewellsoftware@Gmail.com account holder, Programmer, Writer, Graphical Devolper and Head of mangement for Rosewell Software.

JinHo Mo - Rosewell BASIC and Rosewell OS Developer, Writer, Graphical Developer, Programmer, Writer, Graphical Developer, Rosewell Software Team Member.

Beginner's All-Purpose Symbolic Instruction Code or BASIC.
''')
                    print(rose)
                    print(" ")
                    print("Ready")
                    continue
              #List Peek
                  if line == "ListPeek" or line == "listPeek" or line == 'Listpeek' or line == 'listpeek' or line == 'PETSCII' or line == 'petscii' or line == 'PetscII' or line == 'Petscii' or line == 'ATSCII' or line == 'atscii' or line == 'AtscII' or line == 'Atscii':
                      print('''-----List of Builtin ATSCII Characters-----
Built-in ATSCII Characters are based off of Unicode Characters. Useful for Poke and Peek commands.
''')
                      for k, v in atscii.items():
                          print(f"{k} : {v}")
                      print(" ")
                  
                      print("Ready")
                      continue

              #save
                  if line == "Save" or line == "save":
                      print("Would you like to save your program?[y/n]")
                      answer = input()
                      if answer == "No" or answer == "no" or answer == "N" or answer == "n":
                        print("Ready")
                        continue
                      if answer == "Yes" or answer == "yes" or answer == "Y" or answer == "y":
                          print("Enter File name.(the Extension '.py' is not required)")
                          linename = input()
                          file = open(linename + ".py", "w")
                          file.write(save)
                          file.close()
                          print("Saving " + linename + ".py . . . . .")
                          time.sleep(1)
                          print("Your PROGRAM has been saved!")
                          print("Ready")
                          continue
              #run    
                  if line == "Run" or line == "run":
                    try:
                      exec(save)
                      print("Ready")
                      continue
                    except:
                      print('''?Syntax Error? - means something was typed in wrong''')
                      print("Ready")
                      continue
              #Clock/Calendar

                  if line in ['Date', 'date', 'D', 'd', 'Calender', 'calendar', 'C', 'c', 'Time', 'time', 'T', 't', 'Clock', 'clock']:
                    print("Todays Date:")
                    print(today)
                    now = datetime.datetime.now()
                    print(now.strftime("%a ,%d ,%B "))
                    print(" ")
                    yy = today.year
                    mm = today.month
                    print(calendar.month(yy,mm))
                    print(" ")
                    print("Current Time:")
                    current_time = time.strftime("%H:%M:%S", time.localtime())
                    print(current_time)
                    print(" ")
                    print("Ready")
                    continue
              #quit
                  if line == "Exit" or line == "exit" or line == "E" or line == "e" or line == "quit" or line == "Quit" or line == "No" or line == "no" or line == "Goodbye" or line == "goodbye" or line == 'GoodBye' or line == 'goodBye':
                      print("Goodbye")
                      break
              #list        
                  if line == "list" or line == "List":
                      time.sleep(1)
                      print(save)
                      print(" ")
                      print("Ready")
                      continue
              #Rosewell BASIC
                  if line in ['Rosewell', 'rosewell', 'BASIC', 'Basic', 'basic', 'Rosewell BASIC', 'rosewell BASIC', 'Rosewell Basic', 'rosewell Basic', 'Rosewell basic', 'rosewell basic', 'rb', 'Rb', 'rB', 'RB']:
                      print(rose)
                      print('''
--Rosewell BASIC was created to be a Recreation of the older BASIC Operating Systems. This copy isn't as powerful yet but soon it will be.
All files that BASIC can use must be run in the same folder.

Basic Stands for;
Beginner's All-Purpose Symbolic Instruction Code

Hello From Nova Scotia!!
Hello From Canada!!

Brewing Coffee For Next Update.....''')
                      print(" ")
                      print("Ready")
                      continue
              #Background Music
                  if line in ['Music', 'music', 'MUSIC', 'M', 'm', 'BGM', 'bgm', 'BM', 'Bm', 'bM', 'bm', 'Background Music', 'background Music', 'Background music', 'background music']:
                      
                      try:
                          import pygame
                          from pygame import mixer
                      except ModuleNotFoundError as e:
                          print(e)
                          print("Please Install the Pygame Module before using Background Music")
                          continue
                          
                      #music menu
                      while True:
                          print(" ")
                          print("-----Music Menu-----")
                          print(" ")
                          print('''[1] Play Background Music
[2] Stop Background Music
[3] Main Menu''')
                          print(" ")

                          #Play Background Music
                          l1 = input("Enter a number above: " )
                          if l1 in ['1', 'one', 'One', 'Music', 'music', 'm', 'M', 'Play', 'play', 'P', 'p']:
                              
                              print("Enter Music Name  and extension to use for Background Song[Type 'Menu' to go back to Main Menu]:")
                              #Music Input
                              
                              music = input()

                              if music == "menu" or music == 'Menu' or music == 'M' or music == 'm':
                                  
                                  continue

                              #Plays Music
                              try:
                                  
                                  mixer.init()
                                  mixer.music.load(music)
                                  #Loops Music
                                  mixer.music.play(-1)
                                  print(" ")
                                  print("Background Music is Playing")
                                  print(" ")
                                  continue
                              except:
                                  print("?Dir Error? - The PROGRAM Either Doesn't Exist, or was Typed in Wrong or, is not in the same Folder.")
                          
                                  continue


                              
                              
                              
                              

                          #Stop Background Music
                          if l1 in ['2', 'two', 'Two', 'To', 'to', 'Too', 'too', 'Stop', 'stop', 'S', 's']:

                              #Stops Playing the Music
                              mixer.music.stop() 

                              print(" ")
                              print("Music has stoped Playing")
                              print(" ")
                              continue

                          #Go back to Main Menu
                          if l1 in ['3', 'Three', 'three', 'Quit', 'quit', 'Q', 'q', 'Menu', 'menu', 'M', 'm', 'Main Menu', 'main Menu', 'Main menu', 'main menu']:
                              print(" ")
                              break

                              print("Ready")
                              continue
                              
              #Clear Screen
                  if line in ['Clear Screen', 'clear screen', 'Clear screen', 'clearScreen', 'cs', 'CS', 'Cs', 'cS', 'Clear Console', 'clear console', 'Clear console', 'clear Console', 'CC', 'cc', 'Cc', 'cC']:
                      
                        clearConsole()
                        cls()


                        time.sleep(1)
                        print("Console Cleared!")
                        print(" ")
                        print("Ready")
                        continue


              #Restart
                  if line in ['Restart', 'restart', 'RS', 'Rs', 'rS', 'rs']:
                    print(" ")
                    time.sleep(1)
                    print("Restarting Rosewell BASIC . . . . .")
                    break
              #load        
                  if line == "load" or line == "Load" or line == "l" or line == "L" or line == "LOAD":
                      print("Enter PROGRAM Name [Make Sure to add the '.py' extension]:")
                      nerd = input()
                      try:
                          with open(nerd, "r") as file:
                              save = "".join(file.readlines())
                          stats = os.stat(nerd)
                          time.sleep(1)
                          print('''-----Directory-----
memory   PROGRAM   ext''')
                          print(stats.st_size, 'Bytes' + '    ' + nerd)
                          print(str(sys.getsizeof(save)) + " Bytes" + "     System Memory.prg")
                          print(str(sys.getsizeof(load)) + " Bytes" + '     ' + str(load))
                          print('Back to BASIC')
                          print('Ready')
                          continue
                      except:
                          time.sleep(1)
                          print('?Dir Error? The PROGRAM ' + nerd + " Either Doesn't Exist, or was Typed in Wrong, or is not in the same Folder.")
                          
                          print(" ")
                          print("Ready")
                          continue
                      print(" ")
                      print("Ready")
                      continue



              
                    
              #Space
                  if line == "":
                      continue
              #Notes

                  if line in ['Note', 'note', 'Notes', 'notes', 'n', 'N',]:
                    while True:
                                    
                                    print('''-----Notes Menu-----
[1] New/Delete Note
[2] Review Note
[3] Add to/Open Note
[4] Main Menu''')
                                    #Notes menu input
                                    notes = input("Enter a Number to continue: " )
                                    if notes in ['1', 'one', 'One', 'New', 'new', 'n', 'N', 'New Note', 'new Note', 'New note', 'new note']:
                                        print(" ")
                                        print("Are You Sure?[This Action will Destroy the Previous Note][y/n]")
                                        notex = input()
                                        #if user doesn't want to delete note
                                        if notex in ['no', 'No', 'N', 'n', '2', 'Two', 'two']:
                                            print("Note Not Deleted")
                                            print(" ")
                                            continue
                                        if notex in ['Yes', 'yes', 'Y', 'y', '1', 'One', 'one']:
                                            print("Noted Has beed Deleted(No Going Back...)")
                                            note = ""
                                            print("--New Note--")
                                            print("Enter Note Contents[1 line]:")
                                            note = input()
                                            print(" ")
                                            print("Saving Note. . . . . ")
                                            time.sleep(1)
                                            print("Your Note has been saved!")
                                            print(" ")
                                            continue
                                    #Review Note
                                    if notes in ['2', 'Two', 'two', 'Review', 'review', 'r', 'R', 'Review Note', 'review Note', 'Review note', 'review note']:
                                        print(" ")
                                        print("Loading. . . . . ")
                                        time.sleep(1)
                                        print("--Review Note--")
                                        print("Your note Contents:")
                                        print(" ")
                                        print(note)
                                        print(" ")
                                        continue
                                    #Add to note
                                    if notes in ['3', 'Add', 'add', 'A', 'a', 'Edit', 'edit', 'E', 'e', 'Add Note', 'Add note', 'add Note', 'add note', 'Edit Note', 'Edit note', 'edit Note', 'edit note']:
                                        print(" ")
                                        print("--Edit Note--")
                                        print(note)
                                        print(" ")
                                        print("Enter more Contents for Note[1 line]:")
                                        nas = input()
                                        note = note + "\n"
                                        note = note + nas
                                        print(" ")
                                        print("Saving Note. . . . . ")
                                        time.sleep(1)
                                        print("Note Saved!")
                                        continue
                                


                                    #Main Menu
                                    if notes in ['4', 'Main Menu','Main menu', 'main Menu', 'main menu', 'Menu', 'menu', 'M', 'm']:
                                        print(" ")
                                        break
                    print("Ready")
                    continue
              #All chr
                  if line in ['All Chr', 'all chr', 'All chr', 'all Chr']:
                      atsciiprint()
                      print(' ')
                      print('Ready')
                      continue

              #Directory
                  if line == "Dir" or line == "dir" or line == "Directory" or line == "directory":
                      enter = input("Load a file into Dir?[type file name if yes / type quit to exit dir / type no to continue]: " )
                      if  enter == "Quit" or enter == "quit" or enter == "Q" or enter == "q" or enter == 'Exit' or enter == 'exit' or enter == 'E' or enter == 'e':
                        print('Back to BASIC')
                        continue
                      if enter != '' or enter in ['no','No','NO','N','n']:
                        enter = enter
                      else:
                        enter = load
                      print('''-----Directory-----
memory       PROGRAM       ext''')
                      print(str(sys.getsizeof(save)) + " Bytes" + "     SYSTEM Memory.prg")
                      print(str(sys.getsizeof(load)) + " Bytes" + '     ' + str(enter))
                      print('Back to BASIC')
                      continue
              #Clear   
                  if line == "clear" or line == "Clear":
                      print("Are You Sure you want to clear the PROGRAM from memory?[y/n]")
                      abc = input()
                      if abc == "Yes" or abc == "yes" or abc == "Y" or abc == "y":
                          save = ""
                          time.sleep(1)
                          print("Your PROGRAM has been erased from memory!")
                          print("Ready")
                          continue
                      elif abc == "No" or abc == "no" or abc == "N" or abc == "n":
                          save = save
                          print("Your PROGRAM has not been erased from memory!")
                          print("Ready")
                          continue
            #Happy Birthday
                  if line in ['Happy Birthday', 'happy Birthday', 'Happy birthday', 'happy birthday', 'HB', 'Hb', 'hB', 'hb']:
                    print(" ")
                    print("Congratulations! You have found the Happy Birthday Secret!")
                    namex = input("What is your Name user?: " )
                    os.system( "say Happy Birthday to You" )
                    print("Happy Birthday to you!")
                    os.system( "say Happy Birthday to You" )
                    print("Happy Birthday to you!")
                    os.system( "say Happy Birthday to" + namex )
                    print("Happy Birthday to " + namex + "!")
                    os.system( "say Happy Birthday to You" )
                    print("Happy Birthday to you!")
                    time.sleep(1)
                    print(" ")
                    print("Ready")
                    continue
                    
                  
              #Syntax error            
                  else:
                      print("?Syntax Error?")
                      continue
                  content += line + "\n"
              #Restart
              if line in ['Restart', 'restart', 'RS', 'Rs', 'rS', 'rs']:
                continue
              #Quit
              if line == "Exit" or line == "exit" or line == "E" or line == "e" or line == "quit" or line == "Quit" or line == "No" or line == "no" or line == "Goodbye" or line == "goodbye" or line == 'GoodBye' or line == 'goodBye':
                break
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
