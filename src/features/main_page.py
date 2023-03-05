# Python Libraries
import customtkinter
import tkinter as tk
from PIL import Image, ImageTk

# Local Libraries
from features.app_style import *
from features.chat_bot import ChatBot
from features.delete_widgets import clear_widgets


class MainPage():
    def __init__(self, root, frame1, frame2) -> None:
        self.root = root
        self.frame = frame1
        self.chat_bot = ChatBot(frame2)
        self.main_page(frame2)
        

    def main_page(self, frame2):
        # Delete other widgets
        clear_widgets(frame=frame2)

        # Create a frame
        self.frame.tkraise()
        self.frame.pack_propagate(flag=False)

        # Frame1 widget
        logo_img = ImageTk.PhotoImage(file="src/images/custom_bot_logo.png")
        logo_wdiget = tk.Label(master=self.frame, image=logo_img, bg=color_background)
        logo_wdiget.image = logo_img

        logo_wdiget.pack()

        self.__start_button()


    def __start_button(self):
        # Start button
        button1 = customtkinter.CTkButton(
            master=self.frame,
            width = 250,
            height = 70,
            corner_radius=70,
            text="COMEÇAR CHAT",
            font=font_button,
            fg_color=color_button,
            text_color=color_button_text,
            hover_color=color_hover_button,
            command=lambda: self.chat_bot.start(self.frame, self)
        ).place(relx=0.5, rely=0.6, anchor="center")

        self.__text_info()


    def __text_info(self):
        textbox = tk.Label(
            master=self.frame,
            text="Você está pronto para essa nova era?",
            bg=color_background,
            fg=color_button_text,
            font=font_text
        ).place(relx=0.5, rely=0.83, anchor="center")
