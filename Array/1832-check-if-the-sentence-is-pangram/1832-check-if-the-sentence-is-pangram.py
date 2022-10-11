class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        count=0
        for i in range(97,123):
            for j in range(0,len(sentence)):
                if chr(i)==sentence[j]:
                    count+=1
                    break
        if(count==26):
            return True
        else:
            return False