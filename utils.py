def find_max():
    list = []
    numbers = int (input ())
    for x in range (0 ,numbers):
        elements=int (input())
        list.append(elements)
    max = list [0]
    for i in list:
        if max < i :
            max=i
    print(max)
find_max()