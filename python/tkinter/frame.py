import tkinter

window = tkinter.Tk()
window.title("tkinter practice")
window.geometry("640x480+100+100")
window.resizable(False, False)

frame_1 = tkinter.Frame(window, relief = 'solid', bd = 2)
frame_1.pack(side = "left", fill = "both", expand = True)

frame_2 = tkinter.Frame(window, relief = 'solid', bd = 2)
frame_2.pack(side = "right", fill = "both", expand = True)

button_1 = tkinter.Button(frame_1, text = "프레임1")
button_1.pack(side = "right")

button_2 = tkinter.Button(frame_2, text = "프레임2")
button_2.pack(side = "left")

window.mainloop()