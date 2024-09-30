def miniMaxSum(arr):
    (min_ele, max_ele) = (arr.index(min(arr)), arr.index(max(arr)))
    (min_sum, max_sum) = (0, 0)
    for x in range(len(arr)):
        if x!=min_ele:
            max_sum += arr[x]
        if x!=max_ele:
            min_sum += arr[x]
    print("{n1} {n2}".format(n1 = min_sum, n2 = max_sum))