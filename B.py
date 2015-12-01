k = 0
m = 0
input=open('input.txt','r')
output=open('output.txt','w')
n=int(input.readline())
a=input.readline.split()
for i in range(n):
  M=int(a[i])
  M=(M-5)//5
  if M==0:
    k-=1
  elif M<(-k):
    k+=M
  else:
    m+=k+M
    k=0
print(m, file=output)
