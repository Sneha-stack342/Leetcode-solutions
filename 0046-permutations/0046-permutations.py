class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        r=[]
        def bt(path):
            if len(path)==len(nums):
                r.append(path[:])
                return
            for i in nums:
                if i not in path:
                    path.append(i)
                    bt(path)
                    path.pop()
        bt([])
        return r
        