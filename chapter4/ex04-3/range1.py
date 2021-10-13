a = range(5)
print(a)

b = list(range(10))
print(b)

c = list(range(0, 5)) # -> 0부터 (5-1) 까지의 정수로 범위를 만듭니다.
print(c)

d = list(range(5, 10)) # -> 5부터 (10-1) 까지의 정수로 범위를 만듭니다.
print(d)

e = list(range(0, 10, 2)) # -> 0부터 2씩 증가하면서 (10 - 1)까지의 정수로 범위를 만듭니다.
print(e)

f = list(range(0, 10, 3)) # -> 0부터 3씩 증가하면서 ( 10- 1)까지의 정수로 범위를 만듭니다.
print(f)

g = range(0, 10 + 1)
print(list(g))

# h = 10
# i = range(0, h / 2) # 매개변수로 나눗셈을 사용한 경우 오류가 발생합니다.

h = 10
i = range(0, int(h / 2)) # 실수를 정수로 바꾸는 방법보다
print(list(i))

j = 10
k = range(0, h // 2) # 정수 나누기 연산자를 많이 사용합니다.
print(list(k))

