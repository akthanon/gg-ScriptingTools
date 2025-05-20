g = open("posiciones.txt", "r")
glines = g.readlines()
print("NSITES	EWRMS	NWRMS	UWRMS	ENRMS	NNRMS	UNRMS	CODE", end="")

for gline in glines:
	print("\n"+gline[22:24]+"	"+gline[45:49]+"	"+gline[52:56]+"	"+gline[59:63]+"	"+gline[81:86]+"	"+gline[88:93]+"	"+gline[95:100]+"	"+gline[101:112], end="")
print("")
g.close()
