# no stealing, give credit - pilot87

"""
See readme on github for more info
made by Pilot87
version 0.1
"""
from commands import version, exit, length

import sys
import os

commands = ["help", "exit", "version, ver"]

def waitforinput():
    userInput = str(input("\x1b[38;2;255;255;255m~>$"))
    checkinput(userInput)


def checkinput(inpt):
    checkin = inpt.split()

    if inpt == "version" or inpt == "ver":  # version command
        version.version()
        waitforinput()

    elif inpt == "help":  # help command
        print("list of commands:")
        print(*commands, sep="\n")
        waitforinput()

    elif inpt == "exit":  # exit command
        exit.exitapp()
        waitforinput()

    elif checkin[0] == "len" or checkin[0] == "length":  # length command
        strpass = ""
        for i in range(1, len(checkin)):
            if i == 1:
                strpass = strpass + str(checkin[i])
            else:
                strpass = strpass + " " + str(checkin[i])
        length.length(strpass)
        waitforinput()

    else:
        print('\x1b[38;2;255;0;0mcommand not recognized, run the command "help" for a list of commands')
        waitforinput()


if __name__ == "__main__":
    if sys.platform == "win32":
        os.system("cls")
        print("\x1b[38;2;40;177;249mkill yourself windows faggot")

    if sys.platform == "darwin":
        os.system("clear")
        print("\x1b[38;2;40;177;249mimagine spending thousands of dollars for a pile of shit apple fanboy")

    if sys.platform == "riscos":
        os.system("clear")
        print("\x1b[38;2;40;177;249myoure on an OS that hasnt been updated in over a decade get a fucking life")

    if sys.platform == "atheos":
        os.system("clear")
        print("\x1b[38;2;40;177;249mwhat the fuck are you using?")

    if sys.platform == "freebsd7" or "freebsd8" or "freebsdN" or "openbs6":
        os.system("clear")
        print("\x1b[38;2;40;177;249myoure using bsd? poggers")

    if sys.platform == "linux" or "linux2":
        os.system("clear")
        print("\x1b[38;2;40;177;249myoure using linux? poggers")

    print("\x1b[38;2;255;255;255mcheck the github repo if you need any info")
    waitforinput()
