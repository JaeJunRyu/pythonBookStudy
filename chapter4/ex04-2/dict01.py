#딕셔너리를 선언합니다.
dictionary = {
    "name":"7D 건조 망고",
    "type":"당절임",
    "ingredient": ["망고", "설탕", "나트륨", "색소"],
    "origin": "필리핀"
}

#출력합니다.
print("name", dictionary["name"])
print("type", dictionary["type"])
print("ingredient", dictionary["ingredient"])
print("origin", dictionary["origin"])

#값을 변경합니다.
dictionary["name"] = "8D 건조망고"
print(dictionary["name"])


print(dictionary["ingredient"])
print(dictionary["ingredient"][1])
