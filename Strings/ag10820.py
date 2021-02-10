import sys
while True:
    inp = sys.stdin.readline().rstrip('\n')
    if not inp:
        break
    s = 0
    b = 0
    num = 0
    n = 0
    for i in inp:
        if ord(i)>= ord('a') and ord(i) <= ord('z'):
            s += 1
        elif ord(i) >= ord('A') and ord(i) <= ord('Z'):
            b += 1
        elif ord(i) == ord(' '):
            n += 1
        elif ord(i) >= ord('0') and ord(i) <= ord('9'):
            num += 1
    print("{0} {1} {2} {3}".format(s, b, num, n))
    
