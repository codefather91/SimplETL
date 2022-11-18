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
    filenameLabel.config(text=fileName)

mainFrame = tk.Frame(root, bg='gray')

filenameLabel = tk.Label(mainFrame, bg='white', text='File name')
#filenameLabel.pack(padx=10, pady=10, fill='x', expand=True, side="left")
filenameLabel.grid(row=0,column=0,padx=10,pady=10, columnspan=4)

selectFileButton = tk.Button(mainFrame, text='Select File',command=selectFile)
#selectFileButton.pack(expand=True, side="left")
selectFileButton.grid(row=0,column=4,padx=10,pady=10)

mainFrame.pack(expand=True)

root.mainloop()