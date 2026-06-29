#leet code problem no 347
def topKFrequent(self, nums, k):
        hmap={}
        for i in nums :
            if i in hmap :
                hmap[i] += 1
            else :
                hmap[i] = 1
        rt = []
        for i in range(0 , k):
            maxv = max(hmap , key=hmap.get)
            rt.append(maxv) 
            hmap[maxv] = -1
        return rt
