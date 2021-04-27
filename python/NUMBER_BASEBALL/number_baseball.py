from tkinter import *
import random

##########     TKINTER 구현
window = Tk()
window.title('NUMBER BASEBALL')
window.geometry('690x480+200+200')
window.resizable(False, False)

B1 = tkinter.Intvar()

image_1 = PhotoImage(file = 'one.gif')
image_2 = PhotoImage(file = 'two.gif')
image_3 = PhotoImage(file = 'three.gif')
image_4 = PhotoImage(file = 'four.gif')
image_5 = PhotoImage(file = 'five.gif')
image_6 = PhotoImage(file = 'six.gif')
image_7 = PhotoImage(file = 'seven.gif')
image_8 = PhotoImage(file = 'eight.gif')
image_9 = PhotoImage(file = 'nine.gif')

button_1 = Button(window, image = image_1, value = 1, variable = B1, width = 60, height = 80)
button_2 = Button(window, image = image_2, value = 2, variable = B2, width = 60, height = 80)
button_3 = Button(window, image = image_3, value = 3, variable = B3, width = 60, height = 80)
button_4 = Button(window, image = image_4, value = 4, variable = B4, width = 60, height = 80)
button_5 = Button(window, image = image_5, value = 5, variable = B5, width = 60, height = 80)
button_6 = Button(window, image = image_6, value = 6, variable = B6, width = 60, height = 80)
button_7 = Button(window, image = image_7, value = 7, variable = B7, width = 60, height = 80)
button_8 = Button(window, image = image_8, value = 8, variable = B8, width = 60, height = 80)
button_9 = Button(window, image = image_9, value = 9, variable = B9, width = 60, height = 80)

button_1.place(x = 410, y = 150)
button_2.place(x = 490, y = 150)
button_3.place(x = 570, y = 150)
button_4.place(x = 410, y = 255)
button_5.place(x = 490, y = 255)
button_6.place(x = 570, y = 255)
button_7.place(x = 410, y = 360)
button_8.place(x = 490, y = 360)
button_9.place(x = 570, y = 360)

window.mainloop()

##########     NUMBER BASEBALL 
round = 0

answer_list = []
answer_list.append(random.sample(range(1,10),3))        
answer = answer_list[0]

#print(answer)

while True :
    round += 1    
    print("{}번째 시도".format(round))
#####답 입력

    number_0 = int(input("첫번째 숫자 > "))         
    number_1 = int(input("두번째 숫자 > "))
    number_2 = int(input("세번째 숫자 > "))
    print()

    number= []
    number.append(number_0)
    number.append(number_1)
    number.append(number_2)

    #print(number)

#####judge(strike, ball) 

    judge = []

    for i in range(0, 3) :
        for j in range(0, 3) :
            if answer[i] == number[j] :
                if i == j :
                    judge.append("strike")
                else :
                    judge.append("ball")
        
    #print(judge)

#####strike 출력

    if judge.count('strike') == 3 :
        print(" 3 strikes !!!")
        print("WIN!!!")
        break
    elif judge.count('strike') == 2 :
        print(" 2 strikes !!")
    elif judge.count('strike') == 1 :
        print(" 1 strike !")

#####ball 출력
    if judge.count('ball') == 3 :
        print(" 3 balls ~~~")
    elif judge.count('ball') == 2 :
        print(" 2 balls ~~")
    elif judge.count('ball') == 1 :
        print(" 1 ball ~")
    print()
print()