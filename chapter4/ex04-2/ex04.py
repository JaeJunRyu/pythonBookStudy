#딕셔너리를 선언합니다.
character = {
    "name": "기사",
    "level": 12,
    "items": {
      "sword": "불꽃의 검",
      "armor": "풀플레이트"
    },
    "skill": ["베기", "세게 배기", "아주 세게 배기"]
}

for key in character:
    if type(character[key]) is list:
        for key_in in character[key]:
            print("{} : {}".format(key, key_in))
    elif type(character[key]) is dict:
        for key_in in character[key]:
            print("{} : {}".format(key_in, character[key][key_in]))
    else:
        print("{} : {}".format(key, character[key]))