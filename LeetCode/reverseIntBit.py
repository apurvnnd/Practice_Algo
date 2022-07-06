class Solution:
    def reverse(self, x: int) -> int:
        str_x = 1
        if x<0:
            str_x = -1
        val = int(''.join(list(reversed(list(str(abs(x)))))))
        return  str_x*val if abs(val) < 2**31 else 0