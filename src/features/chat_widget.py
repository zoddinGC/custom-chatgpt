# Python Libraries
import tkinter as tk
import threading
import customtkinter


# Local Libraries
from features.app_style import *
from features.helper_functions import clear_widgets
from features.chat_bot import ChatBot


class ChatWidget():
    def __init__(self, frame2:object) -> None:
        self.frame = frame2
        self.first_time = True
        self.chat_bot = ChatBot()


    def start(self, frame1:object, main_page:object, dropdown_choice:str) -> None:
        # Delete other widgets
        clear_widgets(frame=frame1)

        threading.Thread(
            target=self.chat_bot.load_knowledge,
            args=(dropdown_choice,)
        ).start()     

        # Create a new frame
        self.frame.tkraise()
        self.frame.pack_propagate(flag=False)

        # Frame1 widget
        logo_img = tk.PhotoImage(file="src/images/chat_bot_interface.png")
        logo_wdiget = tk.Label(master=self.frame, image=logo_img, bg=color_background)
        logo_wdiget.image = logo_img

        logo_wdiget.pack()

        # Load other widgets
        self.__name_bot(dropdown_choice)
        self.__back_button(main_page)
        self.__user_input()
        self.__send_button()


    def __name_bot(self, dropdown_choice):
        # BotName widget
        menu_name = "".join(dropdown_choice[9:dropdown_choice.index(".")])
        menu_name = " ".join(menu_name.split('_')).title()

        _cut = 19 if len(menu_name) > 19 else None

        menu_name = menu_name[:_cut] + " ChatGPT"

        textbox = tk.Label(
            master=self.frame,
            text=menu_name,
            bg=color_heading_chat,
            fg=color_button_text,
            font=font_title
        )

        textbox.place(relx=0.16, rely=0.025, anchor="nw")


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


    def __user_input(self):     
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

        self.chat_entry.place(relx=0.78, rely=0.9, anchor="e")


    def __send_button(self):
        # Send button
        send_image = tk.PhotoImage(file="src/images/send_icon.png")
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
        send_button.place(relx=0.85, rely=0.901, anchor="center")


    def __get_user_input(self):
        user_input = self.chat_entry.get()

        # Add user textbox and text
        user_input_size = len(user_input) // 41
        user_input_size = min(user_input_size, 4)

        self.__add_user_text_box(user_input_size=user_input_size)
        self.__add_text(self.user_text_box, user_input)
        # Delete user text from input widget
        self.chat_entry.delete(0, tk.END)
        
        threading.Thread(
            target=self.__get_bot_output,
            args=(user_input,)
        ).start()


    def __get_bot_output(self, user_input:str):
        # Add bot input
        bot_answer = self.chat_bot.chatbot(user_input=user_input)

        if bot_answer == "Error 007":
            bot_answer = "ATEN????O: Isso n??o ?? uma mensagem do ChatGPT. \nUm ou mais cargos (roles) cont??m ERROR de nome. Verifique na base de conhecimento para encontrar o cargo errado."

        chat_gpt_size = len(bot_answer) // 41

        self.__add_chatgpt_text_box(chat_gpt_size)
        self.__add_text(self.bot_text_box, bot_answer)


    def __add_user_text_box(self, user_input_size:int):
        self.user_box_height = 45 + (10 * user_input_size) # 30 + in case size  = 0

        if not self.first_time:
            self.__destroy_widgets()

        # "You" at the begin
        display_you = customtkinter.CTkTextbox(
            master=self.frame,
            width=100,
            height=self.user_box_height,
            corner_radius=5,
            border_width=0,
            border_spacing=10,
            bg_color=color_background,
            fg_color=color_background,
            text_color=color_heading_chat,
            font=font_text,
        )
        display_you.place(relx=0.83, rely=0.15, anchor="nw")
        display_you.insert(tk.END, text="Voc??")

        # User text box
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
        self.user_text_box.place(relx=0.32, rely=0.2, anchor="nw")        

        self.__display_chatgpt_icon()


    def __display_chatgpt_icon(self):
        # "ChatGPT" at the begin
        if not self.first_time:
            self.display_gpt.delete("1.0", tk.END)

        self.user_text_box.update()
        user_input_size = (self.user_text_box.winfo_height() - 45) / 600

        self.display_gpt = customtkinter.CTkTextbox(
            master=self.frame,
            width=100,
            height=self.user_box_height,
            corner_radius=5,
            border_width=0,
            border_spacing=10,
            bg_color=color_background,
            fg_color=color_background,
            text_color=color_button,
            font=font_text,
        )
        self.display_gpt.place(relx=0.29, rely=0.25 + user_input_size, anchor="ne")
        self.display_gpt.insert(tk.END, text="ChatGPT")

        # Add writing icon for ChatGPT output
        writing_icon = tk.PhotoImage(file="src/images/writing_message.png")

        self.writing_widget = tk.Label(
            master=self.frame,
            image=writing_icon,
            bg=color_background)
        self.writing_widget.image = writing_icon

        self.writing_widget.place(relx=0.215, rely=0.3 + user_input_size, anchor="ne")


    def __add_chatgpt_text_box(self, bot_input_size:int):
        self.display_gpt.update()
        input_size_box = self.display_gpt.winfo_height()

        chat_gpt_box_height = 45 + 12 * bot_input_size # 30 + in case size = 0
        if input_size_box + chat_gpt_box_height > 276:
            chat_gpt_box_height = 276

        display_chatgpt_posy = input_size_box / 600

        # Remove ChatGPT writing icon
        self.writing_widget.destroy()

        # ChatGPT Text Box
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
        self.bot_text_box.place(relx=0.7, rely=0.23 + display_chatgpt_posy, anchor="ne")

        self.first_time = False


    def __add_text(self, text_box:object, text:str):
        text_box.insert(tk.END, text)


    def __destroy_widgets(self):
        self.user_text_box.destroy()
        self.bot_text_box.destroy()


    @property
    def get_frame(self) -> object:
        return self.frame
