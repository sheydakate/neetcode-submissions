class Solution:

    def encode (self, strs: List[str])-> str:
        res =[]

        for s in strs:
            res.append(str(len(s))+"#"+s)
        
        return "".join(res)

    # Time complexity O(n)
    # Space complexity O(n)

    
    def decode (self, s: str) -> List[str]:
        l, r = 0,0
        res = []

        while r < len(s):

            while s[r] != "#":
                r += 1
            
            length = int(s[l:r])
            res.append(s[r+1:r+1+length])
            r, l = r+1+length, r+1+length
        return res

    # Time complexity O(n)
    # Space complexity O(n)
            