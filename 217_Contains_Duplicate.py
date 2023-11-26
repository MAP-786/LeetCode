#217. Contains Duplicate

class Solution:
    def containsDuplicate(self, nums: list[int])->bool:
        nums2 : list[int] 
        for x in range(0, len(nums)):
#            print("x: ", x)
            for y in range((x+1), len(nums)): 
#                print("y: ", y)
#                print("nums[x]", nums[x])
#                print("nums[y]", nums[y])
                if nums[x] == nums[y]:
                    return True 
        return False  
S = Solution()
print(S.containsDuplicate([1,2,3,3]))

