from tkinter import filedialog, StringVar


def get_filepath(path_var: StringVar, do_after=None, filetypes: list = [("All filetypes", "*.*")]):
    print(path_var.get())
    initialdir = None if path_var.get() == "" else path_var.get()
    new_path = filedialog.askopenfilename(filetypes=filetypes, initialdir=initialdir)
    path_var.set( initialdir if new_path == "" else new_path)
    if do_after is not None:
        do_after()


def get_directorypath(path_var: StringVar, do_after=None):
    print(f"initial_dir:{path_var.get()}")
    initialdir = None if path_var.get() == "" else path_var.get()
    new_dir = filedialog.askdirectory(initialdir=initialdir)
    path_var.set(initialdir if new_dir == "" else new_dir)
    if do_after is not None:
        do_after()
