class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        i=j=0
        ans=0
        k=""
        for i in range(0,len(items)):
                k=items[i]
          #  for j in range(0,len(k)):
                if ruleKey=="type":
                    if k[0] == ruleValue:
                        ans+=1
                elif ruleKey=="color":
                    if k[1] == ruleValue:
                        ans+=1
                elif ruleKey=="name":
                    if k[2] == ruleValue:
                        ans+=1        
        return ans