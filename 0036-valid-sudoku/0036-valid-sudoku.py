class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        r=set()
        c=set()
        b=set()
        for i in range(9):
            for j in range(9):
                x=board[i][j]
                if (i,x) in r:
                    return False
                if (j,x) in c:
                    return False
                if x==".":
                    continue
                ba=(i//3,j//3)
                if (ba,x) in b:
                    return False
                r.add((i,x))
                c.add((j,x))
                b.add((ba,x))
        return True
               
                

       
               
            
        