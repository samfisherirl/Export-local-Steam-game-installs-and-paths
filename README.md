# VDF Steam Library Exporter with Paths
VDF Parser in python (and compiled release with .exe) 
Thank you to @Grub4K at https://github.com/Grub4K/VDFparse/releases
He's done most of the work. I'm just bridging the gap from json to human speak, merging libraries and validating paths. 

adding requirements and more details but this is done with: 

-python 3.10

issues: 
 need to test for alternate paths - right now this release requires standard steam install paths, if your library isnt at the below path, it will throw an error. this will be fixed today.
'C:\\Program Files (x86)\\Steam\\config\\libraryfolders.vdf'
