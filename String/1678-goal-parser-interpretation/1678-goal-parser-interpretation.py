class Solution:
    def interpret(self, command: str) -> str:
        res=""
        for i in range(len(command)):
            if(command[i]=="G"):
                res+="G"
            elif (command[i]=="(" and command[i+1]==")"):
                res+="o"
            elif (command[i]=="(" and command[i+1]=="a" and command[i+2]=="l" and command[i+3]==")"):
                res+="al"
        return res