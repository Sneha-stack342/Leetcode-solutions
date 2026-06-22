class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        c=0
        sum=0
        for i in range(len(costs)):
            if sum+costs[i]<=coins:
                sum+=costs[i]
                c+=1
        return c

            



            


        