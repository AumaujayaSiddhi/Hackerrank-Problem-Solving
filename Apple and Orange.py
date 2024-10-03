# https://www.hackerrank.com/challenges/apple-and-orange?isFullScreen=true
def countApplesAndOranges(s, t, a, b, apples, oranges):
    (n_apples, n_oranges) = (0, 0)
    for x in apples:
        if x+a >= s and x+a <=t:
            n_apples += 1
    for y in oranges:
        if y+b >= s and y+b <= t:
            n_oranges += 1
    print("{n1}\n{n2}".format(n1=n_apples, n2=n_oranges))