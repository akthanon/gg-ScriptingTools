f = open("estadisticas.txt", "r")
lines = f.readlines()
print("ID	NWRMS	NNRMS	EWRMS	ENRMS	UWRMS	UNRMS")
con=0
for line in lines:
	line=line[6:173]
	if (con==0):
		print(line[5:9]+"	"+line[73:77]+"	"+line[88:93], end="	")
	elif(con==1):
		print(line[73:77]+"	"+line[88:93], end="	")
	else:
		print(line[73:77]+"	"+line[88:93])
	con=con+1
	if (con==3):
		con=0
f.close()