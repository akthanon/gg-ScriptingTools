from os import listdir
import os
import sys
import numpy as np

anos=[]
wrms=[]
carpeta=sys.argv[1]
confix=0

archivo = open (carpeta+"/lista_wrms.txt","w")
archivo2 = open (carpeta+"/lista_cord.txt","w")

ref_sites = "ABMF ABPO ADE1 AIRA ALBH ALGO ALIC ALRT AMC2 ANKR AOML AREQ AREV ARTU ASC1 ASPA AUCK BADG BAHR BAKE BAN2 BARH BHR1 BHR2 BILI BJCO BJFS BOGT BOR1 BRAZ BREW BRFT BRMU BRST BRUS BUCU BUE2 CAGL CAGZ CAS1 CCJM CEDU CFAG CHAT CHPI CHTI CHUM CHUR CIC1 CKIS CNMR COCO COYQ CRAO CRO1 DAEJ DARW DAV1 DGAR DGAV DRAG DRAO DUBO DUBR DUM1 EISL EPRT FAA1 FAIR FALK FLIN FORT FUNC GALA GLPS GLSV GMAS GMSD GODE GODZ GOL2 GOLD GOUG GRAS GRAZ GUAM GUAO GUAT GUUG HARB HERS HERT HLFX HNLC HOB2 HOFN HOLB HOLM HRAO HYDE IISC INVK IRKJ IRKM IRKT ISPA ISTA JAB1 JOZ2 JOZE JPLM KARR KAT1 KELY KERG KGNI KHAJ KIRI KIRU KIT3 KOKB KOKV KOSG KOUC KOUR KUNM KWJ1 LAE1 LAUT LHAS LHAZ LMMF LPAL LPGS LROC MAC1 MAL2 MALD MALI MANA MAS1 MAT1 MATE MAUI MAW1 MBAR MCIL MCM4 MDO1 MDVJ MDVO MEDI METS METZ MKEA MOBS MONP MORP MQZG MTKA NAIN NAMA NANO NAUR NICO NIUM NKLG NLIB NNOR NOT1 NOUM NRC1 NRIL NRMD NURK NVSK NYA1 NYAL OHI2 OHI3 OHIG ONSA OSN1 OUS2 PALM PARC PDEL PERT PETP PIE1 PIMO POHN POL2 POLV POTS PRDS PRE1 QAQ1 QIKI QUI2 QUIN RABT RAMO RBAY RCMN RECF RESO REUN RIGA RIO2 RIOG SALU SANT SAVO SCH2 SCOR SCUB SELE SFER SHAO SIMO SOFI SSIA STHL STJO SUTH SUTM SUWN SYDN SYOG TAEJ TAH1 TASH TCMS TEHN THTI THU1 THU3 TID1 TIDB TIXI TLSE TNML TOW2 TRAB TRO1 TROM TSKB TUVA TWTF UFPR ULAB UNBJ UNSA URUM USN3 USNO UZHL VACS VESL VILL VNDP WES2 WHIT WILL WIND WSRT WTZR WUHN XMIS YAKT YAR1 YAR2 YARR YEBE YELL YIBL ZAMB ZECK ZIMJ ZIMM"
estaciones = ref_sites.split(" ")

wrms = open (carpeta+"/wrms/wrms.txt")
cord = open (carpeta+"/apriori/itrf14.apr")
prom = open (carpeta+"/apriori/cord_est.txt")

archivo.write("EST, N, E, U"+"\n")

for linea_wrms in wrms:
	for estacion in estaciones:
		if estacion==linea_wrms[0:4]:
			temp=linea_wrms.split("	")
			for i in range(len(temp)-1):
				archivo.write(str(temp[i])+",")
			archivo.write(temp[-1])

xarray=[]
yarray=[]
zarray=[]

xmean=0
ymean=0
zmean=0

for linea_prom in prom:
	temp=linea_prom.split(" ")
	xarray.append(float(temp[1]))
	yarray.append(float(temp[2]))
	zarray.append(float(temp[3]))


xmean=str(np.mean(np.array(xarray)))
ymean=str(np.mean(np.array(yarray)))
zmean=str(np.mean(np.array(zarray)))


archivo2.write("EST, X, Y, Z"+"\n")
archivo2.write("XXXX,"+xmean+","+ymean+","+zmean+"\n")
temp="XXXXXXXXXXXXXXXXXXX"
for linea_cord in cord:
	for estacion in estaciones:
		if estacion==linea_cord[1:5] and temp!=estacion:
			archivo2.write(str(linea_cord[1:5])+","+str(float(linea_cord[10:24]))+","+str(float(linea_cord[25:39]))+","+str(float(linea_cord[40:54]))+"\n")
	temp=linea_cord[1:5]
		
archivo.close()
wrms.close()

archivo2.close()
cord.close()
prom.close()
