# Python Libraries
import customtkinter
from os import listdir
from os.path import isfile, join
from PIL import ImageTk
import tkinter as tk


# Local Libraries
from features.app_style import *
from features.chat_widget import ChatWidget
from features.delete_widgets import clear_widgets


class MainPage():
    def __init__(self, root:object, frame1:object, frame2:object) -> None:
        self.root = root
        self.frame = frame1
        self.chat_widget = ChatWidget(frame2)
        self.main_page(frame2)
        

    def main_page(self, frame2:object) -> None:
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

        self.dropdown_show = False
        self.dropdown_choice = "src/data/empty_data.xlsx"

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
            command=lambda: self.chat_widget.start(self.frame, self, self.dropdown_choice)
        ).place(relx=0.5, rely=0.6, anchor="center")

        self.__text_info()
        self.__check_box()

    
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

            self.dropdown_choice = "src/data/empty_data.xlsx"

        else:
            options = (
                [file[:file.find(".")] for file in listdir("src/data/") if isfile(join("src/data/", file))]
            )

            dropdown_choice = customtkinter.StringVar(value="empty_data")

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

            self.dropdown_options.place(relx=0.5, rely=0.77, anchor="center")

            self.dropdown_show = True


    def __text_info(self):
        textbox = tk.Label(
            master=self.frame,
            text="Você está pronto para essa nova era?",
            bg=color_background,
            fg=color_button_text,
            font=font_text
        ).place(relx=0.5, rely=0.9, anchor="center")
