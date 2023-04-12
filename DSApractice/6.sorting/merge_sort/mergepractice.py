  
nums = []
def solutin():
    sq = []
    for i in range(len(nums)):
        c = nums[i] * nums[i]
        sq.append(c)

        def merge(sq,st1,ed1,st2,ed2):
            p1 = st1
            p2 = st2
            
            while p1<=ed1 and p2<=ed2 :
                if sq[p1] < sq[p2] :
                    nums.append(sq[p1])
                    p1 = p1 + 1

                else :
                    nums.append(sq[p2])
                    p2 = p2 + 1

            while p1<=ed1:
                nums.append(sq[p1])
                p1 = p1 + 1  

            while p2<=ed2:
                nums.append(sq[p2])
                p2 = p2 + 1 

            id = 0
            while id < len(nums) :
                sq[st1+id] = nums[id]
                id = id + 1
            
            return nums
           

        low = 0
        high = len(nums)-1
        def mergefuc(nums,low,high):
            mid = (low+high)//2
            if low == high:
                return 
            mergefuc(nums,low,mid)
            mergefuc(nums,mid+1,high)
            merge(nums,low,mid,mid+1,high)
        mergefuc(nums,0,len(sq)-1)      
        