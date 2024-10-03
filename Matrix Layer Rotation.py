# https://www.hackerrank.com/challenges/matrix-rotation-algo/problem
def rotateLayer(mat,iterations, m, n, r):
    layer = []
    # Taking respective layer to list
    i, j = iterations, iterations
    while j<n:
        layer.append(mat[i][j])
        j = j+1
    i, j = i+1, j-1
    while i<m:
        layer.append(mat[i][j])
        i = i+1
    i, j = i-1, j-1
    while j>iterations-1:
        layer.append(mat[i][j])
        j = j-1
    i, j = i-1, j+1
    while i>iterations:
        layer.append(mat[i][j])
        i = i-1
    
    # Matrix update after rotation
    i, j = iterations, iterations
    r = r % len(layer)
    layer_index = r
    while j<n:
        if layer_index == len(layer):
            layer_index = 0
        mat[i][j] = layer[layer_index]
        layer_index = layer_index+1
        j = j+1
    i, j = i+1, j-1
    while i<m:
        if layer_index == len(layer):
            layer_index = 0
        mat[i][j] = layer[layer_index]
        layer_index = layer_index+1
        i = i+1
    i, j = i-1, j-1
    while j>iterations-1:
        if layer_index == len(layer):
            layer_index = 0
        mat[i][j] = layer[layer_index]
        layer_index = layer_index+1
        j = j-1
    i, j = i-1, j+1
    while i>iterations:
        if layer_index == len(layer):
            layer_index = 0
        mat[i][j] = layer[layer_index]
        layer_index = layer_index+1
        i = i-1

def matrixRotation(matrix, r, m, n):
    iterations, min_dim = 0, min(m, n)
    while iterations < min_dim//2:
        rotateLayer(matrix, iterations, m-iterations, n-iterations, r)
        iterations = iterations+1
    printMatrix(matrix, m, n)

def printMatrix(matrix, m, n):
    for i in range(m):
        for j in range(n):
            print(matrix[i][j], end=" ")
        print()
