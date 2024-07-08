class Solution:
    def interpret(self, command: str) -> str:
        rpl = {
            '()': 'o',
            '(al)': 'al'
        }
        for i , j in rpl.items() :
            command=command.replace(i,j)
        return command
