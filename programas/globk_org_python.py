import sys
carpeta=sys.argv[1]

f = open(carpeta+"/datos/globk_org_stats.txt", "r")
lines = f.readlines()
print("YEAR	DAY	YEARDEC	NITER	PRERMS	POSTRMS")
aniter=0
antxt="NA"

for line in lines:
	lini=line
	line=line.split(":")
	line1=line[0]
	line2=line[1]
	niter=float(line2[25:26])
	year=line1.split("/")[1]
	day=line1.split("/")[3][13:16]
	yeardec=str(float(year)+float(day)/366)[0:10]
	prerms=line2[38:44]
	posrms=line2[59:66]
	if (niter>aniter):
		antxt=str(year+"	"+day+"	"+yeardec+"	"+str(niter)+"	"+prerms+"	"+posrms)
		aniter=niter
	else:
		print(antxt)
		aniter=0
print(antxt)
f.close()
