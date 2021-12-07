# Foundry File Assistant
[Download the Latest Release Executable](https://github.com/GFBryson/FoundryFileAssistant/releases/latest/download/FoundryFileAssistant.exe)

[View the Latest Release Notes](https://github.com/GFBryson/FoundryFileAssistant/releases/latest)
## Overview
The purpose of this project is to provide a simple way to help users of FoundryVTT clean and optimise files they wish to import to or use with the FoundryVTT system.

The project was born out of an error that happened when a `.json` scene file for import would have an image stored in it as a 64bit string. THis string being much too large would then lag/break the world because the image file was not properly handled by FoundryVTT when it was imported. *(Specifically this was found by users of Dungeon Alchemist who's maps would break their worlds)*

## Functions
### Image Stripping
**FFA** can read in a scene `.json` file and take out the image string, saving it to a place of the users choosing.

If the user stores the image within their FoundryVTT file system the json will receive a path to that image so it will automatically load in when the user imports the scene `.json` file.

Additionally users may opt to save the image as a `.webp` file rather than a `.jpg`

### Image Format Conversion
**FFA** can take in a `.png` or `.jpg` file and convert it to FoundryVTT's preferred format of `.webp`
