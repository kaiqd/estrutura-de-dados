def reorganize_array(arr, k, start=0):
    if start == len(arr):
        return

    if arr[start] <= k:
        arr.insert(0, arr.pop(start))
        reorganize_array(arr, k, start + 1)
    else:
        reorganize_array(arr, k, start + 1)


unsorted_array = [10, 5, 8, 3, 12, 7, 15]
k = 8

print("Array antes da reorganizacao:", unsorted_array)
reorganize_array(unsorted_array, k)
print("Array apos a reorganizacao:", unsorted_array)