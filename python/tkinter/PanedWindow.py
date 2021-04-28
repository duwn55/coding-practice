from tkinter import *

window = Tk()
window.title("tkinter practice")
window.geometry("640x480+100+100")
window.resizable(False, False)

panedwindow_1 = PanedWindow(relief = 'raised', bd = 2)
panedwindow_1.pack(expand = True)

left = Label(panedwindow_1, text = '내부윈도우-1 (좌측)')
panedwindow_1.add(left)

panedwindow_2 = PanedWindow(panedwindow_1, orient = "vertical", relief = "groove", bd = 3)
panedwindow_1.add(panedwindow_2)

right = Label(panedwindow_1, text = "내부윈도우-2 (우측)")
panedwindow_1.add(right)

top = Label(panedwindow_2, text = "내부윈도우-3 (상단)")
panedwindow_2.add(top)

bottom = Label(panedwindow_2, text = "내부윈도우-4 (하단)")
panedwindow_2.add(bottom)

window.mainloop()