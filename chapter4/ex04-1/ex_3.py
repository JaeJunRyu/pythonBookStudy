import sys
numbers = [1,2,3,4,5,6,7,8,9,10,100, 1000]

for number in numbers:
    if number % 2 == 0:
        print(number, "는 짝수 입니다.")
    else:
        print(number, "는 홀수 입니다.")

print()
for number in numbers:
    print(number, "는", len(str(number)), "는 자릿수 입니다.")

