import sys
from cx_Freeze import setup, Executable


build_exe_options = {
    "packages": ["os", "sys"], 
    "excludes": ["tkinter", "pythonnet"] # <-- Include easy_gui
}

base = None
#if sys.platform == "win32":
#    base = "Win32GUI"


setup(  
        name = "main_steamvdf",
        version = "0.1",
        description = "steam_VDF_parser",
        
        #options = {"build_exe": build_exe_options},
        options = { "build_exe": {"include_files": ["VDFP.exe"] } },

        executables = [Executable("main_steamvdf.py", base=base, icon = "C:\\Users\\dower\\Documents\\virtual-reality.ico")])
