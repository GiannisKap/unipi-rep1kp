cnt1=0
cnt2=0
a=str(raw_input("Please enter a parenthesis sequence:\n"))
flag=False
for j in range (len(a)):
	if (a[0]=="(" and a[-1]==")"):
		if a[j]=='(' :
			cnt1+=1
		elif a[j]==str(")"):
			cnt2+=1
if (cnt1==cnt2 and cnt2!=0):
	flag=True
print flag
