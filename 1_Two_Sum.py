#1 Two Sum
#Add first value to remaining values in original array until their sum reaches matches target. 
#Then do this with the second value and so on 
#Hence, two for loops. 
#Add the two values whos sum matches target to second array and return it. 

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        nums2 = []
        for i in range(0, len(nums)):
            for j in range(1, len(nums)):
                if ((nums[i] + nums[j]) == target):
                    nums2.append(i)
                    nums2.append(j)
                    return nums2

S = Solution()
print(S.twoSum([2,7,11,15],17))