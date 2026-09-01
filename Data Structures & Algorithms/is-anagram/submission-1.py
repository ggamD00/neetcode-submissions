class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        check = {}
        for c in s:
            check[c] = check.get(c, 0) + 1

        for c in t:
            check[c] = check.get(c, 0) - 1
        
        for c in check:
            if check[c] != 0:
                return False

        return True