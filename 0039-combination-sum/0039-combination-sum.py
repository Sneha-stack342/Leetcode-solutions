class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        r=[]
        def backtrack(index,path,sum):
            if target==sum:
                r.append(path[:])
                return 
            if sum>target or index==len(candidates):
                return 
            for i in range(index,len(candidates)):
                path.append(candidates[i])
                backtrack(i,path,sum+candidates[i])
                path.pop()
        backtrack(0,[],0)
        return r
      
        