import os
from sys import platform

def exitapp():
    if platform == "win32":
        os.system("cls")
    else:
        os.system("clear")
    exit()
