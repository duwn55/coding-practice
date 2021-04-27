import tkinter

window = tkinter.Tk()
window.title("tkinter practice")
window.geometry("640x480+100+100")
window.resizable(False, False)

def flash() :
    checkbutton1.flash()

CheckVariety_1 = tkinter.IntVar()
CheckVariety_2 = tkinter.IntVar()

checkbutton1 = tkinter.Checkbutton(window, text = '0', variable = CheckVariety_1, activebackground = 'blue')
checkbutton2 = tkinter.Checkbutton(window, text = 'ㅁ', variable = CheckVariety_2)
checkbutton3 = tkinter.Checkbutton(window, text = 'x', variable = CheckVariety_2, command = flash)

checkbutton1.pack()
checkbutton2.pack()
checkbutton3.pack()

window.mainloop()