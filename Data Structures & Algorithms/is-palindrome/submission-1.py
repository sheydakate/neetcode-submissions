class Solution:
    def isPalindrome(self, s: str) -> bool:
        #left and right pointers
        l, r = 0, len(s)-1
        
        #as long as pinters haven't crossed
        while(l<r):
            
            #skip any non-alphanumeric char from left, stay in bound
            while l<r and not self.alphaNumeric(s[l]):
                l+=1
            
            #skip any non-alphanumeric char from right, stay in bound
            while r>l and not self.alphaNumeric(s[r]):
                r-=1
                
            #check if not palindrome return false
            if s[l].lower() != s[r].lower():
                return False
                
            #if palindrome, move both pointers, lowe case
            l, r = l+1, r-1
        
        #if reached end, return true
        return True
        
        
    
    #check if alpha numeric character
    def alphaNumeric(self, c):
        
        return (ord('A') <= ord(c) <= ord('Z') or
                ord('a') <= ord(c) <= ord('z') or
                ord('0') <= ord(c) <= ord('9')) 


#memory complexity O(n)
#space complexity O(1)

sol = Solution()
testString = "was it A car; or a: CaT i Saw?"

ans = sol.isPalindrome(testString)
print(ans)
