#딕셔너리를 선언합니다.
dictionary = {
    "name": "제목",
    "type": "type"
}

#요소 제거 전에 내용을 출력해 봅니다.
print(dictionary)

del dictionary["name"]
del dictionary["type"]

#요소 제거 후에 내용을 출력해 봅니다.
print(dictionary)