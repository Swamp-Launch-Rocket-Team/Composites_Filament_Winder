# Entry file for filament winder generator
# Authors:
#   Rylan Andrews, 2024-2025 Spaceport Composites Lead

import helper

import winder
import definitions


def main():
    # Welcome message
    print("=================================================================")
    print("| Welcome to the Swamp Launch Filament Winder Gcode Generator   |")
    print("| Please enter a command, or type 'help' for a list of commands |")
    print("=================================================================")

    # Take user input until quit
    userInput = ""
    quit = False
    while (not quit):

        userInput = input()

        # Command tree
        if (userInput == "help"):
            helper.printHelpMenu()

        elif (userInput == "load"):
            print("load selected")
            # TODO: implement load ASSIGNED TO ABEER

        elif (userInput == "loadg"):
            print("loadg selected")
            # TODO: implement loadg

        elif (userInput == "generate"):
            print("generate selected")
            # TODO: implement generate

        elif (userInput == "plot"):
            print("plot selected")
            # TODO: implement plot

        elif (userInput == "write"):
            print("write selected")
            # TODO: implement write

        elif (userInput == "calculator"):
            helper.calculator()

        elif (userInput == "quit"):
            confirmation = input("Are you sure you want to quit? Any unsaved data will be lost. (y/n) ")
            if (confirmation == "y"):
                quit = True
        

# Actually call main function
main()

