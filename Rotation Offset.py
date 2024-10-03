# https://www.hackerrank.com/challenges/circular-array-rotation/problem?isFullScreen=true
def circularArrayRotation(a, k, queries):
    k_eff = k % len(a)
    rotation_offset = len(a) - k_eff
    for q in range(len(queries)):
        queries[q] = a[(queries[q]+rotation_offset) % len(a)]
    return queries