# Python Libraries
from os import listdir
from os.path import isfile, join
import customtkinter
import tkinter as tk
import pandas as pd

# Local Libraries
from features.app_style import *
from features.delete_widgets import clear_widgets


class EditKnowledge():
    def __init__(self, frame3:object) -> None:
        self.frame = frame3
        self._separator = False

    
    def start(self, frame1:object, main_page:object) -> None:
        clear_widgets(frame=frame1)

        # Create a new frame
        self.frame.tkraise()
        self.frame.pack_propagate(flag=False)

        # Frame1 widget
        logo_img = tk.PhotoImage(file="src/images/edit_interface.png")
        logo_wdiget = tk.Label(master=self.frame, image=logo_img, bg=color_background)
        logo_wdiget.image = logo_img

        logo_wdiget.pack()

        self.__heading()
        self.__back_button(main_page=main_page)
        self.__database_dropdown()


    def __back_button(self, main_page:object):
        # Back button
        back_image = tk.PhotoImage(file="src/images/back_icon.png")
        self._separator = False
        
        back_button = customtkinter.CTkButton(
            master=self.frame,
            image=back_image,
            width=10,
            height=20,
            corner_radius=50,
            text="",
            bg_color=color_heading_chat,
            fg_color=color_heading_chat,
            text_color=color_button_text,
            hover_color=color_heading_chat_click,
            command=lambda: main_page.main_page(self.frame)
        ).place(relx=0.05, rely=0.05, anchor="center")

    
    def __heading(self):
        # Heading widget
        textbox = tk.Label(
            master=self.frame,
            text="Conhecimento Personalizado",
            bg=color_heading_chat,
            fg=color_button_text,
            font=font_title
        )
        
        textbox.place(relx=0.5, rely=0.05, anchor="center")

    
    def __database_dropdown(self):
        options = (
                [file[:file.find(".")] for file in listdir("src/data/") if isfile(join("src/data/", file))]
            )
        
        options.insert(0, "+ Adicionar novo conhecimento")

        dropdown_choice = customtkinter.StringVar(value="Escolha uma...")

        self.__dropdown(
            options=options,
            func=self.__show_separator,
            dropdown_choice=dropdown_choice,
            text="Base de conhecimento",
            x=0.5,
            y=0.23
        )

    
    def __show_separator(self, choice):
        self.__reset_separator()

        if choice[0] == "+":
            separator_icon = tk.PhotoImage(file="src/images/plus_icon.png")
        else:
            separator_icon = tk.PhotoImage(file="src/images/edit_icon_big.png")

        separator_image = tk.PhotoImage(file="src/images/separator.png")

        self.separator_icon = customtkinter.CTkLabel(
            master=self.frame,
            image=separator_image,
            text=""
        )

        self.separator_icon.place(relx=0.5, rely=0.47, anchor="center")

        self.separator_label = customtkinter.CTkLabel(
            master=self.frame,
            image=separator_icon,
            text=""
        )

        self.separator_label.place(relx=0.5, rely=0.47, anchor="center")

        self._separator = True

    
    def __dropdown(self, options:str, func, dropdown_choice:str, text:str, x:float, y:float):
        dropdown_options = customtkinter.CTkComboBox(
            master=self.frame,
            width=400,
            height=35,
            border_width=2,
            border_color=color_background_input,
            fg_color=color_background_input,
            text_color=color_button_text,
            button_color=color_button,
            button_hover_color=color_press_button,
            dropdown_fg_color=color_background,
            dropdown_hover_color=color_background_input,
            dropdown_text_color=color_button_text,
            font=font_text,
            dropdown_font=font_text,
            values=options,
            command=lambda choice: func(choice),
            variable=dropdown_choice,
            justify="left"
        )

        dropdown_options.place(relx=x, rely=y, anchor="center")

        textbox = tk.Label(
            master=self.frame,
            text=text,
            bg=color_background,
            fg=color_button,
            font=font_menu,
        )
        
        textbox.place(relx=(x - 0.38), rely=(y - 0.06), anchor="w")


    def __reset_separator(self):
        if self._separator:
            self.separator_icon.destroy()
            self.separator_label.destroy()
            self._separator = False

    