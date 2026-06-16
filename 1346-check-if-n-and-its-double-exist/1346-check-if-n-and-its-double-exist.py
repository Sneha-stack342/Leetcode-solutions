class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        r=[]
        #t=arr[0]
        for i in range(len(arr)):
            for j in range(0,len(arr)):
                if i!=j and arr[i]==2*arr[j]:
                    return True
        return False
                




        
        