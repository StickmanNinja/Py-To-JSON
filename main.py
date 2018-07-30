# Made required imports
import json
import types


# This function figures out what type of value x is
def varType(x):
    if type(x) == list or type(x) == tuple:
        return "list" #For practical purposes, tuples are lists.
    if type(x) == str
        return "string"
    if type(x) == int or type(x) == float:
        return "number"
    else:
        return "unknown"

class Convert:
    # This is a reference to the class itself, allowing me to use self.AddName() and so on.
    def __init__(self):
        # This is the most important variable. It stores the JSON string.
        self.var = ""
