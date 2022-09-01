# Binary search implementation
# Binary search requires that the items are sorted orderly
def binary_search(list, item):
    low = 0
    high = len(list) - 1
    mid = 0
    while low <= high:
        mid = (low + high) // 2
        guess = list[mid]
        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None

search_list = [2, 3, 4, 5, 6, 7]
print(binary_search(search_list, 4))