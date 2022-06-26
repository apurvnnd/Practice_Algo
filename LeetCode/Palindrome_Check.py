import math

class Solution:
    def isPalindrome(self, x: int) -> bool:
        new_number = x
        digits_arr = []
        while new_number != 0:
            last_digit = new_number%10
            digits_arr.append(last_digit)
            new_number = math.trunc(new_number/10)
        digits_power = len(digits_arr)
        reversed_number = sum([digits_arr[i]*(10**(digits_power-i-1)) for i in range(len(digits_arr))])
        is_palindrome = False
        if reversed_number == x:
            is_palindrome = True
        return is_palindrome

s = Solution()
print(s.isPalindrome(-141141))