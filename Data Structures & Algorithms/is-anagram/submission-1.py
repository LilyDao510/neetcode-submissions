class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        map_s={}
        map_t ={}
        len_s = len(s)
        len_t = len(t)

        for i in range(len_s):
            if s[i] in map_s:
                map_s[s[i]] += 1
            else:
                map_s[s[i]]= 1
        
        for j in range(len_t):
            if t[j] in map_t:
                map_t[t[j]] +=1
            else:
                map_t[t[j]]= 1
        
        if map_s == map_t:
            return True
        

    































        # n = len(s)
        
        # m = len(t)

        # if n != m:
        #     return False
        # counts= {}
        # countt= {}
        # for i in range(n):
        #     counts[s[i]] = 1 + counts.get(s[i],0)
        #     countt[t[i]] = 1 + countt.get(t[i],0)
        # return counts == countt

# cach 1
        n = len(s)
        l = len(t)

        if n != l:
            return False

        count_s = {}
        count_t = {}

        for char in s:
            count_s[char] = count_s.get(char,0) + 1
        
        for char in t:
            count_t[char] = count_t.get(char,0) + 1
        
        return count_s == count_t



























