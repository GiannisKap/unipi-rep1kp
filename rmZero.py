a=[]
cnt=0
x=raw_input("Please enter a Number.This stops when you hit ENTER with NO INPUT:\n")
while (x!=""):
	a.extend([int(x)])
	x=raw_input()
	cnt+=1
print a
for i in range(cnt):
	if a[i]== 0:
		a.remove(0)
		a.extend([0])
print a
