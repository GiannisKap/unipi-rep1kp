e=[]
d=[]
cnt=0
cnt2=0
strt=0
sentence=raw_input("Please enter a Sentence:\n")
sentence=list(sentence)
for i in sentence:
    cnt+=1
for i in range (cnt):
    try:
        if sentence[i]==" " and (sentence[i+1]==sentence[i+1].upper()):
            d.append(sentence[strt:i])
            strt=i+1
    except IndexError:
        pass
d.append(sentence[strt:cnt])
for i in d:
    cnt2+=1
for i in range (cnt2):
    d[i]="".join(d[i])
for i in range (cnt2):
    flag=False
    for j in range (len(d[i])):
        if d[i][-1]=="!":
            flag=True
        if d[i][j]!="!":
            e.extend([d[i][j]])
    if flag==True:
        e.extend("!")
    e.extend(" ")
print "".join(e)
