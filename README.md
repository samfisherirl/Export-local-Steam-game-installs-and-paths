# All-in-one-tool to export steam game paths to csv, no coding or compiling. 

<a href="https://github.com/samfisherirl/Export-local-Steam-game-installs-and-paths/releases/download/v1.5/exe.win-amd64-3.11.7z">_direct download link_</a>
 
 Update: 3/6/23 works with beta, includes threading for improved performance. 
 
 

VDF Parser in python (and compiled release with .exe) 
Thank you to @Grub4K at https://github.com/Grub4K/VDFparse/releases

To use this application, you just need to run the exe file in the release directory. Upon running, the application will perform the following tasks:

- Run PowerShell to locate the Steam application's location, even if it's in an unusual location.
- Retrieve and deserialize the Steam library file.
- Identify all Steam libraries available.
- Test each game file structure to ensure they have valid paths and return only the ones that meet this criteria, along with the corresponding path, folder structure, and formatted name.
- While the original developer has done a signifigant amount of leg work, this script is taking on the task of linking the file structure to complete paths, providing additional file formats, and validating paths.


 requirements:

-python 3.11
 
 ![image](https://user-images.githubusercontent.com/98753696/215885658-6289fb35-681b-4bbd-b0e0-eee2d4a428ad.png)




