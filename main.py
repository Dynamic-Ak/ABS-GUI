#IMPORTING MODULES
from time import strftime
import os
from tkinter import *
import tkinter.messagebox as tmsg


root=Tk()
root.geometry('758x402') #geometry
root.resizable(0,0) #restricted size
root.title("5 PROJECTS USING TKINTER & PYGAME <<<") #title
root.wm_iconbitmap("docs\\8.ico") #icon
root.configure(background='black',borderwidth=5,  highlightthickness=5, highlightcolor="blue") #bg colour

#buttons command
def program():
    os.startfile('pgm\\calculator.py')
def program1():
    os.startfile('pgm\\reg_form.py')
def program2():
    os.startfile('pgm\\newsarticle.py')
def program3():
    os.startfile('pgm\\notepad.py')
def program4():
    os.startfile("snake game\\Snake.py")

#menubar_functions
def Help():
    tmsg.showinfo('Help!','We will help You soon.')
def rate():
    print('Rate us')
    value=tmsg.askquestion('Rate us',"Did you enjoy Our App ?")
    print(value)
    if value=="yes":
        msg='Great! rate us please'
    else:
        msg="Tell us what went wrong. We will call you soon"
    tmsg.showinfo('Experience',msg)

##time function
def time():
    string=strftime('%H:%M:%S %p')
    label.config(text=string)
    label.after(1000,time)

#menubars
mainmenu=Menu(root)
m1=Menu(mainmenu)
mainmenu.add_command(label='Exit',command=quit)

m3=Menu(mainmenu,tearoff=0)
m3.add_command(label='Help',command=Help)
m3.add_command(label='Rate us',command=rate)

root.config(menu=mainmenu)
mainmenu.add_cascade(label='Help',menu=m3)

#button:1
b2=Button(root,text='Snake Game',bg='red',fg='yellow',font=('OCR A Extended',16), \
    relief=RIDGE,command=program4)
b2.grid(row=0,column=2, padx=10,pady=10)
#button:2
b3=Button(root,text='GUI Notepad',bg='yellow',fg='magenta2',font=('OCR A Extended',16), \
    relief=RIDGE,command=program3)
b3.grid(row=1,column=2, padx=10,pady=10)
#button:3
b1=Button(root,text='News letter',bg='springgreen3',fg='black',font=('OCR A Extended',16), \
    relief=RIDGE,command=program2)
b1.grid(row=2,column=2, padx=10,pady=10)
#button:4
b4=Button(root,text='GUI Calculator',bg='purple',fg='white',font=('OCR A Extended',16), \
    relief=RIDGE,command=program)
b4.grid(row=3,column=2, padx=10,pady=10)
#button:5
b5=Button(root,text='Registration Form',bg='pink',fg='blue',font=('OCR A Extended',16), \
    relief=RIDGE,command=program1)
b5.grid(row=4,column=2, padx=10,pady=10)

#status as note
statusvar=StringVar()
statusvar.set('To Run Program Simply Once >Click< On It')
sbar=Label(root,textvariable=statusvar,bg='black',fg='light green',
relief=FLAT,anchor='w')
sbar.grid(row=5,column=1,pady=45,padx=2)
#created
statusvar=StringVar()
statusvar.set('*Created by: A.B.S group of 12(A) S.O.E 2021 ')
sbar=Label(root,textvariable=statusvar,bg='black',fg='white',
relief=FLAT,anchor='w')
sbar.grid(row=5,column=3)

#time 
label=Label(root,font=('LCDMono2',20),bg='black',fg='blue')
label.grid(row=0,column=3)
time() #function called

root.mainloop()
