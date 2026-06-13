from tkinter import *
from PIL import ImageTk,Image


root=Tk()
root.geometry("1300x1000")
root.maxsize(1300,1000)

root.title="brain tumor detector app"
root["bg"]="teal"

lbl1=Label(root,text="BRAIN    TUMOR   DETECTION    APP",font="Harrington 30 bold",bg="teal",fg="white")
lbl1.pack()





# lbl1=Label(root,text="BRAIN    TUMOR   DETECTION    APP",font="Harrington 30 bold",bg="teal",fg="white")
# lbl1.pack()

btn1=Button(root,text='BROWSE IMAGE',font='Harrington 18 bold',bg="peachpuff")
btn1.place(x=100,y=80)
btn2=Button(root,text='DETECTION',font='Harrington 18 bold',bg="peachpuff",padx=50)
btn2.place(x=400,y=80)
btn3=Button(root,text='RESET',font='Harrington 18 bold',bg="peachpuff",padx=60)
btn3.place(x=730,y=80)
btn4=Button(root,text='EXIT',font='Harrington 18 bold',bg="peachpuff",padx=60)
btn4.place(x=1010,y=80)


frm3=Frame(root,width=560,height=400,bd=2,highlightbackground="peachpuff" ,relief='solid',bg='teal',highlightthickness=2)
frm3.place(x=340,y=180)
# lblfr3=Label(root,text='Preprocessing',font='aial 16 bold',bg='peachpuff')
# lblfr3.place(x=390,y=510)
# frm4=Frame(root,width=280,height=300,bd=2,highlightbackground="peachpuff" ,relief='solid')
# frm4.place(x=680,y=200)
# lblfr4=Label(root,text='Segmentation',font='aial 16 bold',bg='peachpuff')
# lblfr4.place(x=740,y=510)
img_path= Image.open("oi.jpg")
resize= img_path.resize((560,400))
resize_img= ImageTk.PhotoImage(resize)
img_lbl=Label(frm3,image=resize_img)
img_lbl.pack()




a= IntVar()

radiobutton1 = Radiobutton(root, text="DETECT TUMOR", variable=a, value=1,font=' Roboto 20 bold',bg="teal",padx=20,fg="white")
radiobutton1.place(x=200,y=600)

radiobutton2 = Radiobutton(root, text="VIEW TUMOR REGION", variable=a, value=2, font='Harrington 20 bold',bg="teal",fg="white")
radiobutton2.place(x=800,y=600)

lb2=Label(root,text="DETECTION RESULT::::" ,font="Harrington 20 bold",bg="teal",fg="white")
lb2.place(x=290,y=700)
entdata=Frame(root,width=40,height=2,bg='teal')
entdata.place(x=660,y=700)



mainloop()