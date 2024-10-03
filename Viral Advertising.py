# https://hackerrank.com/challenges/strange-advertising/problem?isFullScreen=true
def viralAdvertising(n):
    cum_likes, likes = 2, 2
    for day in range(1, n):
        likes = (likes*3)//2
        cum_likes = cum_likes + likes
    return cum_likes