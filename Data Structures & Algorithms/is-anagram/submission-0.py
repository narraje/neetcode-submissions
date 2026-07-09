class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # sorted() should return a sorted list of the characters in each string and
        # and then I am just trying to see if the are equal
        if sorted(s) == sorted(t):
            return True
        else:
            return False    
        