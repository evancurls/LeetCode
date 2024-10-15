class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        setNums = set(nums)
        seq = 0

        for i in setNums:
            if (i - 1) not in setNums:
                newSeq = 1 
                while (i + newSeq) in setNums:
                    newSeq += 1
                seq = max(seq,newSeq)
        
        return seq