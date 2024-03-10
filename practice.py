def findDuplicate(self, nums: List[int]) -> int:
    slow = 0
    fast = 1
    length = len(nums) - 1
    while nums[fast] != nums[slow]:
        if slow + 1 > length:
            slow = 0
        else:
            slow = slow + 1
        if fast + 2 > length:
            fast = 0
        else:
            fast = fast + 2
    return nums[fast]