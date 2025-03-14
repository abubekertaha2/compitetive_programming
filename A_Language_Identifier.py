t = int(input())
for _ in range(t):
    s = input()
    lst = s.split("_")
    s1 = lst[-1]
    if s1[-1] == "o":
        print("FILIPINO")
    elif s1[-1]=="u":
        print("JAPANESE")
    elif s1[-1] =="a":
        print("KOREAN")