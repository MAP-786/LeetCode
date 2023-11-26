#238. Product of Array Except Self
class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        solution = []
        solution.append(1)
        for i in range (0, len(nums)-1):
            solution.append(nums[i]*solution[i])
        rightvalue = nums[-1]
        for i in range (len(nums)-2, -1, -1):
            solution[i] = rightvalue * solution[i]
            rightvalue *= nums[i]
        return solution



        
S = Solution()
print(S.productExceptSelf([2,3,4,5]))