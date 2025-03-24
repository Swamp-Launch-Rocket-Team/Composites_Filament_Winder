# Folder that simulates the winder
# Generates gcode commands from coordinates and compiles gcode commands

# Definitions:
#   - The x-axis will be defined as the carriage motion along the mandrel, in inches
#   - The z-axis will be defined as the rotation of the mandrel, in degrees
#   - The y-axis is currently unused, but could be employed in the future
#   - GRBL does not allow for additional rotational axes. For a future expansion to a four-axis machine,
#     a different firmware will likely be required.


class Winder():

    def __init__(self, defaultFeedrate):
        [self.mandrelDiameter, self.mandrelLength, self.xLimit] = Winder.loadMachineConfig()

        self.defaultFeedrate = defaultFeedrate

        self.gcode = []

    def loadMachineConfig():
        # TODO: load machine information from config file

        return [mandrelDiameter, mandrelLength, xLimit]
    
    def home(self):
        self.gcode.append("G28")

    def zero(self):
        # TODO: figure out how to reset the axes to zero
        self.pushComment("dummy comment")

    def setAxes(self, x, z):
        # TODO: figure out how to set the axes to x and z
        self.pushComment("dummy comment")


    def move(self, x, z):
        # Stuff here
        return
    
    def pushComment(self, comment):
        self.gcode.append("(" + comment + ")")
    
    def getProperties(self):
        return {'diameter': self.mandrelDiameter,
                'length': self.mandrelLength,
                'xLimit': self.xLimit}
    
    def getGcode(self):
        return self.gcode
    
    def getDiameter(self):
        return self.mandrelDiameter