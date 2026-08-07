class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        myMap = defaultdict(list)

        for s in strs:
            key = [0]*26
            for c in s:
                index = ord(c)-ord('a')
                key[index]+=1
            myMap[tuple(key)].append(s)
        return list(myMap.values())