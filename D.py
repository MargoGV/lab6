p=0
input=open('input.txt','r')
output=open('output.txt','w')
b=input.readline().split()
p=int(b[0])
n=int(b[1])
a=input.readline().split()
for i in range(p-1):
    a1=input.readline().split()
    for j in range(n):
        a[j]=min(int(a1[j]),int(a[j]))
for i in range(n):
    print(a[i],end=' ',file=output)
