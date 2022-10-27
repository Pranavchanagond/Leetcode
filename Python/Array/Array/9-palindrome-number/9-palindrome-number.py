class Solution:
    def isPalindrome(self, x: int) -> bool:
        c=str(x)
        a=c[::-1]
        
        if(c==a):
            return True