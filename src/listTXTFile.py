#!/usr/bin/env python3
import tkinter as tk
from tkinter import filedialog
import os
import shutil
from functools import partial
from tkinter import *
import glob
from tkinter import messagebox


def save_text():
    global text
    label_text.set(f'Type: {entry_text.get()}')
    print(entry_text.get())
    text = entry_text.get()
    print(text)


def createTxt(destinationFolder, fileType):
    print(destinationFolder)
    print(fileType)
    os.chdir(destinationFolder)
    files = glob.glob('*.' + fileType)
    print(files)
    with open('files_list.txt', 'w') as in_files:
       in_files.writelines(os.path.join(fn) + '\n' for fn in files)

    messagebox.showinfo(
        "Information",  "TXT File Created!")


def source():
    global source
    source = filedialog.askdirectory()


root = tk.Tk()

canvas2 = tk.Canvas(root, width=300, height=350,
                    bg='lightsteelblue2', relief='raised')
canvas2.pack()

sourceDirectoryNew = Button(root, text="      Source Directory     ",
                            command=source, bg='green', fg='white', font=('helvetica', 12, 'bold'))
canvas2.create_window(150, 50, window=sourceDirectoryNew)


label_text = tk.StringVar()
label = tk.Label(root, textvariable=label_text)
label.place(x=195, y=75)


entry_text = tk.StringVar()
entry = tk.Entry(root, width=10, textvariable=entry_text)
entry.place(x=120, y=75)

headline = Label(root, text='Enter File Type:')
headline.place(x=30, y=75)

createTXTFile = tk.Button(root, text="      Create TXT     ",
                          command=lambda: createTxt(source, text), bg='green', fg='white', font=('helvetica', 12, 'bold'))
canvas2.create_window(150, 160, window=createTXTFile)


button = tk.Button(root, text="Load file type", command=save_text,
                   bg='green', fg='white', font=('helvetica', 12, 'bold'))
canvas2.create_window(150, 120, window=button)


root.mainloop()

