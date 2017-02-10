import math
a=[]
sum=0
sum2=0
cnt1=0
x=raw_input("Please enter a Number.This stops when you hit ENTER with NO INPUT:\n")
while (x!=""):
	a.extend([int(x)])
	x=raw_input()
	cnt1+=1
a.sort()
a = a[2:(cnt1-2)]
print a
for i in range (cnt1-4):
	sum+=a[i]
xm=sum/(cnt1)
for i in range (cnt1-4):
	sum2+=(a[i]-xm)**2
s=math.sqrt(sum2/cnt1)
print s
