class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # cach 1:
        new_dict ={}
        for num in nums:
            if num not in new_dict:
                new_dict[num] = 1
            else:
                new_dict[num] += 1

        new_arr =[]

        for i, count in new_dict.items():
            new_arr.append([count,i])
        new_arr.sort()

        res=[]

        while len(res) < k:
            res.append(new_arr.pop()[1])
        return res


        

































    
    
    # tao dict de dem so lan lap lai cua cac nums
    # sort cac phan tu trong dict
    # lay k phan tu co so lan lap lai lon nhat

        dictN = {}
        for num in nums:
            dictN[num] = 1 + dictN.get(num,0)

        arr =[]
        for num,cnt in dictN.items():
            arr.append([cnt,num])
        arr.sort()

        res = []
        while len(res) <k:
            res.append(arr.pop()[1])
        return res







        