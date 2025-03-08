# loader class opens a file selection dialog for any json/wind file and converts it into a nested python object so you can access json fields using dot notation (like loader.someField)
import json  # import json to read json data
import tkinter as tk  # import tkinter to show the file dialog
from tkinter import filedialog  # import filedialog to let user pick a file

class Loader:
    def __init__(self):  # constructor- no arguments needed, always opens a file dialog
        root = tk.Tk()  # create a small tkinter window because thats needed apparantly
        root.withdraw()  # hide the window since we only need the file dialog
        file_path = filedialog.askopenfilename(  # open a file selection window
            title="Select JSON/Wind file",  # title of the file dialog
            filetypes=[("JSON/Wind files", "*.json *.wind"), ("All files", "*.*")]  # allow json/wind files and all files
        )
        with open(file_path, 'r') as f: data = json.load(f)  # open file, read it, and convert json into a dictionary
        obj = self._to_obj(data)  # convert the dictionary into an object for the dot notation access thingy
        self.__dict__.update(obj.__dict__)  # copy the attributes from the converted object into this one

    def _to_obj(self, data):  # helper method to convert dictionaries and lists into objects
        if isinstance(data, dict):  # if data is a dictionary
            obj = type('Obj', (), {})()  # create an empty object
            for k, v in data.items(): setattr(obj, k, self._to_obj(v))  # convert each key-value and set it as an attribute
            return obj  # return the converted object
        elif isinstance(data, list): return [self._to_obj(item) for item in data]  # convert each item in the list if it's a dictionary
        else: return data  # if it's not a dictionary or list, return it as is

#examples
loader = Loader()  # opens a file dialog, loads the selected json/wind file
print(loader.towParameters.width)  # prints the 'width' field inside 'towParameters'
print(loader.defaultFeedRate)  # prints the 'defaultFeedRate' field
print(loader.layers[0].windType)  # prints the 'windType' of the first layer
print(loader.layers[1].windAngle)  # prints the 'windAngle' of the second layer



#i still dont get why we need the class stuff for this, if all we want to do is take a json and use its contents cant we just turn it into a basic python dictionary?