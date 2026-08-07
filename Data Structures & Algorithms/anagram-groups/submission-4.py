class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        res = defaultdict(list) #mapping count fo each string to list of anagrams - default value of dictionary is list here
        
        for s in strs: #must go through every string in input
            count = [0]*26 #we have to count how many of each letter from a-z so we have 26 indexes intitalized to 0
            for c in s: #we have to go through every character in each string
                count[ord(c)-ord("a")]+=1 #using ascii to map letters to indeces
            res[tuple(count)].append(s)
        return list(res.values())