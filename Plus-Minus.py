# https://www.hackerrank.com/challenges/plus-minus?isFullScreen=true
def plusMinus(arr, n):
    (positive, negative, zero) = (0, 0, 0) 
    for x in arr:
        if x>0:
            positive += 1
        elif x<0:
            negative +=1
        else:
            zero += 1
    print("%.6f\n%.6f\n%.6f" %(positive/n, negative/n, zero/n))