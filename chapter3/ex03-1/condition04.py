a = float(input("> 1번째 숫자 : "))
b = float(input("> 2번째 숫자 : "))
print()

if a > b:
    print("처음 입력했던 {:0.1f}가 {:0.1f}보다 큽니다.".format(a, b))

if b > a:
    print("두번째로 입력했던 {:0.1f}가 {:0.1f}보다 큽니다.".format(b, a))