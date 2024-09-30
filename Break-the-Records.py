# https://www.hackerrank.com/challenges/breaking-best-and-worst-records/problem?isFullScreen=true
def breakingRecords(scores):
    (high_score, low_score) = (scores[0], scores[0])
    (high_break, low_break) = (0, 0)
    for score in scores:
        if score > high_score:
            high_score = score
            high_break += 1
        if score < low_score:
            low_score = score
            low_break += 1
    return list([high_break, low_break])