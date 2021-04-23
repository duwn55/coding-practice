number = input("정수 입력 > ")
last_character = number[-1]

#숫자로 변환
last_character = int(last_character)

#짝수 확인
if last_character == 0 or last_character == 2 \
    or last_character == 4 or last_character == 6 \
    or last_character == 8 :
    print("짝수입니다.")

#홀수 확인
if last_character == 1 or last_character == 2 \
    or last_character == 5 or last_character == 7 \
    or last_character == 9 :
    print("홀수입니다.")