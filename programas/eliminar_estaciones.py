import sys
import os
carpeta=sys.argv[1]
listado_rinex = os.listdir(carpeta+"/rinex")
archivo_info_n = open (carpeta+"/tables/station.info","r")
archivo_elim = open (carpeta+"/eliminar2.sh","w")

archivo_info=archivo_info_n.readlines()
#limpiar archivo

ano=float(carpeta[-4:])

for est in listado_rinex:
	est_nam=est[:4]
	est_day=ano+float(est[4:7])/366
	sista=0
	linea_temp=""
	for linea in archivo_info:
		if linea[0]!="*" and linea[0]!="#":
			dia1=float(linea[30:33])
			dia2=float(linea[49:52])
			ano1=float(linea[25:29])+dia1/366
			ano2=float(linea[44:48])+dia2/366
			esta=linea[1:5].lower()
			if est_day>=ano1 and est_day<=ano2 and est_nam==esta:
				sista=1
				linea_temp=linea[170:174]

	if sista==1 and len(est)==12 and (linea_temp=="    " or linea_temp=="----" or linea_temp=="3S-0"):
		archivo_elim.write("rm -r rinex/"+est+"\n")

archivo_info_n.close()
archivo_elim.close()