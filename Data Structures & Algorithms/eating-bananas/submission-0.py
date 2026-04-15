class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l,r = 1, max(piles)
        res = r
        while l <= r:
            total_hour = 0
            for i in piles:
                mid = (l+r)//2
                total_hour += math.ceil(float(i)/mid)
            if total_hour <=h:
                k = mid
                r = mid - 1
            else:
                l = mid + 1
        return k



       



        

        
        