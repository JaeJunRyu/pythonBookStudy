#딕셔너리를 선언합니다.
dictionary = {
    "name":"7D 건조 망고",
    "type":"당절임",
    "ingredient": ["망고", "설탕", "나트륨", "색소"],
    "origin": "필리핀"
}

#존재하지 않는 키에 접근해 봅시다.
value = dictionary.get("존재하지 않은 키")
print("값 : ", value)

#None 확인 방법
if value == None: #-> None과 같은지 확인만 하면 됩니다.
    print("존재하지 않은 키에 접근했습니다.")