class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        sum=0
        for i in range(0,len(mat)):
            for j in range(0,len(mat[i])):
                if i==j:
                    sum+=mat[i][j]
                elif (i+j==(len(mat)-1)):
                    sum+=mat[i][j]
        return sum