def sort_array_by_parity(nums):
  
    return [x for x in nums if x % 2 == 0] + [x for x in nums if x % 2 != 0]

# Приклади використання
nums = [3, 1, 2, 4]
print(sort_array_by_parity(nums))  # [2, 4, 3, 1] 

nums = [0]
print(sort_array_by_parity(nums))  # [0]
