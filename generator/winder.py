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

        self.X = 0
        self.Z = 0

        self.gcode = []

    def loadMachineConfig():
        # TODO: load machine information from config file

        return [mandrelDiameter, mandrelLength, xLimit]
    
    def moveHome(self):
        self.gcode.append("G28")


    # Set the axes to zero
    def zero(self):
        self.setAxes(0, 0)


    # Set the axes to the specified X and Z value
    def setAxes(self, x, z) -> None:
        command = "G92 X" + str(round(x, 3)) + " Z" + str(round(z, 3))
        self.gcode.append(command)


    # Actuates each axis by the specified amount
    def moveBy(self, dx, dz) -> None:
        self.X = self.X + dx
        self.Z = self.Z + dz

        command = "G01 X" + str(round(self.X, 3)) + " Z" + str(round(self.Z, 3))
        self.gcode.append(command)

    # Moves to the specified location
    def moveTo(self, x, z) -> None:
        self.X = x
        self.Z = z

        command = "G01 X" + str(round(self.X, 3)) + " Z" + str(round(self.Z, 3))
        self.gcode.append(command)
    
    def pushComment(self, comment):
        self.gcode.append("(" + comment + ")")
    
    def getProperties(self):
        return {'diameter': self.mandrelDiameter,
                'length': self.mandrelLength,
                'xLimit': self.xLimit}
    
    def getGcode(self):
        return self.gcode
    
    def getDiameter(self) -> float:
        return self.mandrelDiameter