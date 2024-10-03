# https://www.hackerrank.com/challenges/find-digits/problem?isFullScreen=true
def findDigits(n):
    n_temp, count = n, 0 
    while n_temp>0:
        digit = n_temp % 10
        try:
            count = count+1 if n % digit == 0 else count
        except ZeroDivisionError:
            pass
        n_temp = n_temp // 10
    return count