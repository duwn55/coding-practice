list_a = [0, 1, 2, 3, 4, 5]
print("# 리스트의 요소 제거하기")

# 인덱스 지정 제거 방법[1] - del
del list_a[1]
print("del list_a[1] :", list_a)        #del 키워드를 사용하면 [3:6], [:3], [3:] 과 같이 범위 지정하여 제거 가능
print()

# 인덱스 지정 제거 방법[2] - pop()
list_a.pop(2)
print("pop(2) :", list_a)           # pop() 함수의 매개변수에 아무 것도 입력하지 않으면 자동으로 -1이 들어가는 것으로 취급하여 마지막 요소 제거
print()

# 특정 값 지정 제거 방법
list_c = [1, 2, 1, 2]
list_c.remove(2)
print(list_c)
print()

#모두 제거
list_d = [0, 1, 2, 3, 4, 5, 6]
list_d.clear()
print(list_d)

