import sys
import os
cabecera="# Station.info written by MSTINF user deon             on 2022-07-21  05:04\n* Reference file : station.info\n*\n*\n*SITE  Station Name      Session Start      Session Stop       Ant Ht   HtCod  Ant N    Ant E    Receiver Type         Vers                  SwVer  Receiver SN           Antenna Type     Dome   Antenna SN           \n"

carpeta=sys.argv[1]
listado_rinex = os.listdir(carpeta+"/rinex")
archivo_info_a = open (carpeta+"/tables/INFO_STATION","r")
archivo_info=archivo_info_a.readlines()
archivo_info_n = open (carpeta+"/tables/INFO_STATION","w")
archivo_info_e = open (carpeta+"/tables/station.info","r")
station_info = archivo_info_e.readlines()
archivo_info_f = open (carpeta+"/tables/station.info","w")

archivo_info_n.write(cabecera)
archivo_info_f.write(cabecera)

for nlinea in range(1,len(station_info),1):
	if station_info[nlinea]!=station_info[nlinea-1]:
		linea=station_info[nlinea]
		if len(linea)>10 and linea[0]!="*" and linea[0]!="#":
			archivo_info_f.write(station_info[nlinea])


for nlinea in range(1,len(archivo_info),1):
	if archivo_info[nlinea]!=archivo_info[nlinea-1]:
		linea=archivo_info[nlinea]
		if len(linea)>10 and linea[0]!="*" and linea[0]!="#":
			archivo_info_n.write(archivo_info[nlinea])


archivo_info_a.close()
archivo_info_n.close()
archivo_info_e.close()
archivo_info_f.close()