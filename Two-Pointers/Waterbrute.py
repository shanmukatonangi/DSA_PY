def maxarea_br(heights):
    n=len(heights)
    maxwater=0
    
    for i in range(n):
        for j in range(i+1,n):
            width=j-i
            height=min(heights[i],heights[j])
            area=width*height            
            maxwater=max(maxwater,area)
    
    return maxwater
    
    


heights=[1,7,9,10]
print(maxarea_br(heights))