def binarySearch(array, target, low, high):
    mid = (low + high) // 2
    if array[mid] == target:
        return True
    elif low == high or target < array[0] or target > array[len(array) - 1]:
        return False
    elif target < array[mid]:
        return binarySearch(array, target, low, mid - 1)
    return binarySearch(array, target, mid + 1, high)

array = [1, 2, 3, 4, 5, 6, 7]
target = 7

result = binarySearch(array, target, 0, len(array) - 1)
if result:
    print(f'O numero {target} foi encontrado no array.')
else:
    print(f'O numero {target} não foi encontrado no array.')