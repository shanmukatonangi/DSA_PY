def max_sum_k_unique(nums,k):
    maxsum=0
    n=len(nums)
    
    for i in range(n-k+1):
        subarray=nums[i:i+k]
        
        
        if len(set(subarray)) == k:
            currentsum=sum(subarray)
            maxsum=max(maxsum,currentsum)
          
    return maxsum    
        
    





nums=[1,2,3,4,3]
k=3

print(max_sum_k_unique(nums,k))