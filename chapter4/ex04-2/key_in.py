#딕셔너리를 선언합니다.
dictionary = {
    "name": "name",
    "type": "type",
    "ingredient" : [1,2,3,4,55],
    "origin": "aa"
}

#사용자로부터 입력을 받습니다.
key = input("> 접근하고자 하는 키: ")
#출력 합니다.
if key in dictionary:
    print(dictionary[key])
else:
    print("존재 하지 않아!")