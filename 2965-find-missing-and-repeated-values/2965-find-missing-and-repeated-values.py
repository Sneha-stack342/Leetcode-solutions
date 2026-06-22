class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)
        s = n * n
        nums = [num for r in grid for num in r] 

        # Find repeated
        for num in nums:
            if nums.count(num) > 1:
                repeated = num
                break

        # Find missing
        for x in range(1, s + 1):
            if x not in nums:
                missing = x
                break

        return [repeated, missing]
        