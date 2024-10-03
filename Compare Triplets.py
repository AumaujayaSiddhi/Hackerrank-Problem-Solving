# https://www.hackerrank.com/challenges/compare-the-triplets?isFullScreen=true
def compareTriplets(a, b):
    result = [0,0]
    for x,y in zip(a, b):
        if x>y :
            result[0]+=1
        elif x<y:
            result[1]+=1 
    return result