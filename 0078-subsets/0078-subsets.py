class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        r=[]
        def bt(index,path):
            r.append(path[:]) 
            for i in range(index,len(nums)):
                path.append(nums[i])
                bt(i+1,path)
                path.pop()
        bt(0,[])
        return r

        