# Selection Sort implemetation in Python
def findSmallestValue(arr):
    smallest_value = arr[0]
    smallest_index = 0
    for i in range(1, len(arr) - 1):
        if arr[i] < smallest_value:
            smallest_value = arr[i]
            smallest_index = i
    return smallest_index

def selectionSort(arr):
    newArr = []
    for i in range(len(arr) - 1):
        smallest = findSmallestValue(arr)
        newArr.append(arr.pop(smallest))
    return newArr

arr_list = [50, 3, 18, 1, 0, -2, 49]
print(selectionSort(arr_list))