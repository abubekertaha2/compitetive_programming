if __name__ == '__main__':
    N = int(input())
    lst=[]
    for i in range(N):
        cmd = input().strip().split()
        if cmd[0] == "insert":
            index = int(cmd[1])
            value = int(cmd[2])
            lst.insert(index, value)
        elif cmd[0] == "print":
            print(lst)
        elif cmd[0] == "remove":
            value = int(cmd[1])
            lst.remove(value)
        elif cmd[0] == "append":
            value = int(cmd[1])
            lst.append(value)
        elif cmd[0] == "sort":
            lst.sort()
        elif cmd[0] == "pop":
            lst.pop()
        elif cmd[0] == "reverse":
            lst.reverse()
