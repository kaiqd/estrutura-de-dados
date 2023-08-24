def has_pair_with_sum(array, target, left=0, right=None):
    if right is None:
        right = len(array) - 1
    
    if left >= right:
        return False

    current_sum = array[left] + array[right]
    
    if current_sum == target:
        return True
    elif current_sum < target:
        return has_pair_with_sum(array, target, left + 1, right)
    else:
        return has_pair_with_sum(array, target, left, right - 1)


sorted_array = [2, 4, 6, 8, 10, 12]
target_sum = 14

result = has_pair_with_sum(sorted_array, target_sum)

if result:
    print(f"Existe um par no array que soma {target_sum}.")
else:
    print(f"Nao existe um par no array que soma {target_sum}.")