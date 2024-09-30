# https://www.hackerrank.com/challenges/divisible-sum-pairs/problem
def findPairs(l1, l2):
    (i, j, count) = (1, 1, 0)
    while i<len(l1) and j<len(l2):
        if l1[i] == l2[j]:
            # This condition will only hit if elements of ar are k's multiples. In that case we add (n*(n-1))//2 to count
            count = ((len(l1)-2) * (len(l1)-1))//2
            break
        elif l1[i] < l2[j]:
            # Count the pairs with all the remaining elements of j 
            (count, i) = (count+len(l2)-j, i+1)
        else:
            # Count the pairs with all the remaining elements of i
            (count, j) = (count+len(l1)-i, j+1)
    return count

def divisibleSumPairsMethod1(n, k, ar):
    """
    Total time complexity : O(n)
    """
    keys_dict = dict()
    count = 0
    """
    1. Take modulo of each and every element of ar
    2. Set default value of key ar[index] to be list(0) if ar[index] doesnot exist
       else append index to list corresponding to ar[index]
    3. Time complexity : O(n)
    """
    for x in range(len(ar)):
        ar[x] = ar[x] % k
        keys_dict.setdefault(ar[x], [0])
        keys_dict[ar[x]].append(x)
    
    """
    Time complexity : O(n)
    """
    for x in range(len(ar)):
        if keys_dict[ar[x]][0] == 0:
            arx_pair = k - ar[x] if ar[x]!=0 else 0
            keys_dict[ar[x]][0] = 1
            if keys_dict.get(arx_pair, -1) != -1:
                count = count + findPairs(keys_dict[ar[x]], keys_dict[arx_pair])
                keys_dict[arx_pair][0] = 1

    return count

def divisibleSumPairsMethod2(n, k, ar):
    """
    Total time complexity : O(n^2)
    """
    count = 0
    for i in range(len(ar)):
        for j in range(i+1, len(ar)):
            if (ar[i] + ar[j]) % k == 0:
                count += 1
    return count