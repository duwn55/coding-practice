from tkinter import *

window = Tk()
window.title("tkinter practice")
window.geometry("640x480+100+100")
window.resizable(True, True)

image = PhotoImage(file = 'one.gif')

label = Label(window, image = image)
label.pack()

window.mainloop()