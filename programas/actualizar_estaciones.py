import sys
import os
cabecera="# Station.info written by MSTINF user deon             on 2022-07-21  05:04\n* Reference file : station.info\n*\n*\n*SITE  Station Name      Session Start      Session Stop       Ant Ht   HtCod  Ant N    Ant E    Receiver Type         Vers                  SwVer  Receiver SN           Antenna Type     Dome   Antenna SN           \n"

carpeta=sys.argv[1]
listado_rinex = os.listdir(carpeta+"/rinex")
archivo_info_a = open (carpeta+"/tables/INFO_STATION","r")
archivo_info_n = open (carpeta+"/tables/station.info","w")
archivo_elim = open (carpeta+"/eliminar.sh","w")
archivo_upt = open (carpeta+"/actualizar.sh","w")

archivo_info=archivo_info_a.readlines()
#limpiar archivo
listado_solo_rinex=[]
for est in listado_rinex:
	if len(est)!=12:
		archivo_elim.write("rm -r rinex/"+est+"\n")
	if not(est[:4] in listado_solo_rinex):
		listado_solo_rinex.append(est[:4])

ano=float(carpeta[-4:])
new_archivo=[]
for linea in archivo_info:
	if len(linea)>10 and linea[0]!="*" and linea[0]!="#" and not("--" in linea[171:180]):
		ano1=float(linea[25:29])
		ano2=float(linea[44:48])
		esta=linea[1:5].lower()
		if ano>=ano1 and ano<=ano2:
			new_archivo.append(linea)

new_solo_rinex=[]
for linea in new_archivo:
	esta=linea[1:5].lower()
	if esta in listado_solo_rinex:
		new_solo_rinex.append(linea)

for est in listado_rinex:
	est_nam=est[:4]
	est_day=ano+float(est[4:7])/366
	sista=0
	for linea in new_solo_rinex:
		dia1=float(linea[30:33])
		dia2=float(linea[49:52])
		ano1=float(linea[25:29])+dia1/366
		ano2=float(linea[44:48])+dia2/366
		esta=linea[1:5].lower()
		if est_day>=ano1 and est_day<=ano2 and est_nam==esta:
			sista=1
	if sista==0 and len(est)==12:
		archivo_upt.write("sh_upd_stnfo -files ../rinex/"+est+"\n")

archivo_info_n.write(cabecera)
for linea in new_solo_rinex:
	archivo_info_n.write(linea)

archivo_info_a.close()
archivo_info_n.close()
archivo_elim.close()
archivo_upt.close()