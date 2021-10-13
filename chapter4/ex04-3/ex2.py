#숫자는 무작위로 입력해도 상관없습니다.
key_list = ["name", "hp", "mp", "level"]
value_list = ["기사", 200, 30, 5]
character = {}

for idx in range(len(key_list)):
    character[key_list[idx]] = value_list[idx]

print(character)
print()

character1 = {}
for idx, val in enumerate(key_list):
    character1[val] = value_list[idx]

print(character1)
print()
