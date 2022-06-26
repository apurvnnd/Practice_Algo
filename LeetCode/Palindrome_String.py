

class Solution:
    def isPalindrome(self, x: int) -> bool:
        is_palindrome = False
        if x < 0:
            return is_palindrome
        reversed_number = int("".join(reversed(list(str(x)))))
        if reversed_number == x:
            is_palindrome = True
        return is_palindrome

s = Solution()
print(s.isPalindrome(1424001))