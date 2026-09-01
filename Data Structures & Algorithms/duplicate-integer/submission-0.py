# O(n): best -> O(1), worst -> O(n)

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hasNum = set()
        for number in nums:
            if(number in hasNum):
                return True
            else:
                hasNum.add(number)
        return False
        