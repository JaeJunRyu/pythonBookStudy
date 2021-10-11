list_a = [0, 1, 2, 3, 4, 5, 6, 7]
list_a.extend(list_a)
print(list_a)
#[0, 1, 2, 3, 4, 5, 6, 7, 0, 1, 2, 3, 4, 5, 6, 7]

list_a1 = [0, 1, 2, 3, 4, 5, 6, 7]
list_a1.append(10)
print(list_a1)
#[0, 1, 2, 3, 4, 5, 6, 7, 10]

list_a2 = [0, 1, 2, 3, 4, 5, 6, 7]
list_a2.insert(3, 0)
print(list_a2)
#[0, 1, 2, 0, 3, 4, 5, 6, 7]

list_a3 = [0, 1, 2, 3, 4, 5, 6, 7]
list_a3.remove(3)
print(list_a3)
#[0, 1, 2, 4, 5, 6, 7]

list_a4 = [0, 1, 2, 3, 4, 5, 6, 7]
# list_a4.pop() #제일 마지막 배열 삭제
list_a4.pop(-1) #제일 마지막 배열 삭제
list_a4.pop(3) #앞에서 3번째 0, 1, 2, 3

print("list_a4: ", list_a4)
#list_a4:  [0, 1, 2, 3, 4, 5, 6]

list_a5 = [0, 1, 2, 3, 4, 5, 6, 7]
list_a5.clear()
print(list_a5)
[]