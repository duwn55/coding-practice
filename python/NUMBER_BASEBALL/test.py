import random

answer_list = []
answer_list.append(random.sample(range(1,10),3))        #정답 random하게 추출
answer = answer_list[0]

print(answer)

#####답 입력

number_0 = int(input("첫번째 숫자 > "))         
number_1 = int(input("두번째 숫자 > "))
number_2 = int(input("세번째 숫자 > "))

number= []
number.append(number_0)
number.append(number_1)
number.append(number_2)

print(number)

ball = []
judge = []

for i in range(0, 3) :
    for j in range(0, 3) :
        if answer[i] == number[j] :
            if i == j :
                judge.append("strike")
            else :
                judge.append("ball")
print(judge)