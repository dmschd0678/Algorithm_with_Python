def binary(array, elem, first, last):

    if first > last:
        return 0

    mid = (first + last) // 2

    if array[mid] == elem:
        return 1

    elif array[mid] > elem:
        return binary(array, elem, first, mid - 1)

    else:
        return binary(array,elem,mid + 1,last)

input()
list1 = list(map(int,input().split()))
list1.sort()
input()
list2 = list(map(int,(input().split())))

for i in list2:
    print(binary(list1, i, 0, (len(list1) - 1)))