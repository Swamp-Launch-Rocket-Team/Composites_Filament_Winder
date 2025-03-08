# Folder that simulates the winder
# Generates gcode commands from coordinates and compiles gcode commands


class Machine():

    def __init__(self, mandrelDiameter, xLimit):
        self.mandrelDiameter: int = mandrelDiameter
        self.xLimit: int = xLimit

    def move(x, y):
        # Stuff here
        return