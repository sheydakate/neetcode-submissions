class Solution: 
    def longestConsecutive(self, nums: list[int]) -> int: 
    #make a set with values of nums 
        numSet = set(nums) 
        longest = 0 #will store the longest length 
        
        for n in nums: 
            #is it a first digit? 
            if (n-1) not in numSet: 
                length = 0 #will store current sequence's length 
                
                #as long as next digit exists 
                while (n+length) in numSet: 
                    length += 1 
                
                longest = max(longest, length) #if new sequence is longer, update longest 
        
        return longest 
    
    
#memory complexity O(n)
#space complexity O(N)
    

sol = Solution () 
numbers = [1,7,2,6,19,5,10,8] 
longestConsecuive = sol.longestConsecutive(numbers) 

print("longest consecutive is: ", longestConsecuive)