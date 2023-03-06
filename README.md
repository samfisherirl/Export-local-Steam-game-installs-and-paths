# All-in-one-tool to export steam game paths to csv, no coding or compiling. 
 
 Update: up to 300% faster, now with threading!
 
 

VDF Parser in python (and compiled release with .exe) 
Thank you to @Grub4K at https://github.com/Grub4K/VDFparse/releases

Simply run the exe within the release dir, this application will:
- run powershell to find steam's location and account for weird locations
- grab and deserialize the steam library file
- identify all steam libraries 
- test each game file structure for valid paths and return only valid games with path, folder struct, and formatted name. 

He's done most of the work. I'm just bridging the gap from file structure to merge with full paths, providing other file-formats, and validating paths. 

 requirements:

-python 3.11
 
 ![image](https://user-images.githubusercontent.com/98753696/215885658-6289fb35-681b-4bbd-b0e0-eee2d4a428ad.png)




