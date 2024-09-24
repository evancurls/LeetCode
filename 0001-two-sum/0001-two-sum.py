class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        ans = 0
        hash = {}
        for i,num in enumerate(nums):
            ans = target - num
            if ans in hash:
                return [hash[ans],i]
            hash[num] = i

        return None
                
        