# def eval():
#     m = int(input())
#     mat = [input().strip() for _ in range(m)]
#     if len(mat)==2:
#         return 0
#     cnt =0
#     for i in range(len(mat)):
#         for j in range(len(mat[0])):
#             if (0 <= i-1 < len(mat) and 0 <= j-1 < len(mat[0])) and (0 <= i+1 < len(mat) and 0 <= j+1 < len(mat[0])):
#                 if mat[i][j] == "X":
#                     if mat[i-1][j-1] =="X" and mat[i-1][j+1] =="X" and mat[i+1][j+1] =="X" and mat[i+1][j-1] =="X":
#                         cnt +=1
#     return cnt

ans = eval()
print(ans)
def eval():
    m = int(input())
    mat = [input().strip() for _ in range(m)]
    
    if len(mat) < 3 or len(mat[0]) < 3:
        return 0
    
    cnt = 0
    for i in range(1, len(mat) - 1): 
        for j in range(1, len(mat[0]) - 1):  
            if mat[i][j] == "X":
                if (mat[i-1][j-1] == "X" and
                    mat[i-1][j+1] == "X" and
                    mat[i+1][j-1] == "X" and
                    mat[i+1][j+1] == "X"):
                    cnt += 1
    
    return cnt

ans = eval()
print(ans)
