n= int(input())
arr= list(map(int, input().split()))

if(n==1):
    print(arr[0] * arr[0])
else:
    l1= max(arr)
    arr.pop(arr.index(l1))
    l2= max(arr)
    print(l1 * l2)