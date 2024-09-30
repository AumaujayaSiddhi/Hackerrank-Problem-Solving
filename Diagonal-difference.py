# https://www.hackerrank.com/challenges/diagonal-difference?isFullScreen=true
def diagonalDifference(arr, n):
    left_sum = 0
    right_sum = 0
    (i,j) = (0,n-1)
    while i<n and j>-1 :
        left_sum += arr[i][i]
        right_sum += arr[i][j]
        i+=1
        j-=1
    return abs(left_sum-right_sum)