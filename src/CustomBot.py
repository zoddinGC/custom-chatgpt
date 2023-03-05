import tkinter as tk
from PIL import ImageTk
from features.frame2 import load_frame2

# Initialize app
root = tk.Tk()
root.title("Custom Zoddin's Bot")

# ========== App style ==========
# Size
width = 500
height = 600

# Colors
color_background = "#3d6466"
color_button = "#28393a"
color_button_text = "#ffffff"
color_press_button = "#303841"
color_press_button_text = "#fff000"

# Fonts
font_button = ("TkHeadingFont", 20)
font_title = ("TkMenuFont", 16)
font_menu = ("", 14)
font_text = ("", 11)

# Centering app
x = root.winfo_screenwidth() // 2
y = int(root.winfo_screenheight() * 0.1)

root.geometry(f'{width}x{height}+' + str(x - width // 2) + '+' + str(y))

# Create a frame
frame1 = tk.Frame(root, width=width, height=height, bg=color_background)
frame1.grid(row=0, column=0)

frame1.pack_propagate(flag=False)

# Frame1 widget
logo_img = ImageTk.PhotoImage(file="src/images/custom_bot_logo.png")
logo_wdiget = tk.Label(frame1, image=logo_img, bg=color_background)
logo_wdiget.image = logo_img

logo_wdiget.pack()
logo_wdiget.place(relx=0.5, rely=0.25, anchor="center")

tk.Label(
    frame1,
    text="ready for chat with an AI?",
    bg=color_background,
    fg="white",
    font=font_title
).place(relx=0.5, rely=0.5, anchor="center")

# Button1 widget
tk.Button(
    frame1,
    text="START CHAT",
    font=font_button,
    bg=color_button,
    fg=color_button_text,
    cursor="hand2",
    activebackground=color_press_button,
    activeforeground=color_press_button_text,
    border=5,
    command=lambda: load_frame2()
).place(relx=0.5, rely=0.6, anchor="center")

# Run app
root.mainloop()
