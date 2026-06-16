class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        s=set()
        for cur in nums:
            if cur in s:
                return True
            else:
                s.add(cur)
        return False

