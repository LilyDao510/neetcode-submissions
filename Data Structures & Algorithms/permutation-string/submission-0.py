class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
# sol 1 Brute force
        length_1 = len(s1)
        length_2 = len(s2)
        list_s1 = list(s1)
        list_s2 = list(s2)
        new_s1 = sorted(list_s1)

        for i in range(0,length_2-length_1+1):
            new_i = list_s2[i:i+length_1]
            new_i.sort()
            if new_s1 == new_i:
                return True
        return False


