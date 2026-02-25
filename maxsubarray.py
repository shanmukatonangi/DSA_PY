def max_sum(arr,k):
    if len(arr)<k:
        return "Array length is less than k"
    
    window_sum=sum(arr[:k])
    max_sum=window_sum
    
    for i in range(k,len(arr)):
        window_sum=window_sum-arr[i-k]+arr[i]
        
        max_sum=max(max_sum,window_sum)
    
    
    return max_sum








arr=[1,4,6,2,8,9,3]
k=3

[2,3,4]
{2:1,3:1,4:1}=3=k

[2,3,3]

{2:1,3:2}=2 !=k


k=3