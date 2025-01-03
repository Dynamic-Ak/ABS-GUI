
from tkinter import *
from PIL import  ImageTk, Image

def every_100(text):
    final_text = ""
    for i in range(0, len(text)):
        final_text +=text[i]
        if i%100==0 and i!=0:
            final_text += "\n"
    return final_text

root = Tk()
root.title("Honest Articles - Aapka Apna Akhabaar")
root.geometry("782x680")
root.wm_iconbitmap("docs\\4.ico")

texts = []
photos = []
#that call and open in read mode of txt files
for i in range(0, 2):
    with open(f"docs\\{i+1}.txt") as f:
        text = f.read()
        texts.append(every_100(text))

    image = Image.open(f"docs\\{i+1}.jpeg")
    #TODO: Resize these images
    image = image.resize((250, 270), Image.ANTIALIAS)
    photos.append(ImageTk.PhotoImage(image))

f0 = Frame(root, width=80, height=70)
Label(f0, text="Technical News", font="lucida 33 bold",fg='yellow',bg='black').pack()
Label(f0, text="April 16, 2021", font="Ascade 13 bold").pack()
f0.pack()

f8 = Frame(root)
Label(f8, text="1",fg='white',bg='blue').pack()
f8.pack()

f1 = Frame(root, width=0, height=0, pady=0)
Label(f1, text=texts[0], padx=0, pady=0).pack(side="right")
Label(f1, image=photos[0], anchor="e").pack()
f1.pack(anchor="w")

f8 = Frame(root)
Label(f8, text="2",fg='white',bg='green').pack()
f8.pack()

f2 = Frame(root, width=0, height=0, pady=0, padx=0)
Label(f2, text=texts[1], padx=0, pady=0).pack(side="left")
Label(f2, image=photos[1], anchor="e", padx=2).pack()
f2.pack(anchor="w")

root.mainloop()