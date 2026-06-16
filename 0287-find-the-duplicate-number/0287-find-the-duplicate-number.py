class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        a=set()
        for i in range(len(nums)):
            if nums[i] not in a:
                a.add(nums[i])
            else:
                return nums[i]