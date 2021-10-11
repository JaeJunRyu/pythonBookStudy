import itertools

numbers = [1,2,3,4,5,6,7,8,9]
output = [[], [], []]

print((1+2) % 3)
print((2+2) % 3)
print((3+2) % 3)
print()
print((4+2) % 3)
print((5+2) % 3)
print((6+2) % 3)
print()
print((7+2) % 3)
print((8+2) % 3)
print((9+2) % 3)
print()
print((10+2) % 3)
print((11+2) % 3)
print((12+2) % 3)

print()
for number in numbers:
    output[(number + 2) % 3].append(number)

print("output : ", output)

print("*output : ", *output)
sortlist = sorted(itertools.chain(*output))
print("sortlist : ", sortlist)

_iter = iter(sortlist)
dlist = list(iter(lambda: list(itertools.islice(_iter, 3)), []))
print("dlist : ", dlist)

myList = [[1,2,3],[4,5,6],[7,8,9]]
newMyList = list(map(list, zip(*myList)))
print("newMyList: ",newMyList)