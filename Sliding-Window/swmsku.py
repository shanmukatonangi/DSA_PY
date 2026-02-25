def maxsumkunique(nums,k):
    freq={}
    left=0
    curr_sum=0
    maxsum=0
    #nums=[1,2,3,4,3]
    #freq={3:2,4:1}
    #left=2
    #cs=0
    #maxs=0
    
    for right in range(len(nums)): 
        # freq[nums[right]]=freq.get(nums[right] , 0)+1   --- 0 1 2 3 4
        if nums[right] in freq:
         freq[nums[right]] += 1
        else:
         freq[nums[right]] = 1
        #  freq[1]=1
        curr_sum= curr_sum+nums[right]  #0  -> 1 -> 3   ->6+4
        
        #if window is greater than k we are shrinking it
        if right-left+1 > k:
            freq[nums[left]] -=1
            curr_sum -=nums[left]  #10-1 =9-2+3=10
            
            if freq[nums[left]]==0:
                del freq[nums[left]]
        
            left=left+1
           
          #if window is eqauls to k we are adding the subarraysum to max sum
        if right-left+1 == k:
            if len(freq)== k:
                maxsum=max(maxsum,curr_sum)  #6,#9
            
            
          
    return maxsum
        
        
    #    nums[left:right+1]     
        
nums=[1,2,3,4,3]

print(maxsumkunique(nums,3))

