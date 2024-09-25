class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict = {} # dictionary for numbers and their respective counts
        freq = [[] for i in range(len(nums) + 1)] #length of integers in nums
        for j in nums:
            dict[j] = 1 + dict.get(j,0) #gets the total repeated. CANNOT DO += 1

        #for each element in the dictionary, numbers = respective number; counts = respective repetitions
        for numbers,counts in dict.items():
            freq[counts].append(numbers)
        
        newlist = []
        for i in range(len(freq) - 1,0,-1): #counts down from the length
            for n in freq[i]:
                newlist.append(n)
            if(len(newlist) == k):
                return newlist

        #count down from k, once k gets 0 return resulting list

        #return knums
        return sorted(newdict, reverse=True)[:k]
        #unfortunately sorts the numbers not their occurrences
