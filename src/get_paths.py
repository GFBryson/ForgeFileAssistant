from tkinter import filedialog, StringVar

def get_filepath(path_var: StringVar, do_after=None, filetypes: list = [("All filetypes", "*.*")]):
    path_var.set(filedialog.askopenfilename(filetypes=filetypes))
    if do_after is not None:
        do_after()


def get_directorypath(path_var: StringVar, do_after=None):
    path_var.set(filedialog.askdirectory())
    if do_after is not None:
        do_after()