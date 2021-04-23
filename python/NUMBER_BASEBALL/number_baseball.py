import random

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