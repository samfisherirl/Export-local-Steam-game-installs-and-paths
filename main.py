import VParse as V
import os.path
from os import getcwd
import shutil
import json
import time
import subprocess
import locatesteam
import sql
directory = getcwd()
Steam = locatesteam.main()
print(Steam.appinfo)


def main():
    # need to find proper global declaration of  

    time.sleep(0.2)

    # Convert appinfo file to pseudo json
    list = V.call_vdfp()

    gamedic = V.parse_json(list)  # Parsing the list of games and   their information.

    # Creating a list of objects.
    lib = V.class_constructor(gamedic)

    # A list of all the paths to the games.

    #################################
    # example of calling library methods 
    # validate if  file path exists
    # try:

    paths = V.call_lib(lib, directory)


    # Checking if the path to each game is valid.

    lib = V.path_validation(paths, lib)

    # # Writing the data to a file.
    V.writer(lib, directory)

    sql.loop_insert(lib)

    print('\n\n\nComplete! Open the text file next to this app just generated. Find Output.txt')

    time.sleep(1)

    # with open('outputter.txt', 'w') as f:
    #     f.write(str(gamedic))
    
    return lib


# # A special variable in Python that gets assigned the name of the module.
if __name__ == "__main__":
    main()
