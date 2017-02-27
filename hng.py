import random
answer="nai"
d=[]
points=0
puta=False
while answer=="nai":
	e=[]
	print "Ksekinaei h kremala.den epitrepetai na valeis to idio gramma 2 fores.Exeis 9 zwes\n"
	cnt=0
	cnt2=0
	cor=0
	flag=False
	err=0
	y=["axladi","avokanto","parking","patzouri","patzari","pezonafths","kolokutha","mpaniera","sfentona","toksoths","mpetoniera","klimaka","makaronia","ypologisths","plhroforikh","kwdikas"]
	leksi=random.choice(y)
	d=[]

	leksi=list(leksi)

	for i in leksi:
		d.extend('_')
		cnt+=1
	print "".join(d)
	gr=raw_input()
	e.extend(gr)
	for i in leksi:
		cnt2+=1
	while (err<8 and cor<(cnt-1)):
		flag=False
		a=0
		for j in range (cnt2):
			cnt3=0
			if gr==leksi[j]:
				d[j]=gr
				flag=True
				a+=1
		if flag==True:
			cor+=a
		else:
			err+=1

		print "SWSTA:"+str(cor)+"/"+str(cnt) , "LATHI:"+str(err)
		if puta==False:
			print """\n
|-----------------|
|                 |
|                 |
|
|
|
|
|
|
"""
			puta=True
		print "grammata poy xoun xrhshmopoihthei:\n",",".join(e)

		print "leksi:","".join(d)
		gr=raw_input()
		e.extend(gr)

		if err==8:
		       print """
|-----------------|
|                 |
|                 |
|                 O
|               ./|\.
|                 |
|               _/ \_
|               ####
|               fire
|
|\n lupamai,exases
"""
		elif err==7:
       		       print """
|-----------------|
|                 |
|                 |
|                 O
|               ./|\.
|                 |
|               _/ \_
|
|
|
|
"""
		elif err==6:
		       print """
|-----------------|
|                 |
|                 |
|                 O
|               ./|\.
|                 |
|               _/
|
|
|
|
|
						"""
		elif err==5:
			print """
|-----------------|
|                 |
|                 |
|                 O
|               ./|\.
|                 |
|
|
|
|
|
|"""
		elif err==4:
		       print """
|-----------------|
|                 |
|                 |
|                 O
|               ./|\.
|
|
|
|
|
|"""
		elif err==3:
			print"""
|-----------------|
|                 |
|                 |
|                 O
|                 |\.
|
|
|
|
|
|"""
		elif err==2:
		       print """
|-----------------|
|                 |
|                 |
|                 O
|                 |
|
|
|
|
|
|"""
		elif err==1:
			print """
|-----------------|
|                 |
|                 |
|                 O
|
|
|
|
|
|
"""
		else:
			print """\n
|-----------------|
|                 |
|                 |
|
|
|
|
|
|
"""
	if (cor>=(cnt-1)):
		points+=10
	print "POINTS="+str(points)
	answer=str(raw_input("thes na sinexiseis?\npata nai gia sunexeia\n"))
