#리스트를 선언합니다.
array = [1,2,3,4,5]

print(len(array))
#리스트에 반복문을 적용합니다.
for element in range(len(array)):
    print("{}번째 반복: {}".format(element, array[element]))