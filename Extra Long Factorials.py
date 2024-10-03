# https://www.hackerrank.com/challenges/extra-long-factorials?isFullScreen=true
def extraLongFactorials(n):
    mul_cum = 1
    for x in range(1, n+1):
        mul_cum *= x
    print(mul_cum)