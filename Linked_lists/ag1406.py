import sys
inp = sys.stdin.readline().rstrip()
N = int(sys.stdin.readline())
temp = len(inp)
for i in range(N):
    cmd = sys.stdin.readline().rstrip().split()
    if cmd[0] == 'L':
        if temp == 0:
            continue
        else:
            temp -= 1
    elif cmd[0] == 'D':
        if temp == len(inp):
            continue
        else:
            temp += 1
    elif cmd[0] == 'B':
        if temp == 0:
            continue
        else:
            inp = inp[0:temp-1] + inp[temp:]            
    elif cmd[0] == 'P':
        inp = inp[0:temp] + cmd[1] + inp[temp:]
print(inp)