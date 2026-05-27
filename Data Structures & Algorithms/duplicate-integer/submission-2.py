class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        lst =[]
        for i in nums:
            if i not in lst:
                lst.append(i)
            else:
                return True
        return False

































        # Cach 1

        # map= {}
        # for i in nums:
        #     if i in map:
        #         map[i] += 1
        #         if map[i] >1:
        #             return True
        #     else:
        #         map[i] = 1
        # return False

        # Cach 2

        # my_set = set()
        # for i in nums:
        #     if i in my_set:
        #         return True
        #     else:
        #         my_set.add(i)
        # return False
        
        
        
        
        # new_map = {}
        # l = len(nums)
        # for i in range(l):
        #     if nums[i] in new_map:
        #         new_map[nums[i]] += 1
        #     else:
        #         new_map[nums[i]] = 1

        #     if new_map[nums[i]]> 1:
        #         return True
        # return False
        




        
       


            
        