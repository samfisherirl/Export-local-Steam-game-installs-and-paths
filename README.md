# All-in-one-tool to export steam libraries, no coding or compiling. 
 
 Update v1 release. Locates steam library folder, paths, and everything without command line. Exports to CSV and TXT.
 

https://streamable.com/jv5e2l
VDF Parser in python (and compiled release with .exe) 
Thank you to @Grub4K at https://github.com/Grub4K/VDFparse/releases

Simply run the exe within the release dir, this application will:
- run powershell to find steam's location and account for weird locations
- grab and deserialize the steam library file
- identify all steam libraries 
- test each game file structure for valid paths and return only valid games with path, folder struct, and formatted name. 

He's done most of the work. I'm just bridging the gap from file structure to merge with full paths, providing other file-formats, and validating paths. 

 requirements:

-python 3.10 

 ![image](https://user-images.githubusercontent.com/98753696/212842672-507bab4e-ddc5-46dd-824a-f17cee1f71ca.png)


