# Entry file for filament winder generator
# Authors:
#   Rylan Andrews, 2024-2025 Spaceport Composites Lead


# Move to a separate file eventually
def printHelpMenu():
    print("===============================================")
    print("Available commands:")
    print(" load - load a wind file")
    print(" loadg - load a gcode file")
    print(" generate - generate gcode from a wind file")
    print(" plot - plot a gcode file")
    print(" write - save a gcode file")
    print(" quit - terminate this session")
    print("===============================================")





# Welcome message
print("Welcome to the Swamp Launch Filament Winder Gcode Generator")
print("Please enter a command, or type 'help' for a list of commands")
print("---")

# Take user input until quit
userInput = ""
while (userInput != "quit"):

    userInput = input()

    # Command tree
    if (userInput == "help"):
        printHelpMenu()

    elif (userInput == "load"):
        print("load selected")
        # TODO: implement load

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



