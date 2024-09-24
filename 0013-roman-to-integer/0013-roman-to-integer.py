class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """

        sum = 0
        table = {
            'M':1000,'D':500,'C':100,'L':50,'X':10,'V':5,'I':1
        }
        s = s.replace('IV','IIII').replace('IX','VIIII').replace('XL','XXXX').replace('XC','LXXXX').replace('CD','CCCC').replace('CM','DCCCC')
        for str in s:
            sum = sum + table[str] 
        return sum

        