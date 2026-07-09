class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # sorted() should return a sorted list of the characters in each string and
        # and then I am just trying to see if the are equal
        #if sorted(s) == sorted(t):
        #    return True
        #else:
        #    return False  

        if len(s) != len(t):
            return False

        sict = {}
        tict = {}

        for letters in s:
            sict[letters] = sict.get(letters, 0) + 1
        for letters in t:
            tict[letters] = tict.get(letters, 0) + 1 
            
        if sict == tict:
            return True
        else:
            return False              
        