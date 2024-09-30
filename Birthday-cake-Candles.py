# https://www.hackerrank.com/challenges/birthday-cake-candles?isFullScreen=true
def birthdayCakeCandles(candles):
    (max_ele, count) = (max(candles), 0)
    for x in candles:
        if x==max_ele:
            count+=1
    return count