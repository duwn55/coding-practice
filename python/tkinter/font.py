from tkinter import *
import tkinter.font

window = Tk()
window.title("tkinter practice")
window.geometry("640x480+100+100")
window.resizable(False, False)

font_1 = tkinter.font.Font(family = "맑은 고딕", size = 20, slant = "italic")

label = Label(window, text = "파이썬 3.6", font = font_1)
label.pack()

window.mainloop()