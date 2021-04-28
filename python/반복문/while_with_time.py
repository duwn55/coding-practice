# 시간과 관련된 기능 가져오기.
import time

# 변수 선언
number = 0

# 5초 동안 반복
target_tick = time.time() + 5
while time.time() < target_tick :
    number += 1

# 출력
print("5초 동안 {}번 반복했습니다.".format(number))
