from fileinput import filename
import tkinter as tk
from tkinter import filedialog, Text
import os

from click import open_file

root = tk.Tk()

def addApp():
    filename = filedialog.askopenfilename(initialdir="/", title="Select File",
    filetypes=(("All Files", "*.*"), ("Text Documents", "*.txt", "*.docx"), 
                ("Images", "*.jpg", "*.jpeg", "*.png" "*.gif", "*.heic" "*.svg")
                ("Videos", "*.mp4", "*.mov", "*.hvec"), 
                ("Microsoft Office Files", "*.docx", "*.pptx", "*.docm", "*.doc", "*.dot", "*.wbk", "*.dotx", 
                "*.dotm", "*.docb", "*.pdf", "*.wll", "*.wwl", "*.xps", "*.pub", "*.ecf", "*.one", 
                "*.AACDA", "*.ACCDB","*.ACCDE", "*.ACCDT", "*.ACCDR", "*.ACCDU", "*.MDA", "*.MDE"
                "*.ppt", "*.pot", "*.pps", "*.ppa", "*.ppam", "*.pptm", "*.potx", "*.potm", "*.ppam", "*.ppsx", "*.ppsm", 
                "*.sldx", "*.sldm" "*.pa", "*.xls", "*.xlt", "*.xlm", "*.xll_", "*.xla_", "*.xla5", "*.xla8", "*.xlsx", 
                ".xlsm", "*.xltx", "*.xltm", "*.xlsb", "*.xla", "*.xlam", "*.xll", "*.xlw")))

canvas = tk.Canvas (root, height=745, width=1150, bg="#263D42")
canvas.pack()

frame = tk.Frame(root, bg="White")
frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

openFile = tk.Button(root, text="Open File", padx=10,
                    pady=5, fg="white", bg="#263D24", command=addApp)
openFile.pack()

runFiles = tk.Button(root, text="Run Selected Files", padx=10,
                    pady=5, fg="white", bg="#263D24")
runFiles.pack()

root.mainloop()
