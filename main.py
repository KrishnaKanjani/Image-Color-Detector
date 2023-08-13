from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk
from colorthief import ColorThief
import os

# --------------------------------- Functions -------------------------- #
def show_image():
    global filename
    filename = filedialog.askopenfilename(initialdir=os.getcwd(),
                                          title='Select Image File')
    
    img = Image.open(filename)
    # Image resizing   
    aspect_ratio = img.height / img.width
    target_width = 370
    target_height = int(aspect_ratio * target_width)
    img = img.resize(size=(target_width, target_height))
    img_tk = ImageTk.PhotoImage(img)    
    img_label.configure(image=img_tk, width=360, height=270)   
    img_label.image = img_tk                                        

    
def find_colors():
    colorthief = ColorThief(file=filename)
    palatte = colorthief.get_palette(color_count=13)

    rgb1 = palatte[0]
    color1 = f'#{rgb1[0]:02x}{rgb1[1]:02x}{rgb1[2]:02x}'
    rgb2 = palatte[1]
    color2 = f'#{rgb2[0]:02x}{rgb2[1]:02x}{rgb2[2]:02x}'
    rgb3 = palatte[2]
    color3 = f'#{rgb3[0]:02x}{rgb3[1]:02x}{rgb3[2]:02x}'
    rgb4 = palatte[3]
    color4 = f'#{rgb4[0]:02x}{rgb4[1]:02x}{rgb4[2]:02x}'
    rgb5 = palatte[4]
    color5 = f'#{rgb5[0]:02x}{rgb5[1]:02x}{rgb5[2]:02x}'
    rgb6 = palatte[5]
    color6 = f'#{rgb6[0]:02x}{rgb6[1]:02x}{rgb6[2]:02x}'
    rgb7 = palatte[6]
    color7 = f'#{rgb7[0]:02x}{rgb7[1]:02x}{rgb7[2]:02x}'
    rgb8 = palatte[7]
    color8 = f'#{rgb8[0]:02x}{rgb8[1]:02x}{rgb8[2]:02x}'
    rgb9 = palatte[8]
    color9 = f'#{rgb9[0]:02x}{rgb9[1]:02x}{rgb9[2]:02x}'
    rgb10 = palatte[9]
    color10 = f'#{rgb10[0]:02x}{rgb10[1]:02x}{rgb10[2]:02x}'
    rgb11 = palatte[10]
    color11 = f'#{rgb11[0]:02x}{rgb11[1]:02x}{rgb11[2]:02x}'
    rgb12 = palatte[11]
    color12 = f'#{rgb12[0]:02x}{rgb12[1]:02x}{rgb12[2]:02x}'
    # print(color1)

    # Color Palatte Left
    colors_left.itemconfig(c1, fill=color1)
    hex1.config(text=color1)
    colors_left.itemconfig(c2, fill=color2)
    hex2.config(text=color2)
    colors_left.itemconfig(c3, fill=color3)
    hex3.config(text=color3)
    colors_left.itemconfig(c4, fill=color4)
    hex4.config(text=color4)
    colors_left.itemconfig(c5, fill=color5)
    hex5.config(text=color5)
    colors_left.itemconfig(c6, fill=color6)
    hex6.config(text=color6)
    # Color Palette Right
    colors_right.itemconfig(c7, fill=color7)
    hex7.config(text=color7)
    colors_right.itemconfig(c8, fill=color8)
    hex8.config(text=color8)
    colors_right.itemconfig(c9, fill=color9)
    hex9.config(text=color9)
    colors_right.itemconfig(c10, fill=color10)
    hex10.config(text=color10)
    colors_right.itemconfig(c11, fill=color11)
    hex11.config(text=color11)
    colors_right.itemconfig(c12, fill=color12)
    hex12.config(text=color12)

# --------------------------------- UI SET UP -------------------------- #
window = Tk()
window.title("IMAGE COLOR DETECTOR")
window.geometry('900x500+100+100')
window.config(bg="goldenrod")
window.resizable(False, False)

# UI ICON
icon = PhotoImage(file=icon.png")
window.iconphoto(False, icon)

# BLACK GAP
black_gap = Label(window, width=140, height=10, bg='darkred')
black_gap.grid(column=0, row=1)

# COLOR PICKER FRAME
frame = Frame(window, width=800, height=400, bg='blanchedalmond')
frame.place(x=50, y=50)

# COLOR PICKER LOGO & FRAME
logo = PhotoImage(file=logo.png')
Label(frame, image=logo, bg="blanchedalmond").place(x=30, y=10)
Label(frame, text='Color Finder', font='arial 25 bold', bg='blanchedalmond').place(x=120, y=25)

# COLOR PALLATE LEFT
colors_left = Canvas(frame, bg='blanchedalmond', width=150, height=280, highlightthickness=0)
colors_left.place(x=40, y=110)

c1 = colors_left.create_rectangle((10,10,40,40), fill='black')
hex1 = Label(colors_left, text='#000000', fg='#000', font='arial 11 bold', bg='blanchedalmond')
hex1.place(x=50, y=15)

c2 = colors_left.create_rectangle((10,40,40,80), fill='black')
hex2 = Label(colors_left, text='#000000', fg='#000', font='arial 11 bold', bg='blanchedalmond')
hex2.place(x=50, y=55)

c3 = colors_left.create_rectangle((10,80,40,120), fill='black')
hex3 = Label(colors_left, text='#000000', fg='#000', font='arial 11 bold', bg='blanchedalmond')
hex3.place(x=50, y=95)

c4 = colors_left.create_rectangle((10,120,40,160), fill='black')
hex4 = Label(colors_left, text='#000000', fg='#000', font='arial 11 bold', bg='blanchedalmond')
hex4.place(x=50, y=135)

c5 = colors_left.create_rectangle((10,160,40,200), fill='black')
hex5 = Label(colors_left, text='#000000', fg='#000', font='arial 11 bold', bg='blanchedalmond')
hex5.place(x=50, y=175)

c6 = colors_left.create_rectangle((10,200,40,240), fill='black')
hex6 = Label(colors_left, text='#000000', fg='#000', font='arial 11 bold', bg='blanchedalmond')
hex6.place(x=50, y=215) 

# COLOR PALLATE RIGHT
colors_right = Canvas(frame, bg='blanchedalmond', width=150, height=280, highlightthickness=0)
colors_right.place(x=180, y=110)

c7 = colors_right.create_rectangle((10,10,40,40), fill='black')
hex7 = Label(colors_right, text='#000000', fg='#000', font='arial 11 bold', bg='blanchedalmond')
hex7.place(x=50, y=15)

c8 = colors_right.create_rectangle((10,40,40,80), fill='black')
hex8 = Label(colors_right, text='#000000', fg='#000', font='arial 11 bold', bg='blanchedalmond')
hex8.place(x=50, y=55)

c9 = colors_right.create_rectangle((10,80,40,120), fill='black')
hex9 = Label(colors_right, text='#000000', fg='#000', font='arial 11 bold', bg='blanchedalmond')
hex9.place(x=50, y=95)

c10 = colors_right.create_rectangle((10,120,40,160), fill='black')
hex10 = Label(colors_right, text='#000000', fg='#000', font='arial 11 bold', bg='blanchedalmond')
hex10.place(x=50, y=135)

c11 = colors_right.create_rectangle((10,160,40,200), fill='black')
hex11 = Label(colors_right, text='#000000', fg='#000', font='arial 11 bold', bg='blanchedalmond')
hex11.place(x=50, y=175)

c12 = colors_right.create_rectangle((10,200,40,240), fill='black')
hex12 = Label(colors_right, text='#000000', fg='#000', font='arial 11 bold', bg='blanchedalmond')
hex12.place(x=50, y=215)

# IMAGE SELECTION BOX
selection_frame = Frame(frame, width=400, height=350, bg='burlywood')
selection_frame.place(x=370, y=25)

# PIC DISPLAY
pic_frame = Frame(selection_frame, bd=3, width=370, height=280, bg='black', relief=GROOVE)
pic_frame.place(x=15, y=15)

img_label = Label(pic_frame, bg='black')
img_label.place(x=0, y=0)

# BUTTONS
selectimage_btn = Button(selection_frame, text='Select Image', width=17, height=1, font='arial 13 bold', bg="beige", command=show_image)
selectimage_btn.place(x=15, y=300)

find_colors_btn = Button(selection_frame, text='Find Colors', width=17, height=1, font='arial 13 bold', bg='beige', command=find_colors)
find_colors_btn.place(x=205, y=300)

window.mainloop()


