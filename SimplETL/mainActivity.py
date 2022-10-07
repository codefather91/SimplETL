import tkinter as tk
from tkinter import filedialog as fd

app_start = 0

root = tk.Tk()
root.geometry('1024x768')
root.title('SimplETL v1.0')
root.resizable(False, False)

def selectFile():
    fileTypes = (('Text Files', '*.txt'), ('Comma Separated Files', '*.csv'),('All Files','*.*'))
    fileName = fd.askopenfilename(title='Select File', initialdir='.',filetypes=fileTypes)
    FileNameLabel.config(text=fileName)

mainFrame = tk.Frame(root, bg='gray')
mainFrame.pack(fill="both", expand=True)

status = tk.Label(root, text="SimplETL tool ready", relief='sunken', anchor=tk.W, bd=1)
status.pack(side="bottom", fill='x')

SelectionBox = tk.Frame(mainFrame, bg='red')
SelectionBox.pack(padx=10, pady=(10, 0),fill="both",expand=True)

FileNameLabel = tk.Label(SelectionBox, bg='white', text='File name')
FileNameLabel.pack(padx=10, pady=10, fill='x', expand=True, side="left")
SelectFileButton = tk.Button(SelectionBox, text='Select File',command=selectFile)
SelectFileButton.pack(expand=True, side="left")
ConfirmFileButton = tk.Button(SelectionBox, text='Proceed')
ConfirmFileButton.pack(expand=True, side="left")

MetadataBox = tk.Frame(mainFrame, bg='green')
MetadataBox.pack(padx=10, pady=(10, 0),fill="both",expand=True)

root.mainloop()