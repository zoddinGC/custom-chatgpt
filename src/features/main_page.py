# Python Libraries
from os import listdir
from os.path import isfile, join
import tkinter as tk
import customtkinter


# Local Libraries
from features.app_style import *
from features.chat_widget import ChatWidget
from features.helper_functions import clear_widgets
from features.edit_widget import EditKnowledge
from features.key_widget import OpenAIKey


class MainPage():
    def __init__(self, root:object, frame1:object, frame2:object, frame3:object, frame4:object) -> None:
        self.root = root
        self.frame = frame1
        self.chat_widget = ChatWidget(frame2)
        self.edit_widget = EditKnowledge(frame3)
        self.api_key = OpenAIKey(frame4)
        self.main_page(frame2)


    def main_page(self, frame2:object) -> None:
        # Delete other widgets
        clear_widgets(frame=frame2)

        # Create a frame
        self.frame.tkraise()
        self.frame.pack_propagate(flag=False)

        # Frame1 widget
        logo_img = tk.PhotoImage(file="src/images/custom_bot_logo.png")
        logo_wdiget = tk.Label(master=self.frame, image=logo_img, bg=color_background)
        logo_wdiget.image = logo_img

        logo_wdiget.pack()

        self.dropdown_show = False
        self.dropdown_choice = "src/data/original.xlsx"

        self.__start_button()
        self.__text_info()
        self.__check_box()
        self.__api_key_icon()


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
            command=lambda: self.chat_widget.start(
                frame1=self.frame,
                main_page=self,
                dropdown_choice=self.dropdown_choice
            )
        )
        
        button1.place(relx=0.5, rely=0.6, anchor="center")

    
    def __check_box(self):
        # Check box to use custom knowledge
        check_var = tk.StringVar(master=self.frame, value="0")

        custom_knowledge = customtkinter.CTkCheckBox(
            master=self.frame,
            width=100,
            height=30,
            bg_color=color_background,
            fg_color=color_background,
            border_width=2,
            border_color=color_button,
            text_color=color_button_text,
            text_color_disabled=color_background_input,
            text="Usar conhecimento personalizado",
            hover=True,
            variable=check_var,
            command=lambda: self.__custom_knowledge(check_var.get()),
        )

        custom_knowledge.place(relx=0.5, rely=0.7, anchor="center")

    
    def __custom_knowledge(self, use:str):
        def __get_dropdown_choice(choice):
            self.dropdown_choice = f"src/data/{choice}.xlsx"

        if use == "0":
            if self.dropdown_show:
                self.dropdown_options.destroy()
                self.edit_button.destroy()

            self.dropdown_choice = "src/data/original.xlsx"

        else:
            self.__edit_custom_knowledge()

            options = (
                [file[:file.find(".")] for file in listdir("src/data/") if isfile(join("src/data/", file))]
            )

            dropdown_choice = customtkinter.StringVar(value="original")

            self.dropdown_options = customtkinter.CTkComboBox(
                master=self.frame,
                width=200,
                height=30,
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
                command=lambda x: __get_dropdown_choice(x),
                variable=dropdown_choice,
                justify="left"
            )

            self.dropdown_options.place(relx=0.52, rely=0.77, anchor="center")

            self.dropdown_show = True

        
    def __edit_custom_knowledge(self):
        edit_image = tk.PhotoImage(file="src/images/edit_icon.png")

        self.edit_button = customtkinter.CTkButton(
            master=self.frame,
            image=edit_image,
            text="",
            width=15,
            height=20,
            corner_radius=5,
            border_width=0,
            border_color=color_background,
            bg_color=color_background,
            fg_color=color_background,
            hover_color=color_background_input,
            command=lambda: self.edit_widget.start(
                frame1=self.frame,
                main_page=self
            )
        )

        self.edit_button.place(relx=0.28, rely=0.77, anchor="center")


    def __text_info(self):
        textbox = tk.Label(
            master=self.frame,
            text="Você está pronto para essa nova era?",
            bg=color_background,
            fg=color_button_text,
            font=font_text
        )
        
        textbox.place(relx=0.5, rely=0.9, anchor="center")


    def __api_key_icon(self):
        # API Key edit button
        api_key_image = tk.PhotoImage(file="src/images/key_icon.png")
        button2 = customtkinter.CTkButton(
            master=self.frame,
            image=api_key_image,
            width=25,
            height=50,
            corner_radius=70,
            text="",
            font=font_button,
            fg_color=color_background,
            text_color=color_button_text,
            hover_color=color_background_input,
            command=lambda: self.api_key.start(
                frame1=self.frame,
                main_page=self,
            )
        )
        
        button2.place(relx=0.9, rely=0.07, anchor="center")
