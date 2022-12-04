def isSubset(arr1, arr2, m, n):
    i = 0
 
    quickSort(arr1, 0, m-1)
    for i in range(n):
        if (binarySearch(arr1, 0, m - 1, arr2[i]) == -1):
            return 0
 
    return 1
 

def binarySearch(arr, low, high, x):
    if(high >= low):
        mid = (low + high)//2
 
        if((mid == 0 or x > arr[mid-1]) and (arr[mid] == x)):
            return mid
        elif(x > arr[mid]):
            return binarySearch(arr, (mid + 1), high, x)
        else:
            return binarySearch(arr, low, (mid - 1), x)
 
    return -1
 
 
def partition(A, si, ei):
    x = A[ei]
    i = (si - 1)
 
    for j in range(si, ei):
        if(A[j] <= x):
            i += 1
            A[i], A[j] = A[j], A[i]
    A[i + 1], A[ei] = A[ei], A[i + 1]
    return (i + 1)
 
def quickSort(A, si, ei):
    if(si < ei):
        pi = partition(A, si, ei)
        quickSort(A, si, pi - 1)
        quickSort(A, pi + 1, ei)
 
# Driver code
count = 0

with open('C:/Users/Kyleq/OneDrive/src/AOC2022/Day4/test.txt') as f:
    lines = f.read().split('\n')

    for l in lines:
        pair = l.split(',')
        str1 = pair[0]
        str2 = pair[1]

        str1_split = str1.split('-')
        str2_split = str2.split('-')

        str1_start = int(str1_split[0])
        str1_end = int(str1_split[len(str1_split)-1])
        str2_start = int(str2_split[0])
        str2_end = int(str2_split[len(str2_split)-1])
        
        if (str1_start == str1_end):
            list1 = [str1_start]
        else:
            list1 = list(range(str1_start, str1_end + 1))

        if (str2_start == str2_end):
            list2 = [str2_start]
        else:
            list2 = list(range(str2_start, str2_end + 1))

        m = len(list1)
        n = len(list2)

        if(isSubset(list1, list2, m, n)) or (isSubset(list2, list1, n, m)):
            count += 1
        
print(count)
