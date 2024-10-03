# https://www.hackerrank.com/challenges/the-birthday-bar?isFullScreen=true
def birthday(s, d, m):
    (i, j, count, summ, diff) = (0, 0, 0, 0, 0)
    while j < len(s):
        if summ < d and diff < m:
            summ = summ + s[j]
            diff = diff + 1
            j += 1
            continue
        if summ == d and diff == m:
            count += 1
        summ = summ - s[i]
        diff = diff - 1
        i += 1
    return count + 1 if summ == d and diff == m else count