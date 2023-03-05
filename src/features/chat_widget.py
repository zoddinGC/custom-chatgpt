# Python Libraries
import customtkinter
import tkinter as tk
from PIL import Image, ImageTk

# Local Libraries
from features.app_style import *
from features.delete_widgets import clear_widgets


class ChatWidget():
    def __init__(self, frame2) -> None:
        self.frame = frame2
        self.first_time = True
    

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
        self.__user_input()
        self.__send_button()

    
    def __back_button(self, main_page):
        # Back button
        back_image = ImageTk.PhotoImage(file="src/images/back_icon.png")
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

    
    def __user_input(self, get:bool=False):       
        self.chat_entry = customtkinter.CTkEntry(
            master=self.frame,
            width=350,
            height=50,
            corner_radius=60,
            placeholder_text="Digite sua mensagem...",
            bg_color=color_background,
            fg_color=color_background_input,
            border_color=color_background,
            text_color=color_button_text,
            placeholder_text_color=place_holder_color,

        )

        self.chat_entry.place(relx=0.80, rely=0.9, anchor="e")
    

    def __send_button(self):
        # Send button
        send_image = ImageTk.PhotoImage(file="src/images/send_icon.png")
        send_button = customtkinter.CTkButton(
            master=self.frame,
            image=send_image,
            width=30,
            height=20,
            corner_radius=50,
            text="",
            bg_color=color_background,
            fg_color=color_background,
            text_color=color_button_text,
            hover_color=color_background_input,
            command=lambda: self.__get_user_input()
        )
        send_button.place(relx=0.87, rely=0.9, anchor="center")


    def __get_user_input(self):
        user_input = self.chat_entry.get()
        bot_answer = user_input # self.chat_gpt.get()
        
        # Add user textbox and text
        user_input_size = len(user_input) // 41
        if user_input_size > 4:
            user_input_size = 4

        self.__add_user_text_box(user_input_size=user_input_size)
        self.__add_text(self.user_text_box, user_input)
        # Delete user text from input widget
        self.chat_entry.delete(0, tk.END)

        # Add bot input
        chat_gpt_size = len(bot_answer) // 41
        if chat_gpt_size > 10:
            chat_gpt_size = 10

        self.__add_chat_gpt_text_box(user_input_size, chat_gpt_size)
        self.__add_text(self.bot_text_box, bot_answer)


    def __add_user_text_box(self, user_input_size):
        self.user_box_height = 30 + (20 * user_input_size) # 30 + in case size  = 0

        if not self.first_time:
            self.user_text_box.destroy()
        
        self.user_text_box = customtkinter.CTkTextbox(
            master=self.frame,
            width=300,
            height=self.user_box_height,
            corner_radius=5,
            border_width=0,
            border_spacing=10,
            bg_color=color_background,
            fg_color=color_heading_chat,
            text_color= color_button_text,
            scrollbar_button_color=color_background,
            font=font_text,            
        )
        self.user_text_box.place(relx=0.3, rely=0.2, anchor="nw")

    
    def __add_chat_gpt_text_box(self, user_input_size:int, bot_input_size:int):     
        chat_gpt_box_height = 30 + (20 * bot_input_size) # 30 + in case size = 0

        if not self.first_time:
            self.bot_text_box.destroy()
        
        self.bot_text_box = customtkinter.CTkTextbox(
            master=self.frame,
            width=300,
            height=chat_gpt_box_height,
            corner_radius=5,
            border_width=0,
            border_spacing=10,
            bg_color=color_background,
            fg_color=color_button,
            text_color= color_button_text,
            scrollbar_button_color=color_background,
            font=font_text,            
        )
        self.bot_text_box.place(relx=0.7, rely=0.30 + 0.035 * user_input_size, anchor="ne")

        self.first_time = False


    def __add_text(self, text_box, text):
        text_box.insert(tk.END, text)


    @property
    def get_frame(self):
        return self.frame
