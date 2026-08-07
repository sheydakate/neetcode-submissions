class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = [] 
        nums.sort() #built in function to sort the array

        for i, a in enumerate(nums): # i is index and a is value
            if i > 0 and a == nums[i-1]: #if we are passed 1st index and see duplicate , skip it
                continue

            l, r = i+1, len(nums)-1 # 2 pointers, one after a and one at the end
            
            while l<r: # while pointers have not crossed
                threeSum = a + nums[l] + nums[r] # add 1st digit with its next and the last

                if threeSum > 0: #if sum is > 0 , reduce by lowering end pointer (since its sorted from low to high)
                    r -= 1
                elif threeSum < 0: #if sum is < 0 , increase by highering l pointer
                    l += 1
                else: # if = 0
                    res.append([a, nums[l], nums[r]]) # add to result
                    l+=1

                    while nums[l] == nums[l-1] and l<r:
                        l += 1
        return res