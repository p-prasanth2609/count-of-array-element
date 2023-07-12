a=list(map(int,input().split()))
max=a[0]
count=0
for i in range(len(a)):
    if a[i]>max:
        max=a[i]
for i in range(len(a)):
    if a[i]!=max:
        count+=1
print(count)
