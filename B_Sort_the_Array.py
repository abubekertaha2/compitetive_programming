def sort():
    n = int(input())
    a = list(map(int, input().split()))

    b = sorted(a)

    if a == b:
        print("yes")
        print(1, 1)
        return

    diff_indx = []
    for i in range(n):
        if a[i] != b[i]:
            diff_indx.append(i)

    if len(diff_indx) ==0:
      print("yes")
      print(1,1)
      return

    start = diff_indx[0]
    end = diff_indx[-1]

    new_a = a[:start] + a[start:end+1][::-1] + a[end+1:]

    if new_a == b:
        print("yes")
        print(start + 1, end + 1)
    else:
        print("no")

sort()
