class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        strx = str(x)
        newx = ''
        i = len(strx) - 1
        j = 0
        while i >= j:
            if strx[j] != strx[i]:
                return False
            i = i - 1
            j = j + 1
        return True
