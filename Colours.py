import tkinter as tk
from tkinter import messagebox
from colorsys import rgb_to_hsv

def hex_to_rgb(hex_color):
    hex_color = hex_color.lstrip('#')
    r = int(hex_color[0:2], 16)
    g = int(hex_color[2:4], 16)
    b = int(hex_color[4:6], 16)
    return r, g, b

def rgb_to_hex(rgb_color):
    r, g, b = rgb_color
    hex_color = "#{:02X}{:02X}{:02X}".format(r, g, b)
    return hex_color

def rgb_to_cmyk(rgb_color):
    r, g, b = [x / 255.0 for x in rgb_color]
    k = min(1 - r, 1 - g, 1 - b)
    if k == 1:
        c, m, y = 0, 0, 0
    else:
        c = (1 - r - k) / (1 - k)
        m = (1 - g - k) / (1 - k)
        y = (1 - b - k) / (1 - k)
    return c, m, y, k

def cmyk_to_rgb(cmyk_color):
    c, m, y, k = cmyk_color
    r = (1 - c) * (1 - k) * 255
    g = (1 - m) * (1 - k) * 255
    b = (1 - y) * (1 - k) * 255
    return int(r), int(g), int(b)

def rgb_to_pms(rgb_color):
    r, g, b = [x / 255.0 for x in rgb_color]
    h, s, v = rgb_to_hsv(r, g, b)

    pms_colors = {
        "PMS Red": (0, 1, 1),
        "PMS Green": (1 / 3, 1, 1),
        "PMS Blue": (2 / 3, 1, 1),
        "PMS Yellow": (1 / 6, 1, 1),
        "PMS Purple": (5 / 6, 1, 1),
        "PMS Orange": (1 / 12, 1, 1),
        "PMS Pink": (11 / 12, 1, 1),
        "PMS Brown": (0.06, 0.68, 0.47),
        "PMS Gold": (0.11, 0.83, 0.91),
        "PMS Silver": (0, 0, 0.75),
        "PMS Gray": (0, 0, 0.5),
        "PMS Lavender": (0.83, 0.75, 0.75),
        "PMS Turquoise": (0.5, 1, 1),
        "PMS Teal": (0.5, 0.67, 0.5),
        "PMS Olive": (0.33, 1, 0.5),
        "PMS Maroon": (0, 1, 0.5),
        "PMS Navy": (0.66, 1, 0.25),
        "PMS Cyan": (0.5, 0, 0),
        "PMS Lime Green": (1 / 6, 1, 0.5),
        "PMS Forest Green": (1 / 3, 0.68, 0.47),
        "PMS Aqua": (0.5, 0, 0.75),
        "PMS Magenta": (5 / 6, 1, 0.75),
    }

    closest_color = min(pms_colors, key=lambda x: abs(pms_colors[x][0] - h) + abs(pms_colors[x][1] - s) + abs(pms_colors[x][2] - v))

    return closest_color

def show_color():
    hex_color = hex_entry.get()
    
    try:
        rgb_color = hex_to_rgb(hex_color)
        color_canvas.config(bg=hex_color)
        color_label.config(text=f"RGB: {rgb_color}")
        
        cmyk_color = rgb_to_cmyk(rgb_color)
        cmyk_label.config(text=f"CMYK: {cmyk_color}")
        
        pms_color = rgb_to_pms(rgb_color)
        pms_label.config(text=f"PMS: {pms_color}")
    except ValueError:
        messagebox.showerror("Error", "Invalid Hex Color Code")

# Create the main window
window = tk.Tk()
window.title("Color Converter")

# Hex to RGB Conversion
hex_label = tk.Label(window, text="Hex Color Code:")
hex_entry = tk.Entry(window)
hex_button = tk.Button(window, text="Convert to RGB", command=show_color)

# RGB to Hex Conversion
r_label = tk.Label(window, text="R:")
g_label = tk.Label(window, text="G:")
b_label = tk.Label(window, text="B:")
r_entry = tk.Entry(window)
g_entry = tk.Entry(window)
b_entry = tk.Entry(window)
rgb_button = tk.Button(window, text="Convert to Hex", command=show_color)

# Color Display
color_canvas = tk.Canvas(window, width=100, height=100, bg="white")
color_label = tk.Label(window, text="Color Information")

# Labels for CMYK and PMS
cmyk_label = tk.Label(window, text="CMYK:")
pms_label = tk.Label(window, text="PMS:")

# Label for Creator and Date
creator_label = tk.Label(window, text="Created by DinethH using Python - 2023", fg="gray")

# Layout
hex_label.grid(row=0, column=0)
hex_entry.grid(row=0, column=1)
hex_button.grid(row=0, column=2)
r_label.grid(row=1, column=0)
g_label.grid(row=1, column=1)
b_label.grid(row=1, column=2)
r_entry.grid(row=1, column=3)
g_entry.grid(row=1, column=4)
b_entry.grid(row=1, column=5)
rgb_button.grid(row=1, column=6)
color_canvas.grid(row=2, column=0, columnspan=3)
color_label.grid(row=3, column=0, columnspan=3)
cmyk_label.grid(row=4, column=0, columnspan=3)
pms_label.grid(row=5, column=0, columnspan=3)
creator_label.grid(row=6, column=0, columnspan=3)

window.mainloop()
