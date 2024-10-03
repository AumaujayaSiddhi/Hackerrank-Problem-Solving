# https://www.hackerrank.com/challenges/beautiful-days-at-the-movies/problem?isFullScreen=true
def findReverse(n):
    n_rev = str()
    while n>0:
        n_rev = "".join([n_rev, str(n%10)])
        n //= 10
    return int(n_rev)

def beautifulDays(i, j, k):
    result = 0
    for num in range(i, j+1):
        num_reverse = findReverse(num)
        result = result + (1 if abs(num-num_reverse) % k == 0 else 0)
    return result