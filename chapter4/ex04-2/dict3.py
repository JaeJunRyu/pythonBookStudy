dictionary = {
    "name":"7D 건조 망고",
    "type":"당절임",
    "ingredient": ["망고", "설탕", "나트륨", "색소"],
    "origin": "필리핀"
}

dictionary["price"] = 5000
print(dictionary)

dictionary["name"] = "새로운 제목"
print(dictionary)

del dictionary["type"]
print(dictionary)