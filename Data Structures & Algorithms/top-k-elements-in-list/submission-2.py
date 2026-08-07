class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        count = {} #hashmap to count occurences of each value
        freq = [[] for i in range(len(nums)+1)]   #special array, index = frequence of element

        for n in nums: #how we'll count number of times each value in nums occurs
            count[n]=1+count.get(n, 0)

        for n, c in count.items(): #will return key value pair
            freq[c].append(n) #value n occurs c number of times

        res = []
        for i in range(len(freq)-1, 0, -1): #descending: -1 order range length of frequency -1->last index, until index 0
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res

"""
nums [1,1,12,2,3]   k = 2
1->3        already in ascendind order
2->2        But regardless we dont neede to sort everything
3->1        just need the k most frequent so use max heap

key of max heap: umber of occurences, we'll pop eactly k times
Will add everything 1st, then run heapif, then pop k times

heapify O(n) , each pop O(logn)* k times

EFFICIENT WAY USING BUCKET SORT
O(n) space and memory

use a count array; numes : [1,1,1,2,2,100]
                   i     : [0 , 1 , 2 , ..., 100]
                   count : [  , 3 ,  2,    ,    ]

i is index, make an array, go thru nums, if first digit in nums is 5, 
go to index 5 of new array and put 1 as its value, if the second value 
is also 5, go to index 5 and increment the value by 1

** would be linear if we nums was bounded, knew from what # to what #

INSSTEAD WILL USE INDECES i AS TOTAL NUMBER OF ORRUREMCES OF DIGITS
                   numes : [1, 1, 1, 2, 2,5,5 100]

                   i     : [0|   1   |   2   |  3  | 4| 5| 6]     0-size of nums
                   count : [ | [100] | [2,5] | [1] |  |  |  ]

start at the end of last index (6 here is most frequent)
go from R to L until see val, here index 3 -> 1 add 1 to result and so on
return array
max size of count array for count, LINEAR
Space O(n)+O(n)
memory O(n)
"""
