class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        ans1=""
        ans2=""
        for i in range(0,len(word1)):
            ans1+=word1[i]
        for i in range(0,len(word2)):
            ans2+=word2[i]

        if ans1==ans2:
            return True
        else:
            return False