list_a = [1, 2, 3]

print("# 리스트 뒤에 요소 추가하기")
list_a.append(4)
list_a.append(5)
print(list_a)
print()

print("# 리스트 중간에 요소 추가하기")
list_a.insert(0, 10)
print(list_a)

print("# 리스트에 한번에 여러개의 요소 추가하기")
list_a.extend([7, 8, 9])
print(list_a)