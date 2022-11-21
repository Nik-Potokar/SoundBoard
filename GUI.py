#Importing the tkinter library
#Importing keyboard libary
#importing winsound libary for our sound effects
#importing pynput
from tkinter import *
from pynput.keyboard import Key, Listener
from tkinter.ttk import *
import winsound
import keyboard

win= Tk()
win.title("SoundBoard")
win.geometry("700x400")


#GUI Buttons functions
def soundeffect1():
    winsound.PlaySound("sound1.wav", winsound.SND_ASYNC)

def soundeffect2():
    winsound.PlaySound("sound2.wav", winsound.SND_ASYNC)

def soundeffect3():
    winsound.PlaySound("sound3.wav", winsound.SND_ASYNC)

def soundeffect4():
    winsound.PlaySound("sound4.wav", winsound.SND_ASYNC)

def soundeffect5():
    winsound.PlaySound("sound5.wav", winsound.SND_ASYNC)

def soundeffect6():
    winsound.PlaySound("sound6.wav", winsound.SND_ASYNC)

def soundeffect7():
    winsound.PlaySound("sound7.wav", winsound.SND_ASYNC)

def soundeffect8():
    winsound.PlaySound("sound8.wav", winsound.SND_ASYNC)

def soundeffect9():
    winsound.PlaySound("sound9.wav", winsound.SND_ASYNC)


#Keybinds NUMPAD 1-9
def key_press(e):
    if keyboard.is_pressed("num_1"):
        winsound.PlaySound("sound1.wav", winsound.SND_ASYNC)
    if keyboard.is_pressed("num_2"):
        winsound.PlaySound("sound2.wav", winsound.SND_ASYNC)
    if keyboard.is_pressed("num_3"):
        winsound.PlaySound("sound3.wav", winsound.SND_ASYNC)
    if keyboard.is_pressed("num_4"):
        winsound.PlaySound("sound4.wav", winsound.SND_ASYNC)
    if keyboard.is_pressed("num_5"):
        winsound.PlaySound("sound5.wav", winsound.SND_ASYNC)
    if keyboard.is_pressed("num_6"):
        winsound.PlaySound("sound6.wav", winsound.SND_ASYNC)
    if keyboard.is_pressed("num_7"):
        winsound.PlaySound("sound7.wav", winsound.SND_ASYNC)
    if keyboard.is_pressed("num_8"):
        winsound.PlaySound("sound8.wav", winsound.SND_ASYNC)
    if keyboard.is_pressed("num_9"):
        winsound.PlaySound("sound9.wav", winsound.SND_ASYNC)
        
win.bind('<KeyPress>',key_press)

# Create style Object
style = Style()
 
#Style that will apply to widgets.
style.configure('TButton', font =
               ('calibri', 20, 'bold',),
                foreground = 'darkblue',
                background = 'black')

#Configure Rows and column
Grid.columnconfigure(win,0,weight=1)
Grid.rowconfigure(win, 1,weight=1)
Grid.columnconfigure(win,1,weight=1)
Grid.rowconfigure(win, 2,weight=1)
Grid.columnconfigure(win,2,weight=1)
Grid.rowconfigure(win, 3,weight=1)
 
#Create buttons 
b1= Button(win, text= "Sound Effect 1", command =soundeffect1)
b2= Button(win, text= "Sound Effect 2", command =soundeffect2)
b3= Button(win, text= "Sound Effect 3", command =soundeffect3)
b4= Button(win, text= "Sound Effect 4", command =soundeffect4)
b5= Button(win, text= "Sound Effect 5", command =soundeffect5)
b6= Button(win, text= "Sound Effect 6", command =soundeffect6)
b7= Button(win, text= "Sound Effect 7", command =soundeffect7)
b8= Button(win, text= "Sound Effect 8", command =soundeffect8)
b9= Button(win, text= "Sound Effect 9", command =soundeffect9)

#Create List of buttons
bl= [b1, b2, b3, b4, b5, b6, b7, b8, b9]

#Adjust the position in grid and make them sticky
b1.grid(row=1, column=0, sticky= "nsew")
b2.grid(row=1, column=1, stick= "nsew")
b3.grid(row=1, column=2, stick= "nsew")

b4.grid(row=2, column=0, stick= "nsew")
b5.grid(row=2, column=1, stick= "nsew")
b6.grid(row=2, column=2, stick= "nsew")

b7.grid(row=3, column=0, stick= "nsew")
b8.grid(row=3, column=1, stick= "nsew")
b9.grid(row=3, column=2, stick= "nsew")

win.mainloop()
