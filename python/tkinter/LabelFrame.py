from tkinter import *

window = Tk()
window.title("tkinter practice")
window.geometry("640x480+100+100")
window.resizable(False, False)

def check() :
    label.config(text = RadioVariety_1.get())

labelframe = LabelFrame(window, text = "플랫폼 선택")
labelframe.pack()

RadioVariety_1 = StringVar()
RadioVariety_1.set("미선택")

radio_1 = Radiobutton(labelframe, text = 'Python', value = '가능', variable = RadioVariety_1, command = check)
radio_1.pack()
radio_2 = Radiobutton(labelframe, text = 'C/C++', value = '부분 가능', variable = RadioVariety_1, command = check)
radio_2.pack()
radio_3 = Radiobutton(labelframe, text = 'JSON', value = '불가능', variable = RadioVariety_1, command = check)
radio_3.pack()

label = Label(labelframe, text = "None")
label.pack()

window.mainloop()