class Solution(object):
    def interpret(self, parser):
    
        parser = parser.replace("()", "o").replace("(al)", "al")
        return parser