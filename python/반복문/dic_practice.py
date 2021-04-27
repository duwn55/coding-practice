##### 강아지 이름과 나이 출력_딕셔너리 리스트

###딕셔너리 리스트 선언
pets = [
	{"name" : "구름", "age" : 5},
	{"name" : "초코", "age" : 3},
	{"name" : "아지", "age" : 1},
	{"name" : "호랑이", "age" : 1}
	]

###이름과 나이만 출력
print("# 우리 동네 강아지들")
for index in pets :
    print(index["name"], str(index["age"])+"살")
print()


#####숫자 빈도 확인
numbers = [1, 2 ,6 ,8, 4, 3, 2, 1, 9, 5, 4, 9, 7, 2, 1, 3, 5, 4, 8, 9, 7, 2, 3]
counter = {}

for number in numbers :
    counter[number] = numbers.count(number)

print(counter)
print()



#####리스트 중첩
character = {
    "name" : "기사",
    "level" : 12,
    "items" : {
        "sword" : "불꽃의 검",
        "armor" : "풀플레이트"
    },
    "skill" : ["베기", "세게 베기", "아주 세게 베기"]
}

for key in character :
    if type(character[key]) is dict :
        KEY = character[key]
        for key in KEY :
            print(key, ":", KEY[key])
    elif type(character[key]) is list :
        for index in character[key] :
            print(key, ":", index)
    else :
        print(key, ":", character[key])