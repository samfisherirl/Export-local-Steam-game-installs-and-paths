# All-in-one-tool to export steam libraries, no coding or compiling. 
VDF Parser in python (and compiled release with .exe) 
Thank you to @Grub4K at https://github.com/Grub4K/VDFparse/releases
He's done most of the work. I'm just bridging the gap from json to human speak, merging libraries and validating paths. 

need to add requirements and more details but this is done with: 

-python 3.10

issues: 
 need to test for alternate paths - right now this release requires standard steam install paths, if your library isnt at the below path, it will throw an error. this will be fixed today.
'C:\\Program Files (x86)\\Steam\\config\\libraryfolders.vdf'

need to remove duplicates

-update: it currently includes duplicates but this will be fixed, along with better matching 12/21/22
![image](https://user-images.githubusercontent.com/98753696/208944151-4638e4a8-2ebc-4322-941d-15d962c9e073.png)
