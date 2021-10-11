list_a = [1, 2, 3]
list_b = [4, 5, 6]
print("list_a + list_b", list_a.extend(list_b)) #실행결과로 아무 것도 출력하지 않습니다.
print("list_a", list_a) # 앞에 입력했던 list_a 자차에 직접적인 변화가 있습니다.(파괴적 처리)
print("list_b", list_b)

