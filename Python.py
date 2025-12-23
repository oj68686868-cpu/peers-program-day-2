# Check if Array Is Sorted
def isSorted(nums):
    for i in range(len(nums) - 2):
        if nums[i] > nums[i + 1]:
            return False
    return True
nums = list(map(int, input().split()))
print(isSorted(nums))