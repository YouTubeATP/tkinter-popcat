## Tkinter for UI things
import tkinter as tk
from tkinter import Button, Label

## pygame mixer for audio playing
from pygame import mixer

## Pillow for showing image
from PIL import Image, ImageTk

## Initialize toplevel widget
top = tk.Tk()
top.iconbitmap("assets/icon.ico")
top.geometry("800x930")
top.title("POPCAT")

mixer.init()

## Make toplevel widget a label
t_label = Label(top, text="0", font=("Nunito Black", 40))
t_label.pack(pady=5)

count = 0

def on_click():
    ## Change text
    global count
    count += 1
    t_label.configure(text=str(count), font=("Nunito Black", 40))
    
    ## Change image
    global photo1
    photo1 = ImageTk.PhotoImage(Image.open("assets/open.png"))
    button.configure(image=photo1)
    
    top.update()
    
    ## Play sound
    mixer.music.load("assets/pop.mp3")
    mixer.music.play()
    
    ## Change image back
    global photo2
    photo2 = ImageTk.PhotoImage(Image.open("assets/close.png"))
    button.configure(image=photo2)
    
    top.update()

im = ImageTk.PhotoImage(Image.open("assets/close.png"))
im_label = Label(image=im)
button = Button(top, image=im, command=lambda:on_click(), borderwidth=0)
button.pack(pady=30)

top.mainloop()