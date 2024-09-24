class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        x = 0
        for i in range(0,len(nums)):
            if nums[i] != val:
                nums[x] = nums[i]
                print nums[x]
                x +=1
        return x

        