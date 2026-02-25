def max_subarray(arr,k):
    n=len(arr)
    if len(arr)<k:
        return "Array size is lesser than k"
    
    max_sum=0
    
    for i in range(n-k+1):
        current_sum=0
        for j in range(i,i+k):
            current_sum+=arr[j]
            
        if current_sum>max_sum:
            max_sum=current_sum
            
    return max_sum






arr=[1,4,6,2,8,9,3]
k=3