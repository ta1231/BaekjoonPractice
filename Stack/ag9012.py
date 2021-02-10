import sys
N = int(sys.stdin.readline())
for i in range(N):
    stack = list(sys.stdin.readline().rstrip())
    while len(stack) != 0:
        temp = stack.copy()
        for i in range(len(stack) - 1):
            if stack[i] == "(" and stack[i + 1] == ")":
                for j in range(2):
                    del(stack[i])
                break
        if temp == stack:
            print("NO")
            break
        else:
            if stack == []:
                print("YES")
                break
            else:
                continue
        
    

              

            
