import platform
import pyglet

# ===== Size
width = 500
height = 600

# ===== Colors
# = Background
color_background = "#264653"

# = Button
color_button = "#E76F51"
color_press_button = "#955E52"

color_button_text = "#FFFFFF"
color_press_button_text = "#E6C5A6"

color_hover_button = "#CF6247"

color_heading_chat = "#2A9D8F"
color_heading_chat_click = "#238074"

# ===== User input
place_holder_color = "#3C6E82"
color_background_input = "#162F39"

# ====== Fonts
# = Check operational system
if platform.system() == "Windows":
    pyglet.font.add_file("src/fonts/CODE_Bold.otf")
    font = "CODE_Bold"
else:
    font = "TkHeadingFont"

font_button = (font, 18, 'bold')
font_title = (font, 16, 'bold')
font_menu = (font, 14, 'bold')
font_text = (font, 12, 'bold')
