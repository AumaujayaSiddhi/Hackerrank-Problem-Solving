# https://www.hackerrank.com/challenges/angry-professor/problem?isFullScreen=true
def angryProfessor(k, a):
    present = 0
    for attendance in a:
        present = present + (1 if attendance<=0 else 0)
    return "YES" if present < k else "NO"