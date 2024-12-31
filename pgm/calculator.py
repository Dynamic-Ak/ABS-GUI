from tkinter import *
root=Tk()
root.geometry('262x511')
root.resizable(False,False)
root.title("ABS's calculator")
root.wm_iconbitmap("docs\\c1.ico")
root.configure(background='turquoise')
#functions
def click(event):
    global scvalue # here "scvalue" make globalise that can use in function
    
    #that give the value of button clicked 
    text=event.widget.cget('text')
    print(text)
    if text=='P':
        text='**'
        
    if text =='=':
        if scvalue.get().isdigit():
            value=int(scvalue.get())
        else:
            try:
                value=eval(screen.get())
            except Exception as e:
                print(e)
                value='Error'
        scvalue.set(value)
        screen.update()
        
    elif text =='C':
        scvalue.set("")# here scvalue is now blank
        screen.update()
    else:
        scvalue.set(scvalue.get()+text)
        screen.update() # here screen is update

scvalue=StringVar()
scvalue.set('')
#entry box and screen
screen=Entry(root,textvar=scvalue,font='lucida 20 bold',relief=SOLID,
borderwidth=5)
screen.pack(fill=X,ipadx=8,pady=10,padx=10)


#  frames of calc
f=Frame(root)
f.pack()
#buttons creation
###############1################
b=Button(f,text='9',padx=5,pady=5,font='lucida 30 bold',fg='brown')
b.bind('<Button-1>',click)
b.pack(side=LEFT)
b=Button(f,text='8',padx=5,pady=5,font='lucida 30 bold',fg='orange')
b.bind('<Button-1>',click)
b.pack(side=LEFT)
b=Button(f,text='7',padx=5,pady=5,font='lucida 30 bold',fg='red')
b.bind('<Button-1>',click)
b.pack(side=LEFT)
b=Button(f,text='=',padx=5,pady=6,font='lucida 30 bold',fg='black',bg='lime')
b.bind('<Button-1>',click)
b.pack(side=LEFT)
################2#################
f=Frame(root)
f.pack()
b=Button(f,text='6',padx=5,pady=5,font='lucida 30 bold',fg='green')
b.bind('<Button-1>',click)
b.pack(side=LEFT)
b=Button(f,text='5',padx=5,pady=5,font='lucida 30 bold',fg='blue')
b.bind('<Button-1>',click)
b.pack(side=LEFT)
b=Button(f,text='4',padx=5,pady=5,font='lucida 30 bold',fg='purple')
b.bind('<Button-1>',click)
b.pack(side=LEFT)
b=Button(f,text='C',padx=3,pady=6,font='lucida 30',fg='red',bg='pink')
b.bind('<Button-1>',click)
b.pack(side=LEFT)
#################3################
f=Frame(root)
f.pack()
b=Button(f,text='3',padx=5,pady=5,font='lucida 30 bold',fg='violet')
b.bind('<Button-1>',click)
b.pack(side=LEFT)
b=Button(f,text='2',padx=5,pady=5,font='lucida 30 bold',fg='grey')
b.bind('<Button-1>',click)
b.pack(side=LEFT)
b=Button(f,text='1',padx=5,pady=5,font='lucida 30 bold',fg='skyblue')
b.bind('<Button-1>',click)
b.pack(side=LEFT)
b=Button(f,text='0',padx=5,pady=5,font='lucida 30 bold',fg='brown')
b.bind('<Button-1>',click)
b.pack(side=LEFT)
##################4#####################
f=Frame(root)
f.pack()
b=Button(f,text='.',padx=10,pady=5,font='lucida 30 bold',fg='teal')
b.bind('<Button-1>',click)
b.pack(side=LEFT)
b=Button(f,text='P',padx=3,pady=5,font='lucida 30 bold',fg='orange')
b.bind('<Button-1>',click)
b.pack(side=LEFT)
b=Button(f,text='(',padx=9,pady=5,font='lucida 30 bold',fg='red')
b.bind('<Button-1>',click)
b.pack(side=LEFT)
b=Button(f,text=')',padx=10,pady=5,font='lucida 30 bold',fg='black')
b.bind('<Button-1>',click)
b.pack(side=LEFT)
#################5#################
f=Frame(root,bg='red')
f.pack()
b=Button(f,text='/',padx=10,pady=5,font='lucida 30 bold',fg='olive')
b.bind('<Button-1>',click)
b.pack(side=LEFT)
b=Button(f,text='*',padx=8,pady=5,font='lucida 30 bold',fg='maroon')
b.bind('<Button-1>',click)
b.pack(side=LEFT)
b=Button(f,text='-',padx=9,pady=5,font='lucida 30 bold',fg='cyan')
b.bind('<Button-1>',click)
b.pack(side=LEFT)
b=Button(f,text='+',padx=5,pady=5,font='lucida 30 bold',fg='gold')
b.bind('<Button-1>',click)
b.pack(side=LEFT)

root.mainloop()
