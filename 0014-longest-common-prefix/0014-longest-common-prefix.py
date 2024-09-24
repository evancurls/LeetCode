class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """

        prefix = ''
        i = 0
        word1 = strs[0]
        #print "Word 1: ", word1
        #print "Letter 1:", word1[0]
        length = len(min(strs,key=len))
        if length == 0:
            return prefix
        while i < length:
            ch = word1[i]
            # "Letter", i, ": ", word1[i]
            for word in strs:
                if word[i] != ch:
                    return prefix
            prefix = prefix + ch
            i = i + 1
        return prefix
