# Python Libraries
from os import listdir, system
from os.path import isfile, join
import tkinter as tk
import threading
import pandas as pd
import customtkinter

# Local Libraries
from features.app_style import *
from features.helper_functions import clear_widgets


def _dropdown(
            frame:object,
            options:str,
            func,
            dropdown_choice:str,
            text:str,
            x:float,
            y:float
        ):

    dropdown_options = customtkinter.CTkComboBox(
        master=frame,
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
        master=frame,
        text=text,
        bg=color_background,
        fg=color_button,
        font=font_menu,
    )

    textbox.place(relx=(x - 0.38), rely=(y - 0.06), anchor="w")

    return dropdown_options


class EditKnowledge():
    def __init__(self, frame3:object) -> None:
        self.frame = frame3
        self._end = False
        self._input = False


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
        self._end = False
        self._input = False

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
        )
        
        back_button.place(relx=0.05, rely=0.05, anchor="center")


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

        self.dropdown = _dropdown(
            frame=self.frame,
            options=options,
            func=self.__show_separator,
            dropdown_choice=dropdown_choice,
            text="Base de conhecimento",
            x=0.5,
            y=0.23
        )


    def __show_separator(self, choice):
        self.__reset_separator()
        self.__show_content(choice=choice)

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

        self.separator_icon.place(relx=0.5, rely=0.33, anchor="center")

        self.separator_label = customtkinter.CTkLabel(
            master=self.frame,
            image=separator_icon,
            text=""
        )

        self.separator_label.place(relx=0.5, rely=0.33, anchor="center")


    def __show_content(self, choice:str):
        original_choice = choice

        if choice[0] != "+":
            database = pd.read_excel(f"src/data/{choice}.xlsx", usecols="A:B")
            database = database.dropna()

            try:
                database["content"] = database["content"].str[:40]
            except:
                pass

            choice = " ".join(choice.split("_")).title()

            # "Content of [...]" at the begin
            self.display_database_name = customtkinter.CTkLabel(
                master=self.frame,
                width=200,
                height=50,
                corner_radius=5,
                bg_color=color_background,
                fg_color=color_background,
                text_color=color_button,
                font=font_button,
                text=f"Conteúdo de {choice}"
            )
            self.display_database_name.place(relx=0.5, rely=0.42, anchor="center")
            
            # Database content text box
            self.database_content = customtkinter.CTkTextbox(
                master=self.frame,
                width=350,
                height=240,
                corner_radius=5,
                border_width=0,
                border_spacing=10,
                bg_color=color_background,
                fg_color=color_background_input,
                text_color= color_button_text,
                scrollbar_button_color=color_background,
                font=font_text,
            )
            self.database_content.place(relx=0.5, rely=0.67, anchor="center")

            if database.shape[0] == 0:
                database = "Empty"

            self.database_content.insert(tk.END, database)

            self.__end_button(
                image="edit_icon_white",
                x=0.5,
                y=0.92,
                text="Editar",
                func=self.__get_user_input,
                choice=original_choice
            )
        
        else:
            self.__user_input()
            self.__end_button(
                image="plus_icon_white",
                x=0.5,
                y=0.7,
                text="Adicionar",
                func=self.__get_user_input,
                choice=original_choice
            )

            self._input = True


    def __end_button(self, image:str, x:float, y:float, text:str, func, choice:str):
        # Save button
        end_image = tk.PhotoImage(file=f"src/images/{image}.png")

        self.end_button = customtkinter.CTkButton(
            master=self.frame,
            image=end_image,
            width=30,
            height=35,
            corner_radius=50,
            text=text,
            bg_color=color_background,
            fg_color=color_heading_chat,
            text_color=color_button_text,
            hover_color=color_heading_chat_click,
            font=font_button,
            command=lambda: func(choice)
        )

        self.end_button.place(relx=x, rely=y, anchor="center")

        self._end = True


    def __user_input(self):       
        self.chat_entry = customtkinter.CTkEntry(
            master=self.frame,
            width=350,
            height=50,
            corner_radius=60,
            placeholder_text="Digite APENAS o NOME da base:",
            bg_color=color_background,
            fg_color=color_background_input,
            border_color=color_background,
            text_color=color_button_text,
            placeholder_text_color=place_holder_color,

        )

        self.chat_entry.place(relx=0.5, rely=0.58, anchor="center")


    def __get_user_input(self, choice):
        def create_file():
            with open(f"src/data/{user_input}.xlsx", "w") as f:
                pd.DataFrame(columns=["role", "content"]).to_excel(f"src/data/{user_input}.xlsx", index=False)
        try:
            user_input = self.chat_entry.get()

            user_input = user_input.strip().lower()

            # Delete user text from input widget
            self.chat_entry.delete(0, tk.END)

            threading.Thread(target=create_file())

            self.dropdown.destroy()
            self.__database_dropdown()

        except:
            system(f"start EXCEL.EXE src/data/{choice}.xlsx")


    def __reset_separator(self):
        if self._end:
            self.separator_icon.destroy()
            self.separator_label.destroy()
            if self._input:
                self.chat_entry.destroy()
            else:
                self.database_content.destroy()
                self.display_database_name.destroy()
            self.end_button.destroy()

            self._input = False
            self._end = False
