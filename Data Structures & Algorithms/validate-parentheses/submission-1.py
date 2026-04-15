class Solution:
    def isValid(self, s: str) -> bool:

# solution 1:
        stack =[]
        dictS ={'(':')', '{':'}','[':']'}
        for i in s:
            if i in dictS:
                stack.append(i)
            elif len(stack) == 0 or i != dictS[stack.pop()]:
                return False
        return len(stack)==0


# solution 2:
        # for i in s:
        #     if i =="()" or "{}" or "[]":
        #         s = s.replace("()","")
        #         s = s.replace("{}","")
        #         s = s.replace("[]","")
        # return s == ""
            