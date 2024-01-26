from tkinter import *
from tkinter import filedialog
from tkinter.filedialog import askopenfilenames
import img2pdf

root = Tk()
root.geometry('400x200')
root.title("ImageToPDF developed by Gunjan")

def select_file():
    global file_names
    file_names = filedialog.askopenfilenames(initialdir="/", title="Select Files")

def images_to_pdf():
    with open("file.pdf", "wb") as f:
        f.write(img2pdf.convert(file_names))

Label(root, text="IMAGE CONVERSION", font="italic 15 bold").pack(pady=10)

Button(root, text="Select Images", relief="solid", command=select_file, font=14).pack(pady=10)
Button(root, text="Images To PDF", relief="solid", command=images_to_pdf, bg="white", font=15).pack(pady=10)

root.mainloop()
