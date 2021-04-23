number = input("정수 입력 > ")
last_character = number[-1]

#짝수 확인
if last_character in "02468" :
    print("짝수입니다.")

#홀수 확인
if last_character in "13579" :
    print("홀수입니다.")