from tkinter import *
from tkinter import messagebox
import os

def checkbox() :
    if chk.get() == 0 :
        messagebox.showinfo("", "체크버튼이 꺼졌어요.")
    else :
        messagebox.showinfo("", "체크버튼이 켜졌어요.")

def radio_button() :
    if var.get() == 1 :
        label_5.configure(text = "파이썬")
    elif var.get() == 2 :
        label_5.configure(text = "C++")
    else :
        label_5.configure(text = "Java")

window = Tk()
window.title("Number Baseball")
window.geometry("400x600")
window.resizable(width = FALSE, height = FALSE)     #window size수정 불가

photo = PhotoImage(file = "python\morning.gif")

label_1 = Label(window, text = "Cookbook~~ Python을")
label_2 = Label(window, text = "열심히", font = ("궁서체", 30), fg = "blue")    #font 글꼴과 크기 지정, fg(foreground)글자색지정
label_3 = Label(window, text = "공부 중입니다.", bg = "magenta", width = 20, height = 5, anchor = SE)   #bg(background)배경색지정 / width, height 위젯의 폭과 높이 / anchor 위젱이 어느 위치에 자리 잡을지
label_4 = Label(window, image = photo)

label_1.pack()         #해당 label을 화면에 표시
label_2.pack() 
label_3.pack() 
#label_4.pack() 

button_1 = Button(window, text = "파이썬 종료", fg = "red", command = quit)

button_1.pack() 

chk = IntVar()
cb1 = Checkbutton(window, text = "클릭하세요", variable = chk, command = checkbox)

cb1.pack()

var = IntVar()
rb1 = Radiobutton(window, text = "파이썬", variable = var, value = 1, command = radio_button)
rb2 = Radiobutton(window, text = "C++", variable = var, value = 2, command = radio_button)
rb3 = Radiobutton(window, text = "Java", variable = var, value = 3, command = radio_button)

label_5 = Label(window, text="선택한 언어 : ", fg="red")

rb1.pack()
rb2.pack()
rb3.pack()
label_5.pack()


window.mainloop()

print(os.path.dirname(os.path.realpath(__file__)))