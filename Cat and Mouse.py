# https://www.hackerrank.com/challenges/cats-and-a-mouse/problem?isFullScreen=true
def catAndMouse(x, y, z):
    d_CatA_Mouse = abs(x-z)
    d_CatB_Mouse = abs(y-z)
    return "Mouse C" if d_CatA_Mouse==d_CatB_Mouse else "Cat A" if d_CatA_Mouse<d_CatB_Mouse else "Cat B" 
