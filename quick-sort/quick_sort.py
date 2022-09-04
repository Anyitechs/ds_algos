# QuickSort implementation in Python
# QuickSort uses the D&C algorithm
def quickSort(arr):
    if len(arr) < 2:
        return arr
    else:
        pivot = arr[0]
        less = [i for i in arr[1:] if i <= pivot]
        high = [i for i in arr[1:] if i > pivot]
        
        return quickSort(less) + [pivot] + quickSort(high)

arr_item = [5, 2, 6, 0, 11, 1, 20, 3, 50, 66, 2, 7]
print(quickSort(arr_item))
