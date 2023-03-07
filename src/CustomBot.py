# Python Libraries
import customtkinter
import tkinter as tk
from warnings import filterwarnings

# Local imports
from features.main_page import MainPage
from features.app_style import *


# Initialize app
filterwarnings("ignore")
root = customtkinter.CTk()
root.title("Custom ChatGPT Bot")

# Centering app
x = root.winfo_screenwidth() // 2
y = int(root.winfo_screenheight() * 0.1)

root.geometry(f'{width}x{height}+' + str(x - width // 2) + '+' + str(y))

# Creating frames
frame1 = tk.Frame(root, width=width, height=height, bg=color_background)
frame2 = tk.Frame(root, width=width, height=height, bg=color_background)
frame3 = tk.Frame(root, width=width, height=height, bg=color_background)

for frame in (frame1, frame2, frame3):
    frame.grid(row=0, column=0, sticky="nesw")

# Call main page
main_page = MainPage(root=root, frame1=frame1, frame2=frame2, frame3=frame3)

# Run app
root.mainloop()
