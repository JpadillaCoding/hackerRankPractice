def timeConversion(s):
    # Write your code here
    # if time is < 12, return in same time but without am/pm 
    # if >12, do 12+ the time
    # with the answer remove am/pm 
    if 'AM' in s:
        s = s[:8]
        # get without am
        hour = int(s[:2])
        # get the hour
        if (hour == 12):
            s = s.replace(s[:2], "00")
            return s
        return s
    else:
        s = s[:8]
        hour = int(s[:2])
        if hour == 12:
            return s
        millitaryHour = str(hour + 12)
        s = s.replace(s[0:2], millitaryHour)
        return s