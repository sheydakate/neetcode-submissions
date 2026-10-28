class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)
        
        for s in strs:
            #will use tuple for key, stores appearance of each letter in each word
            count = [0] * 26 

            for c in s:
                #find each index
                count[ord(c)-ord('a')] += 1
            
            #turn count to tuple, use as key
            result[tuple(count)].append(s)
        
        #must return a list[list[]]
        return list(result.values())



#class Solution:
#    def groupAnagrams(self, strs: List[str]) -> List[List[str]]: 
#        #default dict auto creates a key if != exist
#        res = defaultdict(list)

#       for s in strs:
#            #create a key byt sorting the letters of words
#            myKey = ''.join(sorted(s))

#            #sorted word is key to anagrams in the dictionary
#            res[myKey].append(s)
#        
#        return list(res.values())