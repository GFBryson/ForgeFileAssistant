# Foundry File Assistant
## Overview
The purpose of this project is to provide a simple way to help users of FoundryVTT clean and optimise files they wish to import to or use with the FoundryVTT system.

The project was born out of an error that happened when a JSON map file for import would have an image saved init as a 64bit string which would break the world because the file was not properly handelled by FoundryVTT on import. *(Specifically this was found by users of Dungeon Alchemist who's maps would break thier worlds)*

## Functions
### Image Stripping
**FFA** can read in a scene json file and take out the image string, saving it to a place of the users choosing.

If the user stores the image within their FoundryVTT file system the json will receive a path to that image so it will automatically load in when the user imports the scene json file

### Image Format Conversion
**FFA** can take in a .png or .jpeg file and convert it to FoundryVTT's preffered format of .webp

*we are aware that there is a bug where this feature does not work on large images. We are looking into solutions*