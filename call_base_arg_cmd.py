import VParse as V
import os.path
import shutil
import json
import time

import subprocess
directory = os.path.dirname(__file__)

appinfo = r'C:\Program Files (x86)\Steam\appcache\appinfo.vdf'


class Library():
    # profile = data['Datasets'][400]['Data']['appinfo']
    def __init__(self, exe, dir, path, name):
        self.exe = exe
        self.name = name
        self.dir = dir
        self.path = path
        
def main():
    
    list = []
    V.moveV(directory)
    time.sleep(0.5)
    list = V.cmd4(directory)
    V.parse(list)
# f'{VDFexe} {appinfo} --pretty >output.json'
# 
# # A special variable in Python that gets assigned the name of the module.
if __name__ == "__main__":
    main()
    
