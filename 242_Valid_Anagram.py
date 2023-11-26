#242. Valid Anagram 



#One Posssible Solution
'''
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if sorted(s) == sorted(t):
            return True 
        else:
            return False
'''

#Another solution without built in functions

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dictionaryS = {}
        dictionaryT = {}
        letterS = ""
        letterT = ""
        for i in range (0, len(s)):
            value = 1
            letterS = s[i]
            if letterS in dictionaryS:
                value = dictionaryS[letterS]
                value += 1 
            dictionaryS[letterS] = value 
            print(dictionaryS) 
        for i in range (0, len(t)):
            value = 1
            letterT = t[i]
            if letterT in dictionaryT:
                value = dictionaryT[letterT]
                value += 1 
            dictionaryT[letterT] = value 
            print(dictionaryT) 
        for i in range (0, len(s)):
            letterS = s[i]
            if letterS not in dictionaryT:
                return False
            if dictionaryS[letterS] != dictionaryT[letterS]:
                return False 
        for i in range (0, len(t)):
            letterT = t[i]
            if letterT not in dictionaryS:
                return False
            if dictionaryS[letterT] != dictionaryT[letterT]:
                return False 
        return True

S = Solution()
print(S.isAnagram("b", "ab"))