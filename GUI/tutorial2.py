from tkinter import*
from PIL import Image, ImageTk
yashg_root = Tk()

yashg_root.geometry("455x255")

# photo = PhotoImage(file="1.png")

#for jpg images 
image = Image.open("IMG_20190210_134029.jpg")
photo = ImageTk.PhotoImage(image)

varun_lable = Label(image=photo)
varun_lable.pack()

yashg_root.mainloop()