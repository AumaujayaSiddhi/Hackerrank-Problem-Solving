# https://www.hackerrank.com/challenges/time-conversion?isFullScreen=true
def timeConversion(s):
    timeline = s[-2:]
    time = s[0:len(s)-2].split(":")
    if "PM" == timeline:
        if time[0] != "12":
            time[0] = str(int(time[0])+12)
    elif "AM" == timeline:
        if time[0] == "12":
            time[0] = "00"
    return ":".join(time)