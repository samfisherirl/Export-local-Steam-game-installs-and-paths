import VParse as V
import os.path
import shutil
import json
import time

import subprocess


#################################################
# need to find proper global declaration of paths 
#################################################
global dirname  
dirname = os.path.dirname(__file__)
directory = os.path.dirname(__file__) 
#################################################
# need to find proper global declaration of paths
#################################################


appinfo = r'C:\Program Files (x86)\Steam\appcache\appinfo.vdf'

def dirnam():
    # need to find proper global declaration of paths
    return dirname

def main():
    # need to find proper global declaration of paths
    global dirname
    dirname = dirnam()
    list = []
    if V.verify_vdf_location(directory):

        time.sleep(0.2)
        # Calling the cmd4 function in the VParse.py file.
        list = V.call_vdfp(directory)
        gamedic = V.parse_json(list)  # Parsing the list of games and their information.
        
        # Creating a list of objects.
        lib = V.class_constructor(gamedic)
        # A list of all the paths to the games.

        #################################
        # example of calling library methods 
        # validate that path file exists
        try:
            paths = V.callLibrary(lib, directory)
        except: 
            print('\n\nNo paths found. Please locate what should be in: \n===>C:\\Program Files (x86)\\Steam\\config\\libraryfolders.vdf\n\nMove this file adjacent to this app and try again.')
            time.sleep(5)
            return
# Checking if the path to the game is valid.
        lib = V.pathValidator(paths, lib)
        with open('output1.txt', 'w') as f:
            f.write(str(lib))
        # # Writing the data to a file.
        V.writer(lib, directory)
        print('\n\n\nComplete! Open the text file next to this app just generated. Find Output.txt')
        time.sleep(5)
    else:
        print('\n\nClosing now. No appinfo.vdf file found.')
 
 
# # A special variable in Python that gets assigned the name of the module.
if __name__ == "__main__":
    main()
