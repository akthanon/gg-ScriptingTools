import sys
carpeta=sys.argv[1]
f = open(carpeta+"/datos/PAW_summary_stats.txt", "r")
lines = f.readlines()

con=0
print("YEAR	DAY	YEARDEC	PAWLF	PANLF")
for line in lines:
	try:
		lini=line
		lini=line.split(":")
		line1=lini[0]
		line2=lini[1]
		year=str(line1.split("/")[1])
		day=str(line1.split("/")[2])
		yeardec=str(float(year)+float(day)/366)[0:10]
		pawlf=str(float(line2[28:33]))
		panlf=str(float(line2[44:49]))
		if not("nan" in line2):
			print(year+"	"+day+"	"+yeardec+"	"+pawlf+"	"+panlf)
	except:
		print("")
f.close()

