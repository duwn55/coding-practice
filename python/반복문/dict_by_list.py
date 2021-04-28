# 각 리스트를 조합하여 하나의 딕셔너리 만들기
key_list = ["name", "hp", "mp", "level"]
value_list = ["기사", 300, 40, 9]
character = {}
for i in range(0, 4) :
    character[key_list[i]] = value_list[i]

# 출력
print(character)
