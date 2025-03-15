# Folder that simulates the winder
# Generates gcode commands from coordinates and compiles gcode commands


class Winder():

    def __init__(self, mandrelDiameter, xLimit):
        self.mandrelDiameter: int = mandrelDiameter
        self.xLimit: int = xLimit

    def move(self, x, y):
        # Stuff here
        return
    
    def getProperties(self):
        return {'diameter': self.mandrelDiameter,
                'xLimit': self.xLimit}