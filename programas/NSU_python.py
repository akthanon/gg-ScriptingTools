import sys
carpeta=sys.argv[1]
f = open(carpeta+"/datos/NSU_summary_stats.txt", "r")
lines = f.readlines()
print("YEAR	DAY	YEARDEC	SinUt	NoSU	TXfiles")
dif=0
diferentes=[]
for line in lines:
	try:
		lini=line
		lini=line.split(":")
		line1=lini[0]
		line2=lini[1].split(" ")
		year=str(line1.split("/")[1])
		day=str(line1.split("/")[2])
		yeardec=str(float(year)+float(day)/366)[0:10]


		nosu=line2[4]
		txfi=line2[7]
		dif=float(txfi)-float(nosu)


		if (dif!=0):
			diferentes.append(line)
		print(year+"	"+day+"	"+yeardec+"	"+str(dif)+"	"+nosu+"	"+txfi, end="")
	except:
		print("")
f.close()

