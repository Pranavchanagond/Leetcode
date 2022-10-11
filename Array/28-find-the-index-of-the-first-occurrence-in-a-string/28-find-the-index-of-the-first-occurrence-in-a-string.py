class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        i=0
        n=len(needle)
        if(haystack==needle):
            return 0
        while i+n <= len(haystack):
            if(haystack[i:i+n]==needle):
                return i
            else:
                i+=1
        
        return -1