from os import listdir
import os
import sys

anos=[]
breaks=[]
carpeta=sys.argv[1]
ano1=int(sys.argv[2])
ano2=int(sys.argv[3])+1
confix=0

archivo = open (carpeta+"/lista_breaks.txt","w")
estaciones = "ABMF ABPO ADE1 AIRA ALBH ALGO ALIC ALRT AMC2 ANKR AOML AREQ AREV ARTU ASC1 ASPA AUCK BADG BAHR BAKE BAN2 BARH BHR1 BHR2 BILI BJCO BJFS BOGT BOR1 BRAZ BREW BRFT BRMU BRST BRUS BUCU BUE2 CAGL CAGZ CAS1 CCJM CEDU CFAG CHAT CHPI CHTI CHUM CHUR CIC1 CKIS CNMR COCO COYQ CRAO CRO1 DAEJ DARW DAV1 DGAR DGAV DRAG DRAO DUBO DUBR DUM1 EISL EPRT FAA1 FAIR FALK FLIN FORT FUNC GALA GLPS GLSV GMAS GMSD GODE GODZ GOL2 GOLD GOUG GRAS GRAZ GUAM GUAO GUAT GUUG HARB HERS HERT HLFX HNLC HOB2 HOFN HOLB HOLM HRAO HYDE IISC INVK IRKJ IRKM IRKT ISPA ISTA JAB1 JOZ2 JOZE JPLM KARR KAT1 KELY KERG KGNI KHAJ KIRI KIRU KIT3 KOKB KOKV KOSG KOUC KOUR KUNM KWJ1 LAE1 LAUT LHAS LHAZ LMMF LPAL LPGS LROC MAC1 MAL2 MALD MALI MANA MAS1 MAT1 MATE MAUI MAW1 MBAR MCIL MCM4 MDO1 MDVJ MDVO MEDI METS METZ MKEA MOBS MONP MORP MQZG MTKA NAIN NAMA NANO NAUR NICO NIUM NKLG NLIB NNOR NOT1 NOUM NRC1 NRIL NRMD NURK NVSK NYA1 NYAL OHI2 OHI3 OHIG ONSA OSN1 OUS2 PALM PARC PDEL PERT PETP PIE1 PIMO POHN POL2 POLV POTS PRDS PRE1 QAQ1 QIKI QUI2 QUIN RABT RAMO RBAY RCMN RECF RESO REUN RIGA RIO2 RIOG SALU SANT SAVO SCH2 SCOR SCUB SELE SFER SHAO SIMO SOFI SSIA STHL STJO SUTH SUTM SUWN SYDN SYOG TAEJ TAH1 TASH TCMS TEHN THTI THU1 THU3 TID1 TIDB TIXI TLSE TNML TOW2 TRAB TRO1 TROM TSKB TUVA TWTF UFPR ULAB UNBJ UNSA URUM USN3 USNO UZHL VACS VESL VILL VNDP WES2 WHIT WILL WIND WSRT WTZR WUHN XMIS YAKT YAR1 YAR2 YARR YEBE YELL YIBL ZAMB ZECK ZIMJ ZIMM"
estaciones = estaciones.split(" ")

breaks_fix = open (carpeta+"/breaks/"+"tabla_breaks.txt")
for i in breaks_fix:
	if confix>4:
		breaks.append(i)
	confix=confix+1


#breaks_fix=breaks.readlines()
encontrada=0
cuenta=0
cuentanos=0
conta=0

archivo.write("EST,")
for i in range(ano1,ano2,1):
	anos.append(str(i))
	archivo.write(str(i)+",")

archivo.write("TOTAL"+"\n")

for estacion in estaciones:
	archivo.write(str(estacion)+",")
	cuentanos=0
	for ano in anos:
		cuenta=0
		for linea_break in breaks:
			if estacion==linea_break[0:4] and ano==linea_break[5:9]:
				cuenta=cuenta+1

		archivo.write(str(cuenta)+",")
		cuentanos=cuentanos+cuenta
	archivo.write(str(cuentanos)+"\n")
	conta=conta+1
#	print(str(conta)+"/"+str(len(estaciones))) 
		
archivo.close()
breaks_fix.close()
