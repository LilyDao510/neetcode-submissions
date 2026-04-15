class Solution:
    def isValid(self, s: str) -> bool:
# solution 1:
        for i in s:
            if i =="()" or "{}" or "[]":
                s = s.replace("()","")
                s = s.replace("{}","")
                s = s.replace("[]","")
        return s == ""
            