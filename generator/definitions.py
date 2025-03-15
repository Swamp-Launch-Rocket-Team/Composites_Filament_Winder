from enum import Enum

# Wind type can be used to identify what kind of wind something is
class WindType(Enum):
    HOOP = 1
    HELICAL = 2
    # Add further wind types as needed


# All winds inherit from ply so that they can be stored in one list, but information specific to a hoop vs helical wind can be extracted.

class Ply():

    def __init__(self, windType):
        # Specify either a hoop or helical wind
        self.windType = windType


class HoopWind(Ply):

    def __init__(self, isSinglePass):
        super().__init__(windType=WindType.HOOP)

        # Specify if this should be a single pass, as in the case of taping
        self.isSinglePass = isSinglePass


class HelicalWind(Ply):
    
    def __init__(self, windAngle, numStarts, skipIndex, lockAngle, leadInLength, leadOutLength, skipInitialLock):
        super().__init__(windType=WindType.HELICAL)

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
        

