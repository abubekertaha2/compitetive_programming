#bubble sort method
"""arr = [64, 25, 12, 22, 11]
l=len(arr)
for i in range(l):
    for j in range(l-1-i):
        if arr[j] > arr[j+1]:
            arr[j], arr[j+1]= arr[j+1] , arr[j]
print(arr)"""
"""#slecction srot method
arr1 = [5,2,7,3,6,0]
l = len(arr1)
for i in range(l):
    min_indx = i
    for j in range(i+1,l):
        if arr1[min_indx] > arr1[j]:
            min_indx = j
    arr1[i], arr1[min_indx] = arr1[min_indx], arr1[i]
print(arr1)"""
"""array = [64, 25, 12, 22, 11]
size = len(array)
for i in range(1, size):
    key = array[i]
    j = i - 1
    while j >= 0 and key < array[j]:
        array[j + 1] = array[j]
        j -= 1
    array[j + 1] = key
print(array)"""
#count sorting method
"""count = [0] * (maxi + 1)
for i in arr2 :
    count [i] +=1
target= 0
for indx , val in enumerate(count):
    for i in range(val):
        arr2[target] = indx
        target+=1
print(count)
print(arr2)
"""
"""costs = [1,3,2,5,1,3]
students = [1,2,3,4,5,6]
student_dict={}
for idx in range(len(students)):
    student_dict[students[idx]]= costs[idx]
print(student_dict)
def sorted_stu(itm):
    return student_dict[itm]
students.sort(key=sorted_stu)
print(students)
dct = dict(zip(students,costs))
student = sorted(students, key = lambda x : dct[x])
print(student)"""
