hour, minute = map(int, input().split())

time = hour * 60 + minute
if time < 45:
    time = time + 1440
time = time - 45
Shour = time // 60
Sminute = time % 60

print("{0} {1}".format(Shour, Sminute))
