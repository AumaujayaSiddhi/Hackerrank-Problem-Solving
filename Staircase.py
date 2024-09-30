def staircase(n):
    for i in range(1,n+1):
        temp = "#"*i
        print(temp.rjust(n, " "))