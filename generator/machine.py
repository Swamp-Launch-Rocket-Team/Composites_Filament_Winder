# Folder that simulates the winder
# Generates gcode commands from coordinates and compiles gcode commands


class Machine():

    def __init__(self, mandrelDiameter, xLimit):
        self.mandrelDiameter = mandrelDiameter
        self.xLimit = xLimit

    def move(x, y):
        # Stuff here
        return