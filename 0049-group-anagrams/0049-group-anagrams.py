class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #for i in strs:
        #    print(i)

        #go through list of words, check if word is in an anagram list
        #if not, create a new anagram list
        #anagram list should be recursive
        anagrams = defaultdict(list)

        for word in strs:
            abc = [0] * 26 #alphabet array
            for character in word:
                abc[ord(character) - ord("a")] += 1 #adds 1 to respective letter count
            anagrams[tuple(abc)].append(word)
        return anagrams.values()


        #anagrams.append(newAnagram())
        #def checkAnagram(anagrams: List[str], string):
        #    for word[0] for word in anagrams:
        #        if string.sorted() == word.sorted():

        #def newAnagram(list: List[str], gram: str,count: int):