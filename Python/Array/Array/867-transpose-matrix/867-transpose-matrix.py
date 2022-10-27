class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        ans=[]
        m=len(matrix)
        n=len(matrix[0])
        ans=[[0 for i in range(m)]for j in range(n)]
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                ans[c][r]=matrix[r][c]
        return ans