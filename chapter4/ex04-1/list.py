array = [1,2,3,4] #숫자만으로 구성된 리스트
print(array)
print(array[5])
str_array = ["안","녕","하","세","요"]  #문자열만으로 구성된 리스트
print(str_array)
object_array = [273,32,103,"문자열", True, False]
print(object_array)

print()
list_a = [273,32,103,"문자열", True, False]
print(list_a[0])
print(list_a[1])
print(list_a[2])
print(list_a[1:3])

print()
list_b = [273,32,103,"문자열", True, False]
list_b[0] = "변경"
print(list_b)

print()
list_c = [273,32,103,"문자열", True, False]
print(list_c[-1])
print(list_c[-2])
print(list_c[-3])

print()
list_d = [273,32,103,"문자열", True, False]
print(list_d[3])
print(list_d[3][0])
print(list_d[3][1])
print(list_d[3][2])

print()
list_e = [[1,2,3],[4,5,6],[7,8,9]]
print(list_e[0])
print(list_e[1][0])
print(list_e[1][1])
print(list_e[1][2])
