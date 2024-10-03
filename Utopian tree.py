# https://www.hackerrank.com/challenges/utopian-tree/problem?isFullScreen=true
def utopianTree(n):
    tree_height = 0
    for cycle in range(n+1):
        tree_height = tree_height+1 if cycle % 2==0 else tree_height*2
    return tree_height