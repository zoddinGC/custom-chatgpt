from os import getenv, listdir
import tkinter as tk
import customtkinter
from dotenv import load_dotenv
import openai
import threading

# Local imports
from features.helper_functions import clear_widgets
from features.app_style import *


load_dotenv()

class OpenAIKey():
    def __init__(self, frame4:object) -> None:
        self.frame = frame4
        self.API_KEY = getenv("API_KEY")
        self.first_time = True

        if ".env" not in listdir():
            self.__save_in_env(create_env=True)


    def start(self, frame1:object, main_page:object) -> None:
        # Clear older frames
        clear_widgets(frame1)

        # Create a new frame
        self.frame.tkraise()
        self.frame.pack_propagate(flag=False)

        # Frame1 widget
        logo_img = tk.PhotoImage(file="src/images/edit_interface.png")
        logo_wdiget = tk.Label(master=self.frame, image=logo_img, bg=color_background)
        logo_wdiget.image = logo_img

        logo_wdiget.pack()

        textbox = tk.Label(
            master=self.frame,
            text="Edite sua chave da OpenAI",
            bg=color_heading_chat,
            fg=color_button_text,
            font=font_title
        )
        
        textbox.place(relx=0.5, rely=0.05, anchor="center")

        self.__back_button(main_page)
        self.__edit_key()
        self.__save_button()


    def __back_button(self, main_page:object):
        # Back button
        back_image = tk.PhotoImage(file="src/images/back_icon.png")
        self.first_time = True

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


    def __edit_key(self):
        # "Your Key" at the begin
        textbox = tk.Label(
            master=self.frame,
            text="Sua chave atual",
            bg=color_background,
            fg=color_button,
            font=font_text
        )
        
        textbox.place(relx=0.5, rely=0.27, anchor="center")

        # User text box
        self.api_key_textbox = customtkinter.CTkTextbox(
            master=self.frame,
            width=400,
            height=50,
            border_color=color_background,
            corner_radius=10,
            border_width=5,
            bg_color=color_background,
            fg_color=color_background_input,
            text_color= color_button_text,
            scrollbar_button_color=color_background,
            font=font_text,
        )
        self.api_key_textbox.place(relx=0.5, rely=0.35, anchor="center")
        self.__show_api()


    def __show_api(self):
        if not self.first_time:
            self.api_key_textbox.delete("1.0", tk.END)

        self.api_key_textbox.tag_config("center", justify="center")
        self.api_key_textbox.insert("1.0", text=self.API_KEY)
        self.api_key_textbox.tag_add("center", "1.0", "end")


    def __save_button(self):
        if not self.first_time:
            self.message.destroy()

        # Start button
        save_button = customtkinter.CTkButton(
            master=self.frame,
            width = 100,
            height = 50,
            corner_radius=70,
            text="SALVAR CHAVE",
            font=font_button,
            fg_color=color_button,
            text_color=color_button_text,
            hover_color=color_hover_button,
            command=lambda: self.__save_in_env()
        )

        save_button.place(relx=0.5, rely=0.5, anchor="center")


    def __save_in_env(self, create_env:bool=False):
        if not create_env:
            self.API_KEY = self.api_key_textbox.get("1.0", tk.END).strip()
            threading.Thread(target=self.__check_API())

        with open(".env", "w") as f:
                if self.API_KEY is None:
                    self.API_KEY = "Sem chave cadastrada"
                f.write(f"API_KEY={self.API_KEY}")


    def __check_API(self):
        try:
            openai.api_key = self.API_KEY
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[{"role":"system", "content":"Oi"}],
                temperature=0.2
            )
            self.__show_message(accepted=True)
        except:
            self.__show_message(accepted=False)


    def __show_message(self, accepted:bool):
        if accepted:
            text = "Chave Aceita!"
            fg_color = color_heading_chat
        else:
            text = "Chave Errada."
            fg_color = color_button

        self.message = tk.Label(
            master=self.frame,
            text=text,
            bg=color_background,
            fg=fg_color,
            font=font_button
        )

        self.message.place(relx=0.5, rely=0.6, anchor="center")
        self.first_time = False
        self.__show_api()
