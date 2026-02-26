def longestsubstring(str):
    last={}
    start=0
    maxlen=0
    
    
     
    
    for end,ch in enumerate(str):
        if ch in last:
            start=last[ch]+1
        last[ch]=end
        maxlen=max(maxlen,end-start+1)
        
    return maxlen
        
        
        
        
        
        
        
        
 
        
        
        
        
str="abad"
print(longestsubstring(str))