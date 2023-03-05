# Python Libraries
import customtkinter
import tkinter as tk
from PIL import Image, ImageTk

# Local Libraries
from features.app_style import *
from features.delete_widgets import clear_widgets


class ChatBot():
    def __init__(self, frame2) -> None:
        self.frame = frame2
    

    def start(self, frame1, main_page):
        # Delete other widgets
        clear_widgets(frame=frame1)

        # Create a new frame
        self.frame.tkraise()
        self.frame.pack_propagate(flag=False)

        # Frame1 widget
        logo_img = ImageTk.PhotoImage(file="src/images/chat_bot_interface.png")
        logo_wdiget = tk.Label(master=self.frame, image=logo_img, bg=color_background)
        logo_wdiget.image = logo_img

        logo_wdiget.pack()
        self.__back_button(main_page)


    def __back_button(self, main_page):
        # Back button
        back_image = ImageTk.PhotoImage(file="src/images/back_icon.png")
        back_button = customtkinter.CTkButton(
            master=self.frame,
            image=back_image,
            width = 10,
            height = 20,
            corner_radius=50,
            text="",
            bg_color=color_heading_chat,
            fg_color=color_heading_chat,
            text_color=color_button_text,
            hover_color=color_heading_chat_click,
            command=lambda: main_page.main_page(self.frame)
        ).place(relx=0.05, rely=0.05, anchor="center")


    @property
    def get_frame(self):
        return self.frame
