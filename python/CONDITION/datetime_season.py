#날짜/시간 관련 기능 가져오기
import datetime

#현재 날짜/시간 구하기
now = datetime.datetime.now()

#봄
if 3 <= now.month <= 5 :
    print("이번 달은 {}월로 봄입니다.".format(now.month))

#여름
if 6 <= now.month <= 8 :
    print("이번 달은 {}월로 여름입니다.".format(now.month))

#가을
if 9 <= now.month <= 11 :
    print("이번 달은 {}월로 가을입니다.".format(now.month))

#겨울
if now.month == 12 or now.month <= 2 :
    print("이번 달은 {}월로 겨울입니다.".format(now.month))