import tkinter as tk
from tkinter import filedialog
import os
import shutil
from functools import partial
from tkinter import *
import glob
from tkinter import messagebox

root = tk.Tk()
var = tk.StringVar()


def createTxt(destinationFolder, fileType):
    print(destinationFolder)
    print(fileType)
    os.chdir(destinationFolder)
    files = glob.glob('*.' + fileType)
    with open('files_list.txt', 'w') as in_files:
        in_files.writelines(os.path.join(
            destinationFolder, fn) + '\n' for fn in files)


def getInput():

    global newValue
    newValue = value.get()


def source():
    global source
    source = filedialog.askdirectory()


canvas2 = tk.Canvas(root, width=300, height=350,
                    bg='lightsteelblue2', relief='raised')
canvas2.pack()

sourceDirectoryNew = Button(root, text="      Source Directory     ",
                            command=source, bg='green', fg='white', font=('helvetica', 12, 'bold'))
canvas2.create_window(150, 50, window=sourceDirectoryNew)

Label(root, text='File Type:').place(x=35, y=75)

value = Entry(root, textvariable=var).place(x=100, y=75)


loadType = Button(root, text="      Load file type     ",
                  command=getInput, bg='green', fg='white', font=('helvetica', 12, 'bold'))

canvas2.create_window(150, 120, window=loadType)

createTXTFile = tk.Button(root, text="      Create TXT     ",
                          command=lambda: createTxt(source, fileType), bg='green', fg='white', font=('helvetica', 12, 'bold'))
canvas2.create_window(150, 160, window=createTXTFile)


root.mainloop()
