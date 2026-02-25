
#find longest substring -> continous

def substrlongest(str):
    maxlen=0
    
    for i in range(i,len(str)): # 0  1 2
        seen=set()  #(a,b) (b,a,c) ,(a)
        for j in range(i,len(str)): #1 2 3
            if str[j] in seen:
                break
            seen.add(str[j])
            
            maxlen=max(maxlen,j-i+1) #1,2,3
            
    return maxlen






str="abac"
