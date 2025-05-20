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

archivo_info_n.write(cabecera)
for linea in archivo_info:
	if len(linea)>10 and linea[0]!="*" and linea[0]!="#":
		archivo_info_n.write(linea)
archivo_info_a.close()
for linea in station_info:
	linea_temp=linea.split(" ")
	if len(linea)>10 and linea[0]!="*" and linea[0]!="#":
		if "mstinf:" in linea_temp:
			archivo_info_n.write(str(linea[:-30]+"\n"))

archivo_info_a.close()
archivo_info_n.close()
archivo_info_e.close()
