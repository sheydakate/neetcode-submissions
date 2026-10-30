class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(i, temp, total):
            #base case 1
            if total == target:
                res.append(temp.copy())
                return
            #base case 2
            if i >= len(nums) or total > target:
                return

            #dfs call to add same digit
            temp.append(nums[i])
            dfs(i, temp, total + nums[i])

            #dfs call to move to next digit
            temp.pop()
            dfs(i+1, temp, total)


        #dfs call to explore nums
        dfs(0, [], 0)
        return res