# https://www.hackerrank.com/challenges/bon-appetit/problem?isFullScreen=true
def bonAppetit(bills, k, b):
    total_bill_anna = 0
    for bill in range(len(bills)):
        if bill != k:
            total_bill_anna += bills[bill]
    total_bill_anna = total_bill_anna // 2
    print("Bon Appetit" if total_bill_anna == b else b-total_bill_anna)