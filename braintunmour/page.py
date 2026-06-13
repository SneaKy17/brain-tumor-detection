from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from PIL import Image,ImageTk
root=Tk()

root.config(bg='white')
he=PhotoImage(file='brain image.png')
root.iconphoto(False,he)

root.title("Brain Tumor Detection")
head=Label(root,text="Brain Tumor Detection",bg='blue',fg='white',font=("Times New Roman", 40 ,"bold"),padx=30,pady=20,justify='center',width=40)
head.place(x=0,y=0)

frm=Frame(root,width=700,height=400,borderwidth=3,relief="solid")
frm.place(x=300,y=180)

txt=Label(frm,text="Upload image",font=("Times New Roman",30,'bold'),padx=50,pady=50)
txt.place(x=10,y=10)

def openfile():
    file=filedialog.askopenfile(filetypes=[("Image files",'*.jpg;*.jpeg;*.png')])
    if file:
        select_file.config(text=f"Selected file: {file}",font=("Times New Roman",10,'bold',"italic"),padx=40,pady=10,bg="#1E90FF",fg="black",borderwidth=1,relief="solid")
        select_file.place(x=50,y=140)

btn=Button(frm,text="Upload Files",borderwidth=1,relief="solid",padx=15,pady=5,font=("Times New Roman",20),bg="#1E90FF",fg="white",activebackground="blue",activeforeground="white",command=openfile)
btn.place(x=340,y=55)
select_file=Label(frm)
select_file.place(x=50,y=140)

'''img=ImageTk.PhotoImage(Image.open("select_file"))
lbl=Label(frm,image="img")
lbl=img.place(x=50,y=200)'''

text=Label(frm,text="Detect Tumor",font=("Times New Roman",30,'bold'),padx=50,pady=40)
text.place(x=10,y=250)

def detect_image():
    if select_file.cget("text")=="":
        messagebox.showwarning("Warning","Please select an image first")
    else:
        messagebox.showinfo("Detecting image","Image is under processing")

butn=Button(frm,text="Click Here",borderwidth=1,relief="solid",padx=20,pady=5,font=("Times New Roman",20),bg="#1E90FF",fg="white",activebackground="blue",activeforeground="white",command=detect_image)
butn.place(x=340,y=290)


mainloop()