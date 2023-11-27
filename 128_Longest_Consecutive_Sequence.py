#First we need to sort the array 
#Then we need to keep another array which keeps track of numbers in order.
#We have a variable called longest which calculates the length of the tracking array and updates at each iteration. 
#We add the first value of sorted array into tracking array. 
#We compute the next value ourselves and compare it with the value in the sorted array. 
#If its the same we add it to the tracking array 
#Oherwise we make the tracking array blank and add the value from the sorted array. 
#However, this will give us a time complexity of O(nlogn)

#The other apporach is to have to create a hashset which enables us to search in O(1) time. 
#We then take each value from the array and see if a smalller value then it exists. 
#If a smaller value exists then it means it is not the start of a sequence and we move on to the next value. 
#However, if it has no smaller values then we that means this could potenitally be the largest sequence.
#We then add 1 to this value and see if it exists in the hashset. We keep adding 1 until we the next value does not exists. 
#We keep track of the maximum numbers of 1s added for each sequence until the end of the array. 
#We retunr the maximum number of 1s added (or the longest sequence)


class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        nums = set(nums)
        best = 0 
        for x in nums: 
            if x - 1 not in nums: 
                y = x + 1 
                while y in nums: 
                    y += 1
                best = max(best, y-x)
        return best

S = Solution()
print(S.longestConsecutive([100,4,200,1,3,2]))