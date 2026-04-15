class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left, right = 0,0
        l = len(s)
        sub_str = set()
        max_length = 0
        for right in range(l):
            while s[right] in sub_str:
                sub_str.remove(s[left])
                left += 1
            sub_str.add(s[right])
            max_length = max(max_length,right - left +1)
        return max_length



        