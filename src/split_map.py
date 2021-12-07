from tkinter import *

def get_split_map_frame(window):
        tab_root = Frame(window)

        radio_selection = IntVar()
        R1 = Radiobutton(tab_root, text="2", variable=radio_selection, value=0, command=None)
        R1.pack(anchor=W)
        R2 = Radiobutton(tab_root, text="4", variable=radio_selection, value=1, command=None)
        R2.pack(anchor=W)
        R3 = Radiobutton(tab_root, text="6", variable=radio_selection, value=2, command=None)
        R3.pack(anchor=W)

        tab_root.pack(expand=True, fill='both')
        return tab_root
