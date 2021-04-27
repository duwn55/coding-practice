from tkinter import *
window = Tk()

window.title("Number Baseball")
window.geometry("640x400+200+100")      #640x400은 화면 크기,200,100은 초기 윈도우 위치 
window.resizable(False, False)

label_1 = Label(window, text = "파이썬", width = 5, height = 2, fg = "red", relief = "solid")
label_1.grid(row = 0, column = 0)

count = 0

def  countUP() :
    global count
    count += 1
    label_2.config( text = str(count) )

label_2 = Label(window, text = '0')
label_2.grid(row = 1, column = 0)

button_image_1 = PhotoImage(file = "one.gif")
button_1 = Button(window, image = button_image_1, overrelief = "solid", width = 60, height = 80, command = countUP, repeatdelay = 1000, repeatinterval = 100 )
button_1.grid(row = 2, column = 3)

window.mainloop()