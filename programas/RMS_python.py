import sys
carpeta=sys.argv[1]
f = open(carpeta+"/datos/RMS_summary_stats.txt", "r")
lines = f.readlines()

con=0
print("YEAR	DAY YEARDEC	ALL	BEST1	BEST2	WORST1	WORST2")
for line in lines:
	lini=line
	lini=line.split(":")
	line1=lini[0]
	year=str(line1.split("/")[1])
	day=str(line1.split("/")[2])
	yeardec=str(float(year)+float(day)/366)[0:10]
	line2=lini[1]
	if not ("All" in line2):
		allst=str(float(line2[14:19]))
	if (con==1):
		print(year+"	"+day+"	"+yeardec+"	"+allst, end="	")
	elif(con==2):
		print(allst, end="	")
	elif(con==3):
		print(allst, end="	")
	elif(con==4):
		print(allst, end="	")
	elif(con==5):
		print(allst)
	con=con+1
	if (con==6):
		con=0
f.close()
