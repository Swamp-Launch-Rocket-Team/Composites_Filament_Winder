# Computes required mandrel and carriage positions to execute winds

import math

import generator.definitions as definitions
import generator.winder as winder



def planWind(schedule, machine: winder.Winder):

    # Set location as zero
    machine.zero()
    # Set default feed rate
    machine.setFeedRate(0.5)

    for layer in schedule:
        if (layer.getType() == definitions.WindType.HOOP):
            planHoopWind(layer, machine)
        elif (layer.getType() == definitions.WindType.HELICAL):
            planHelicalWind(layer, machine)
        else:
            print('Error: layer not recognized as a valid type')



    return machine.getGcode()            


def planHoopWind(layer, machine):
    # TODO: implement logic for a hoop wind
    return

def planHelicalWind(layer: definitions.HelicalWind, machine: winder.Winder):
    # Compute important wind information
    mandrelCircumference = math.pi * machine.getDiameter()          # Mandrel diameter, [in]
    windLength = layer.getWindLength()                              # Wind length, [in]
    towWidth = layer.getWidth()                                     # Tow width, [in]
    windAngle = layer.getWindAngle()                                # Wind angle, [deg]
    numStarts = layer.getNumStarts()                                # Number of starts (integer)
    lockAngle = layer.getLockAngle()                                # Lock angle, [deg]
    skipInitialLock = layer.doSkipInitialLock()                     # (boolean)

    # When at an angle, the tow will occupy a greater effective width than its simple width
    # See the documentation for a diagram of this
    # TODO: add to documentation
    effectiveTowWidth = towWidth / math.cos(math.radians(windAngle))

    # Compute the number of circuits that are required to fully cover the mandrel
    # Based on the effective width of the tow
    numCircuits = math.ceil(mandrelCircumference / effectiveTowWidth)

    # How far the mandrel should be rotated for the next pass to avoid wrapping
    # over an existing length of tow
    # In degrees
    passStepAngle = 360 / numCircuits

    # How far the mandrel should rotate for a pass
    # In degrees
    passAngle = (windLength * math.tan(windAngle)) * (360 / mandrelCircumference)

    # How many patterns must be completed to cover the mandrel
    numPatterns = numCircuits / numStarts

    # Confirm pattern number and pass number work together
    if (numCircuits % numStarts != 0):
        print('Invalid combination of number of circuits and number of starts.')
        print('Please use the calculator to compute valid start numbers for your wind angle and tow.')
        print('-------------------------------------------------------------------------------------')
        print('This layer will be skipped.')
        return
    
    # Perform a lock wind
    if (not skipInitialLock):
        machine.moveBy(dx=0, dz=lockAngle)

    # Loop for each pattern
    for i in range(numPatterns):
        # Reset the z axis to prevent very large numbers
        machine.setAxes(x=machine.X, z=0)

        # Loop for each start
        for j in range(numStarts):
            # Insert a comment
            machine.pushComment("Pattern: " + str(i) + "/" + str(numPatterns) + " Circuit: " + str(numStarts) + "/" + str(j))

            # Wind down the mandrel
            machine.moveBy(dx=windLength, dz=passAngle)

            # Perform lock wind
            machine.moveBy(dx=0, dz=(lockAngle - (passAngle % 360)) )

            # Wind up the mandrel
            machine.moveBy(dx=-windLength, dz=passAngle)

            # Perform another lock wind
            machine.moveBy(dx=0, dz=(lockAngle - (passAngle % 360)) )

            # Move to next start position
            machine.moveBy(dx=0, dz=(passStepAngle * numCircuits / numStarts))

        # Move to the next pattern location
        machine.moveBy(dx=0, dx=passStepAngle)

    
