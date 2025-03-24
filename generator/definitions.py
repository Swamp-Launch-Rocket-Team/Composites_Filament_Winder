from enum import Enum

# Wind type can be used to identify what kind of wind something is
class WindType(Enum):
    HOOP = 1
    HELICAL = 2
    # Add further wind types as needed


# All winds inherit from ply so that they can be stored in one list, but information specific to a hoop vs helical wind can be extracted.

class Ply():

    def __init__(self, windType, windLength, towWidth, towThickness):
        # Specify either a hoop or helical wind
        self.windType = windType
        self.windLength = windLength
        self.towWidth = towWidth
        self.towThickness = towThickness

    def getType(self):
        return self.windType
    
    def getWindLength(self):
        return self.windLength
    
    def getWidth(self):
        return self.towWidth
    
    def getThickness(self):
        return self.towThickness


class HoopWind(Ply):

    def __init__(self, windLength, towWidth, towThickness, isSinglePass):
        super().__init__(WindType.HOOP, windLength, towWidth, towThickness)

        # Specify if this should be a single pass, as in the case of taping
        self.isSinglePass = isSinglePass


class HelicalWind(Ply):
    
    def __init__(self, windLength, towWidth, towThickness, windAngle, numStarts, skipIndex, lockAngle, leadInLength, leadOutLength, skipInitialLock):
        super().__init__(WindType.HELICAL, windLength, towWidth, towThickness)

        # Angle of the helical wind
        # Defined as the angle between the mandrel axis and the wind tow
        # i.e., a length of tow running straight from one end of the mandrel to the other would have an angle of zero degrees
        self.windAngle = windAngle

        # Each circuit will perform a pass going down the mandrel and coming back. The next pass will not be started immediately adjacent 
        # to the previous pass, and will instead start at a new start position some angle off from the previous start position.
        # Once a pass has been completed at each start position, a "pattern" is completed. Subsequent patterns will be completed
        # to cover the mandrel completely (the number of patterns required is determined by tow width).
        # This parameter determines the number of start positions
        self.numStarts = numStarts

        # The number of start positions to skip to find the next start position
        # Currently unused
        self.skipIndex = skipIndex

        # The angle through which to turn the mandrel at the end of each pass. Usually 720 degrees
        self.lockAngle = lockAngle

        # If some intermediate lead-in or lead-out length is desired, it is specified here
        # Currently unused
        self.leadInLength = leadInLength
        self.leadOutLength = leadOutLength

        # If this helical layer follows a previous helical layer, skip the lock wind at the beginning
        self.skipInitialLock = skipInitialLock


    def getWindAngle(self):
        return self.windAngle


    def getNumStarts(self):
        return self.numStarts


    def getLockAngle(self):
        return self.lockAngle
    

    def doSkipInitialLock(self):
        return self.skipInitialLock
        

