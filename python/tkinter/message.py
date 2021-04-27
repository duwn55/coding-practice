import tkinter

window = tkinter.Tk()
window.title("tkinter practice")
window.geometry("640x480+100+100")
window.resizable(False, False)

message = tkinter.Message(window, text = "메세지입니다.", width = 100, relief = 'solid')
message.pack()

window.mainloop()