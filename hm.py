

nums=[1,2,2,3,4,4,4]
# for num in nums:
#     print(num,nums.count(num))

freq={}

for num in nums:
    if num in freq:
        freq[num] +=1 
    else:
        freq[num]=1
        
        
        # {1:1,2:2}
        
# print(freq)               (nan,0)+1=1
#                          (1,0)+1=2
# freq[nums[num]]=freq.get(nums[num],0)+1



# freq[1]=freq={1:1+1}


# dict={
#     "shanmukh":"123"
# }