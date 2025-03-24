# Helper functions for top-level functionality

import math

import winder


def printHelpMenu():
    # Prints the help menu
    
    print("=================================================================")
    print("Available commands:")
    print(" load - load a wind file")
    print(" loadg - load a gcode file")
    print(" generate - generate gcode from a wind file")
    print(" plot - plot a gcode file")
    print(" write - save a gcode file")
    print(" calculator - run wind parameter utility")
    print(" quit - terminate this session")
    print("=================================================================")


# Loads the wind file that specifies the layup schedule
def loadWindFile():
    # TODO: implement load wind file helper function

    return [schedule, towParameters, defaultFeedRate]

def generateWind(schedule, towParameters, defaultFeedRate):
    machine = winder.Winder()

def calculator():
    print("===============================================================================================")
    print("This calculator utility will compute valid wind settings for a given tow width and wind angle.")
    print("Note: units must match if not specified.")
    print("-----------------------------------------------------------------------------------------------")

    mandrelDiameter = float(input("Mandrel diameter: "))
    towWidth = float(input("Tow width: "))
    windAngle = float(input("Wind angle [deg]: "))

    mandrelCircumference = math.pi * mandrelDiameter
    effectiveTowWidth = towWidth / math.cos(math.radians(windAngle))
    numCircuits = math.ceil(mandrelCircumference / effectiveTowWidth)

    print("-----------------------------------------------------------------------------------------------")
    print("Number of circuits: " + str(numCircuits))
    print("Valid start position quantities:")

    for i in range(1, numCircuits+1):
        if (numCircuits % i == 0):
            print("     " + str(i))

    print("===============================================================================================")


