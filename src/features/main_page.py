# Python Libraries
import customtkinter
import tkinter as tk
from PIL import Image, ImageTk

# Local Libraries
from features.app_style import *
from features.chat_bot import ChatBot

class MainPage():
    def __init__(self, root) -> None:
        self.root = root
        self.chat_bot = ChatBot()
        self.main_page()
        

    def main_page(self):
        # Create a frame
        frame1 = tk.Frame(self.root, width=width, height=height, bg=color_background)
        frame1.grid(row=0, column=0)

        frame1.pack_propagate(flag=False)

        # Frame1 widget
        logo_img = ImageTk.PhotoImage(file="src/images/custom_bot_logo.png")
        logo_wdiget = tk.Label(master=frame1, image=logo_img, bg=color_background)
        logo_wdiget.image = logo_img

        logo_wdiget.pack()

        self.start_button()


    def start_button(self):
        # Start button
        button1 = tk.Button(master=self.root)
        button1_image = ImageTk.PhotoImage(file="src/images/button1.png")

        button1.configure(
            image=button1,
            bg=color_background,
            highlightthickness=0,
            activebackground="#000000",
            command= lambda: ChatBot()
        ).pack() # .place(relx=0.5, rely=0.7, anchor="center")