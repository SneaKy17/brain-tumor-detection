import tkinter
from PIL import Image
from tkinter import filedialog
import cv2 as cv
from frames import *
from displayTumor import *
# from predictTumor import *
import subprocess

class Gui:
    MainWindow = 0
    listOfWinFrame = list()
    FirstFrame = object()
    val = 0
    fileName = 0
    DT = object()

    wHeight = 700
    wWidth = 1180

    def __init__(self):
        global MainWindow
        MainWindow = tkinter.Tk()
        MainWindow.geometry('1200x720')
        MainWindow.resizable(width=False, height=False)

        self.DT = DisplayTumor()

        self.fileName = tkinter.StringVar()

        self.FirstFrame = Frames(self, MainWindow, self.wWidth, self.wHeight, 0, 0)
        self.FirstFrame.btnView['state'] = 'disable'

        self.listOfWinFrame.append(self.FirstFrame)

        WindowLabel = tkinter.Label(self.FirstFrame.getFrames(), text="Brain Tumor Detection", height=1, width=40)
        WindowLabel.place(x=0, y=0)
        WindowLabel.configure(bg="blue",fg='white', font=("Times New Roman", 40, "bold"),justify="center",pady=20)

        browseBtn = tkinter.Button(self.FirstFrame.getFrames(), text="Upload Image", font=("Times New Roman",10,'bold'),width=25, command=self.browseWindow,bg="gray",fg='white',borderwidth=1,relief="solid",pady=5,padx=5)
        browseBtn.place(x=300, y=200)
        
        
        self.val = tkinter.IntVar()
        RB1 = tkinter.Radiobutton(self.FirstFrame.getFrames(), text="Detect Tumor", variable=self.val,font=("Times New Roman",20,'bold'),value=1, command=self.check)
        RB1.place(x=150, y=250)
        RB2 = tkinter.Radiobutton(self.FirstFrame.getFrames(), text="View Tumor Region",variable=self.val, value=2, command=self.check,font=("Times New Roman",20,'bold'))
        RB2.place(x=400, y=250)
        RB3 =  tkinter.Radiobutton(self.FirstFrame.getFrames(), text="Symptoms", variable=self.val,font=("Times New Roman",20,'bold'),value=3,command = self.symp)
        RB3.place(x=150,y=310)


        MainWindow.mainloop()

    def getListOfWinFrame(self):
        return self.listOfWinFrame

    def browseWindow(self):
        global mriImage
        FILEOPENOPTIONS = dict(defaultextension='*.*',
                               filetypes=[('jpg', '*.jpg'), ('png', '*.png'), ('jpeg', '*.jpeg'), ('All Files', '*.*')])
        self.fileName = filedialog.askopenfilename(**FILEOPENOPTIONS)
        image = Image.open(open(self.fileName, 'rb'))
        imageName = str(self.fileName)
        mriImage = cv.imread(imageName, 1)
        self.listOfWinFrame[0].readImage(image)
        self.listOfWinFrame[0].displayImage()
        self.DT.readImage(image)
    def symp(self):
        subprocess.call(["python","tumorsymptoms.py"])

    def check(self):
        global mriImage
        #print(mriImage)
        if (self.val.get() == 1):
            self.listOfWinFrame = 0
            self.listOfWinFrame = list()
            self.listOfWinFrame.append(self.FirstFrame)

            self.listOfWinFrame[0].setCallObject(self.DT)

            # res = predictTumor(mriImage)
            
            # if res > 0.5:
            #     resLabel = tkinter.Label(self.FirstFrame.getFrames(), text="Tumor Detected", height=1, width=20)
            #     resLabel.configure(background="White", font=("Cambria", 16, "bold"), fg="red")
            # else:
            #     resLabel = tkinter.Label(self.FirstFrame.getFrames(), text="No Tumor", height=1, width=20)
            #     resLabel.configure(background="White", font=("Cambria", 16, "bold"), fg="green")

            # resLabel.place(x=700, y=420)

        elif (self.val.get() == 2):
            self.listOfWinFrame = 0
            self.listOfWinFrame = list()
            self.listOfWinFrame.append(self.FirstFrame)

            self.listOfWinFrame[0].setCallObject(self.DT)
            self.listOfWinFrame[0].setMethod(self.DT.removeNoise)
            secFrame = Frames(self, MainWindow, self.wWidth, self.wHeight, self.DT.displayTumor, self.DT)

            self.listOfWinFrame.append(secFrame)


            for i in range(len(self.listOfWinFrame)):
                if (i != 0):
                    self.listOfWinFrame[i].hide()
            self.listOfWinFrame[0].unhide()

            if (len(self.listOfWinFrame) > 1):
                self.listOfWinFrame[0].btnView['state'] = 'active'

        else:
            print("Not Working")

mainObj = Gui()