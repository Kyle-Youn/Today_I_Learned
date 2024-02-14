# 'nums'리스트 안의 두 가지 요소를 더해 'target' 숫자로 만들 수 있으면 True, 아니면 False

#투 포인터로 풀이. O(nlogn)
def twoSum(nums, target):
    nums.sort()
    l, r = 0, len(nums)-1
    while l < r:
        if nums[l] + nums[r] > target:
            r -= 1
        elif nums[l] + nums[r] < target:
            l += 1
        elif nums[l] + nums[r] == target:
            return True
    return False

print(twoSum(nums=[4,1,9,7,5,3,16], target=14))