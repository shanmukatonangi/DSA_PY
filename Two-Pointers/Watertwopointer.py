def maxarea_tp(heights):
    left=0
    right=len(heights)-1
    maxwater=0
    
    while(left<right):
        width=right-left
        height=min(heights[left],heights[right])
        area=width*height
        maxwater=max(maxwater,area)
        
        if heights[left]<heights[right]:
            left=left+1
        else:
            right=right-1
            
    return maxwater
         



heights=[1,7,9,10]
print(maxarea_tp(heights))