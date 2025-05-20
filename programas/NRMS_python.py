import sys
carpeta=sys.argv[1]
f = open(carpeta+"/datos/NRMS_summary_stats.txt", "r")
lines = f.readlines()

con=0
print("YEAR	DAY	YEARDEC	PREFIT1	POSTFIT1	PREFIT2	POSTFIT2	PREFIT3	POSTFIT3	PREFIT4	POSTFIT4")
for line in lines:
	lini=line
	lini=line.split(":")
	line1=lini[0]
	line2=lini[2]
	line3=lini[3]
	year=str(line1.split("/")[1])
	day=str(line1.split("/")[2])
	prefit=str(float(line2[1:13]))
	posfit=str(float(line3[0:12]))
	yeardec=str(float(year)+float(day)/366)[0:10]

	if not ("nan" in prefit or "nan" in posfit):
		if (con==0):
			print(year+"	"+day+"	"+yeardec+"	"+prefit+"	"+posfit, end="	")
		elif(con==1):
			print(prefit+"	"+posfit, end="	")
		elif(con==2):
			print(prefit+"	"+posfit, end="	")
		elif(con==3):
			print(prefit+"	"+posfit)
	con=con+1
	if (con==4):
		con=0
f.close()
