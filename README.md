# All-in-one-tool to export steam libraries, no coding or compiling. 
 
 Update v1 release. Locates steam library folder, paths, and everything without command line. Exports to CSV and TXT.
 

https://streamable.com/jv5e2l
VDF Parser in python (and compiled release with .exe) 
Thank you to @Grub4K at https://github.com/Grub4K/VDFparse/releases

He's done most of the work. I'm just bridging the gap from file structure to merge with full paths, providing other file-formats, and validating paths. 

need to add requirements and more details but this is done with: 

-python 3.10 

need to remove duplicates, it does identify correct paths with some missing. Registry search being added.

-update: it currently includes duplicates ~~and a bad delimiter~~, this will be fixed. 
![image](https://user-images.githubusercontent.com/98753696/210921205-e4ccffc0-4df7-40a4-906f-fd43ec175487.png)

