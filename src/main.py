"""
## How to Run
To run this script you'll need to
1) install python 3.9^ from https://www.python.org/downloads/
2) paste this script into a file saved with the .py extension (ex. foundry_import_helper.py)
3) open a command prompt(windows) or bash shell (Linux/Mac) and run the following command
    python3 name_of_script.py
    ** please note you need to replace 'name_of_script' with whatever you named the file in step 2 and you need the
    ** shell to be looking in the place you put the script
    ** (you can easily youtube how to navigate in cmd or bash so I won't explain here)
"""

from tkinter import *
from tkinter.ttk import Notebook

from src.remove_image_from_json import get_remove_image_from_json_tab
from src.optimize_image import get_image_optimization_frame
from src.split_map import get_split_map_frame

if __name__ == '__main__':
    root_window = Tk()
    root_window.title("Foundry File Assistant")
    root_window.geometry("800x500")

    tab_control = Notebook(root_window)

    tab_1 = get_remove_image_from_json_tab(root_window)
    tab_2 = get_image_optimization_frame(root_window)

    tab_3 = Frame(root_window)
    tab_3_control = Notebook(tab_3)
    tab_3.pack(expand=True, fill='both')
    tab_3_1 = get_split_map_frame(tab_3)
    # tab_3_2 = get_split_map_frame(tab_3)
    # tab_3_3 = get_split_map_frame(tab_3)

    tab_control.add(tab_1, text="Clean.jpeg from JSON")
    tab_control.add(tab_2, text="Optimize Image")
    tab_control.add(tab_3, text="Map Manipulation")
    tab_3_control.add(tab_3_1, text="Tile Map")
    # tab_3_control.add(tab_3_2, text="Split Map")
    # tab_3_control.add(tab_3_3, text="Rotate Map")

    tab_control.pack(expand=True, fill='both')
    tab_3_control.pack(expand=True, fill='both')
    mainloop()
