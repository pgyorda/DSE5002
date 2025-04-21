# -*- coding: utf-8 -*-
import tkinter as tk
from tkinter import filedialog

def file_choose():
    """
    Opens a file dialog using tkinter and returns the path to the selected file.

    Returns:
        str: The path to the selected file, or an empty string if no file is selected.
    """
    root = tk.Tk()
    root.withdraw()  # Hide the main window

    file_path = filedialog.askopenfilename()
    return file_path

if __name__ == '__main__':
    selected_file = file_choose()
    if selected_file:
        print(f"You selected (tkinter): {selected_file}")
    else:
        print("No file selected (tkinter).")