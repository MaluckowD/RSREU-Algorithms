def largest_rectangle_area(heights): 
    stack = [] 
    max_area = 0 
    heights.append(0) 
 
    for i in range(len(heights)): 
        while stack and heights[stack[-1]] > heights[i]: 
            h = heights[stack.pop()] 
            w = i if not stack else i - stack[-1] - 1 
            max_area = max(max_area, h * w) 
 
        stack.append(i) 
 
    return max_area 
 
 
heights = [int(x) for x in input().split()] 
N = heights.pop(0) 
 
max_area = largest_rectangle_area(heights) 
 
print(max_area)
