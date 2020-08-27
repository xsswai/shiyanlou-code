
for i in range(1,101):
	a=i/100,b=i/10%10,c=i%10
	if (i%7 !== 0) and (a!==7 and b!==7 and c!==7):
		print(i,end='/n')

