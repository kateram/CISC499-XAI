from collections import deque

from sklearn.base import defaultdict


class Solution:
    def minJumps(self, arr):
        
        queue    = deque()  
        dct      = defaultdict(list)
        vstd_ndx = set()  
        vstd_val = set()  
        arr_l = len(arr)
        for i in range(arr_l - 1, -1, -1):
            dct[arr[i]].append(i)
        
        st_nmb = 0       
        queue.append(0)  
        while queue:
            for _ in range(len(queue)): 
                ndx = queue.popleft()   
                
                if ndx in vstd_ndx:    continue
                if ndx == arr_l - 1:   return st_nmb
                vstd_ndx.add(ndx)      

                val = arr[ndx]
                if val not in vstd_val:  
                    queue.extend(dct[val]) 
                    vstd_val.add(val)      
                if ndx < arr_l:   queue.append(ndx + 1)
                if ndx > 0:       queue.append(ndx - 1)
             
            st_nmb += 1   
        return -1
    
solution = Solution()
print(solution.minJumps([100,-23,-23,404,100,23,23,23,3,404]))