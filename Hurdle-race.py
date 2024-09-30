# https://www.hackerrank.com/challenges/the-hurdle-race/problem?isFullScreen=true
def hurdleRace(k, height):
    max_wall_height = max(height)
    return max_wall_height-k if k < max_wall_height else 0