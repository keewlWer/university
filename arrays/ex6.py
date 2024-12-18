def remove_duplicates(nums):
    if not nums:
        return 0

    unique_index = 0

    for i in range(1, len(nums)):
        if nums[i] != nums[unique_index]:
            unique_index += 1
            nums[unique_index] = nums[i]

    return unique_index + 1

# Приклади використання
nums = [1, 1, 2]
k = remove_duplicates(nums)
print(k, nums[:k])  # 2, [1, 2]

nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
k = remove_duplicates(nums)
print(k, nums[:k])  # 5, [0, 1, 2, 3, 4]
