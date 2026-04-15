class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # solution 1: bruce force
        # l = len(temperatures)
        # result = [0]*l

        # for i in range(l):
        #     for j in range(i+1,l):
        #         if temperatures[j]> temperatures[i]:
        #             result[i] = int(j)-int(i)
        #             break
        #         else:
        #             result[i] == 0
        # return result


        # slotuion 2: stack
        l = len(temperatures)
        result = [0]*l
        stack=[]

        for i in range(l):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                prev_day= stack.pop()
                result[prev_day] = i - prev_day

            stack.append(i)
        return result

