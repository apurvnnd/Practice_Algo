class Solution:
    def romanToInt(self, s: str) -> int:
        romanDigitValues = {'M':1000,'D':500,'C':100,'L':50,'X':10,'V':5,'I':1}
        romanNumberList = list(s)
        romanNumberPriority = {'M':7,'D':6,'C':5,'L':4,'X':3,'V':2,'I':1}
        prevNumberWeight = 0
        new_s = ''
        for romanNumber in romanNumberList:
            if prevNumberWeight== 0:
                prevNumberWeight = romanNumberPriority[romanNumber]
                new_s = romanNumber  
            else:
                if prevNumberWeight >= romanNumberPriority[romanNumber]:
                    new_s = f'{new_s}+{romanNumber}'
                    prevNumberWeight = romanNumberPriority[romanNumber]
                else:
                    new_s = f'{new_s[:-2]}-{new_s[-1]}+{romanNumber}'
                    prevNumberWeight = romanNumberPriority[romanNumber]
        for l in list(new_s):
            if l in romanDigitValues.keys():
                new_s = new_s.replace(l,str(romanDigitValues[l]))
        return eval(new_s)


s = Solution()
print(s.romanToInt('III'))