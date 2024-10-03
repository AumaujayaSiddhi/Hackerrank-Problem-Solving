# https://www.hackerrank.com/challenges/append-and-delete?isFullScreen=true
def appendAndDelete(s, t, k):
    (x, y) = (0, 0)
    while x<len(s) and y<len(t):
        if s[x] != t[y]:
            k = k - (len(s)-x) -(len(t)-y)
            break
        (x, y) = (x+1, y+1)

    if x==len(s) and y<len(t):
        k = k - (len(t)-y)
    elif x<len(s) and y==len(t):
        k = k - (len(s)-x)

    return "No" if k<0 or k <= 2*y and k % 2!=0 else "Yes"