class Solution:
    def isValid(self, s: str) -> bool:
        list_s = list(s)
        matching_pair = {'(':')','{':'}','[':']'}
        priority = []
        valid = False
        if len(list_s)%2!=0:
            return valid
        for br in list_s:
            if br in matching_pair.keys():
                priority.append(br)
                valid=False
            elif priority:
                if matching_pair[priority[len(priority)-1]] == br:
                    priority.pop()
                    if not priority:
                        valid=True
                else:
                    valid=False
                    break
            else:
                valid=False
                break
        return valid