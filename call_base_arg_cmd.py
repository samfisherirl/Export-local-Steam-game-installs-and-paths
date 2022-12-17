import VParse as V
import os.path
import shutil
import json
import time

import subprocess

directory = os.path.dirname(__file__)

appinfo = r'C:\Program Files (x86)\Steam\appcache\appinfo.vdf'


# class Library():
#     # profile = data['Datasets'][400]['Data']['appinfo']
#     def __init__(self, exe, dir, path, name):
#         self.exe = exe
#         self.name = name
#         self.dir = dir
#         # `self` is a reference to the current instance of the class.
#         self.path = path

def main():
    list = []
    if V.moveV(directory):

        time.sleep(0.2)
        list = V.cmd4(directory)
        gamedic = V.parser(list)  # Parsing the list of games and their information.

        lib = V.constructor(gamedic)
        # A list of all the paths to the games.
        paths = V.callLibrary(lib)
        lib = V.pathValidator(paths, lib)
        with open('output1.txt', 'w') as f:
            f.write(str(lib))
        # # Writing the data to a file.
        V.writer(lib, directory)
        print('\n\n\nComplete! Open the text file next to this app just generated. Find Output.txt')
        time.sleep(5)
    else:
        print('\n\nClosing now. No appinfo.vdf file found.')

    ########last_working#############
    # list = []
    # V.moveV(directory)
    # time.sleep(0.5)
    # list = V.cmd4(directory)
    # gamedic = V.parser(list)
    # val = V.constructor(gamedic)
    # V.writer(gamedic, directory)
    # V.writer(ar)
    ###############################################


# f'{VDFexe} {appinfo} --pretty >output.json'
# 
# # A special variable in Python that gets assigned the name of the module.
if __name__ == "__main__":
    main()
