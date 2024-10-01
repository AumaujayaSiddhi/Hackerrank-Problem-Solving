# https://hackerrank.com/challenges/counting-valleys/problem?isFullScreen=true
def move(sea_level, path, i):
    while i<len(path):
        sea_level = sea_level + (-1 if path[i]=="D" else 1)
        if sea_level == 0:
            i = i+1
            return sea_level, i, 1
        i = i+1
    return sea_level, i, 0

def countingValleys(steps, path):
    """
    Time Complexity : O(n)
    Space Complexity : O(1)
    """
    sea_level, valley_count, i = 0, 0, 0
    while i < len(path):
        if path[i]=="D":
            sea_level, i = sea_level - 1, i+1
            sea_level, i, c = move(sea_level, path, i)
            valley_count = valley_count+c
        else:
            sea_level, i = sea_level + 1, i+1
            sea_level, i, c = move(sea_level, path, i)
    return valley_count