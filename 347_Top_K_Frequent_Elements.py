#347. Top K Frequent Elements
#We are given an array of values, that may be unsorted. 
#We are also given a k value/threshold value. 
#We need to figure out which values in the original array are equal to or more frequent than the k value. 
#Count the frequency of different numbers in array, take into account repeated values, and record results into a dictionary. 
#Add those values(once) whose frequency is equal/greater than k into second array. 

class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        nums2 = []
        dictionarynums = {}
        for i in range(0, len(nums)):
            dictionarynums[nums[i]] = 1 + dictionarynums.get(nums[i], 0)
            print(dictionarynums)
        for key, val in dictionarynums.items():
            if val >= k:
                if val not in nums2:
                    nums2.append(key)
        return nums2
         



S= Solution()
print(S.topKFrequent([1,1,1,2,2,3,5,5,7,8,8,8,9], k = 2))
