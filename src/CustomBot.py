# Python Libraries
import customtkinter
import tkinter as tk
from PIL import Image, ImageTk

# Local imports
from features.main_page import MainPage
from features.app_style import *


# Initialize app 
root = customtkinter.CTk()
root.title("Custom Zoddin's Bot")

# Centering app
x = root.winfo_screenwidth() // 2
y = int(root.winfo_screenheight() * 0.1)

root.geometry(f'{width}x{height}+' + str(x - width // 2) + '+' + str(y))

# Call main page
main_page = MainPage(root=root)

# Run app
root.mainloop()
