def twoSum(nums, target):
    num_to_index = {}
    for index, num in enumerate(nums):
        difference = target - num
        if difference in num_to_index:
            return [num_to_index[difference], index]
        num_to_index[num] = index

# 예시 사용:
nums = [2, 7, 11, 15]
target = 9
print(twoSum(nums, target))  # 출력: [0, 1] (nums[0] + nums[1] = 2 + 7 = 9)
