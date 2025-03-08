from enum import Enum

# Wind type can be used to identify what kind of wind something is
class WindType(Enum):
    HOOP = 1
    HELICAL = 2
    # Add further wind types as needed


class Ply():

    def __init__(self, windType):
        self.windType: WindType = windType
        # Add other features for a general ply


class HoopWind(Ply):

    def __init__(self, windType):
        super().__init__(windType=windType)
        # Add other features for a hoop wind


# Add a class for a helical wind