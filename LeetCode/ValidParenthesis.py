class Solution:
    def isValid(self, s: str) -> bool:
        list_s = list(s)
        opening = ['(','{','[']
        closing = [')','}',']']
        matching_pair = {'(':')','{':'}','[':']'}
        priority = []
        valid = False
        if len(list_s)%2!=0:
            return valid
        for br in list_s:
            if br in opening:
                priority.append(br)
                valid=False
            elif br in closing and priority:
                if matching_pair[priority[len(priority)-1]] == br:
                    priority.pop()
                    if not priority:
                        valid=True
                else:
                    valid=False
                    break
            elif br in closing and not priority:
                valid=False
                break
        return valid
            