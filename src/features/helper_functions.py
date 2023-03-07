from os import path
import sys


# https://stackoverflow.com/questions/31836104/pyinstaller-and-onefile-how-to-include-an-image-in-the-exe-file
def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS2
    except Exception:
        base_path = path.abspath(".")

    return path.join(base_path, relative_path)


def clear_widgets(frame:object) -> None:
    for widget in frame.winfo_children():
        widget.destroy()
