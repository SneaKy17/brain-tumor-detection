from tkinter import *
from PIL import Image,ImageTk
from tkinter.ttk import *
import subprocess
root=Tk()
root.geometry('1000x800')
root.maxsize(1000,800)

'''root.config(bg='white')
he=PhotoImage(file='brain image.png')
root.iconphoto(False,he)'''

def you():
    subprocess.call(['python','youtubecon.py'])
Label_title=Label(root,text='Brain Tumor Detection',font='arial 30 bold',borderwidth=2,relief='solid',width=30)
Label_title.pack(pady=20)

frm=Frame(root,width=300,height=400)
frm.place(x=60,y=150)
img=ImageTk.PhotoImage(Image.open('0.jpg'))
img_label=Label(frm,image=img)
img_label.pack()
frm2=Frame(root,width=500,height=250)
frm2.place(x=400,y=150)

you_con=Button(root,text='Youtube convertor',command=you)
you_con.place(x=60,y=500)
fb_con=Button(root,text='Facebook convertor')
fb_con.place(x=400,y=500)
insta_con=Button(root,text='Instagram convertor')
insta_con.place(x=740,y=500)

root.mainloop()