# Made required imports
import json
import types

# This function figures out what type of value x is
def varType(x):
    if type(x) == list or type(x) == tuple:
        return "list" #For practical purposes, tuples are lists.
    if type(x) == str
        return "string"
    if type(x) == int:
        return "int"

