#변수를 선언합니다.
numbers = [1,2,3,10,20,30]

#반복을 돌립니다.
for number in numbers:
    # number가 10보다 작으면 다음 반복으로 넘어갑니다.
    if number < 10:
        continue
    print(number)