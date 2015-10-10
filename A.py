file1=open('intinput.txt','w')
A=input()
B=input()
file1.write(A+'\n'+B)
file1=open('intinput.txt','r')
file2=open('output.txt','w')
i=0
n=0
while i<=len(B)-2:
	if int(B[i])==int(B[i+2]):
		n=B[i]
	i+=2
file2.write(str(n))
file1.close
