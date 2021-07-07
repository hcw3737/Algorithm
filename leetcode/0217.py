from itertools import combinations
def maxArea(height) :
    water = []
    for i in range(len(height)-1):
        x1, y1 = i, height[i]
        for j in range(i+1,len(height)) :
            x2, y2 = j , height[j]
            y = min(y1,y2)
            x = x2-x1
            w = x*y
            water.add(w)
    return sorted(list(water),reverse=True)[0]
# >> Time Limit

height = [1,8,6,2,5,4,8,3,7]
print(maxArea(height))



def maxArea(height) :
    water = 0

    for i in range(len(height)-1):
        x1, y1 = i, height[i]
        for j in range(i+1,len(height)) :
            x2, y2 = j , height[j]
            y = min(y1,y2)
            x = x2-x1
            w = x*y
            water.add(w)
    return sorted(list(water),reverse=True)[0]

def maxArea(height) :
    left, right, y = 0, len(height) - 1, 0
    max_water = 0
    while left < right:
        x = (right - left)
        if height[left] <= height[right]:
            y = height[left]
            left += 1
        else:
            y = height[right]
            right -= 1
        max_water = max(x * y, max_water)
    return max_water
