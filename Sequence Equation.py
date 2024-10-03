# https://www.hackerrank.com/challenges/permutation-equation/problem?isFullScreen=true
def permutationEquation(p):
    p_dict = dict()
    result = []
    for p_i in range(len(p)):
        p_dict[p[p_i]] = p_i
    
    for i in range(1, len(p)+1):
        result.append(p_dict[p_dict[i]+1]+1)
    return result