import sys
N = int(sys.stdin.readline())
deque = []
for i in range(N):
    read_line = sys.stdin.readline().rstrip().split()
    
    if read_line[0] == "push_front":
        deque.insert(0, read_line[1])
    elif read_line[0] == "push_back":
        deque.append(read_line[1])
    elif read_line[0] == "pop_front":
        if len(deque) == 0:
            print(-1)
        else: 
            print(deque[0])
            del(deque[0])
    elif read_line[0] == "pop_back":
        if len(deque) == 0:
            print(-1)
        else:
            print(deque.pop())
    elif read_line[0] == "size":
        print(len(deque))
    elif read_line[0] == "empty":
        if len(deque) == 0:
            print(1)
        else:
            print(0)
    elif read_line[0] == "front":
        if len(deque) == 0:
            print(-1)
        else:
            print(deque[0])
    elif read_line[0] == "back":
        if len(deque) == 0:
            print(-1)
        else:
            print(deque[-1])