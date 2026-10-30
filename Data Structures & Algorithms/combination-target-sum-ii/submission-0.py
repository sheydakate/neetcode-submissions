class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        res = []
        candidates.sort()

        #dfs call
        def dfs (i, temp, sum):
            #base case 1
            if sum == target:
                res.append(temp.copy())
                return

            #base case 2
            if i == len(candidates) or sum > target: 
                return

            #include number, move nextm update total
            temp.append(candidates[i])
            dfs(i+1, temp, sum + candidates[i])

            #exlude last digit to explore diff combos
            temp.pop()

            #exclude number, skip duplicate
            while i+1 < len(candidates) and candidates[i] == candidates[i+1]:
                #move to suplicate
                i += 1
            
            #skip duplicate
            dfs (i+1 , temp, sum)


        #dfs call
        dfs(0, [], 0)
        return res