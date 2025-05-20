from os import listdir
import os
import sys
import numpy as np
from math import sqrt

anos=[]
wrms=[]
carpeta=sys.argv[1]
ano1=int(sys.argv[2])
ano2=int(sys.argv[3])+1

archivo = open (carpeta+"/reporte_resultados_sin_calidad.txt","w")

ref_sites = "ABMF ABPO ADE1 AIRA ALBH ALGO ALIC ALRT AMC2 ANKR AOML AREQ AREV ARTU ASC1 ASPA AUCK BADG BAHR BAKE BAN2 BARH BHR1 BHR2 BILI BJCO BJFS BOGT BOR1 BRAZ BREW BRFT BRMU BRST BRUS BUCU BUE2 CAGL CAGZ CAS1 CCJM CEDU CFAG CHAT CHPI CHTI CHUM CHUR CIC1 CKIS CNMR COCO COYQ CRAO CRO1 DAEJ DARW DAV1 DGAR DGAV DRAG DRAO DUBO DUBR DUM1 EISL EPRT FAA1 FAIR FALK FLIN FORT FUNC GALA GLPS GLSV GMAS GMSD GODE GODZ GOL2 GOLD GOUG GRAS GRAZ GUAM GUAO GUAT GUUG HARB HERS HERT HLFX HNLC HOB2 HOFN HOLB HOLM HRAO HYDE IISC INVK IRKJ IRKM IRKT ISPA ISTA JAB1 JOZ2 JOZE JPLM KARR KAT1 KELY KERG KGNI KHAJ KIRI KIRU KIT3 KOKB KOKV KOSG KOUC KOUR KUNM KWJ1 LAE1 LAUT LHAS LHAZ LMMF LPAL LPGS LROC MAC1 MAL2 MALD MALI MANA MAS1 MAT1 MATE MAUI MAW1 MBAR MCIL MCM4 MDO1 MDVJ MDVO MEDI METS METZ MKEA MOBS MONP MORP MQZG MTKA NAIN NAMA NANO NAUR NICO NIUM NKLG NLIB NNOR NOT1 NOUM NRC1 NRIL NRMD NURK NVSK NYA1 NYAL OHI2 OHI3 OHIG ONSA OSN1 OUS2 PALM PARC PDEL PERT PETP PIE1 PIMO POHN POL2 POLV POTS PRDS PRE1 QAQ1 QIKI QUI2 QUIN RABT RAMO RBAY RCMN RECF RESO REUN RIGA RIO2 RIOG SALU SANT SAVO SCH2 SCOR SCUB SELE SFER SHAO SIMO SOFI SSIA STHL STJO SUTH SUTM SUWN SYDN SYOG TAEJ TAH1 TASH TCMS TEHN THTI THU1 THU3 TID1 TIDB TIXI TLSE TNML TOW2 TRAB TRO1 TROM TSKB TUVA TWTF UFPR ULAB UNBJ UNSA URUM USN3 USNO UZHL VACS VESL VILL VNDP WES2 WHIT WILL WIND WSRT WTZR WUHN XMIS YAKT YAR1 YAR2 YARR YEBE YELL YIBL ZAMB ZECK ZIMJ ZIMM"
estaciones = ref_sites.split(" ")

cord_fix = open (carpeta+"/lista_cord.txt")
wrms_fix = open (carpeta+"/lista_wrms.txt")
brks_fix = open (carpeta+"/lista_breaks.txt")
dtos_fix = open (carpeta+"/lista_datos.txt")

cord_base= [0,0,0]

wrms = []
cord = []
brks = []
dtos = []
repo = []


confix=0
for i in cord_fix:
	if confix==1:
		tempo=i.split(",")
		cord_base[0]=float(tempo[1])
		cord_base[1]=float(tempo[2])
		cord_base[2]=float(tempo[3])
	if confix>0:
		cord.append(i.split(","))
	confix=confix+1

confix=0
for i in wrms_fix:
	if confix>0:
		wrms.append(i.split(","))
	confix=confix+1

confix=0
for i in brks_fix:
	if confix>0:
		brks.append(i.split(","))
	confix=confix+1

confix=0
for i in dtos_fix:
	if confix>0:
		dtos.append(i.split(","))
	confix=confix+1

confix=0
for i in dtos_fix:
	if confix>0:
		dtos.append(i.split(","))
	confix=confix+1


cord_x=[]
cord_y=[]
cord_z=[]
esta_n=[]

wrms_e=[]
wrms_n=[]
wrms_u=[]

anos=[]
brks_m=[]
dtos_m=[]

for i in range(ano1,ano2,1):
	anos.append(i)
dias_tot=(ano2-ano1)*366

for estacion in estaciones:
	check=0
	brks_x=[]
	dtos_x=[]
	for f_cord in cord:
		if estacion==f_cord[0] and check==0:
			esta_n.append(estacion)
			cord_x.append(float(f_cord[1]))
			cord_y.append(float(f_cord[2]))
			cord_z.append(float(f_cord[3]))
			check=1

	for f_wrms in wrms:
		if estacion==f_wrms[0] and check==1:
			wrms_e.append(float(f_wrms[1]))
			wrms_n.append(float(f_wrms[2]))
			wrms_u.append(float(f_wrms[3]))
			check=2

	for f_brks in brks:
		if estacion==f_brks[0] and check==2:
			for ano in range(len(anos)):
				brks_x.append(float(f_brks[ano+1]))
			check=3
	if check==3:
		brks_m.append(brks_x)

	for f_dtos in dtos:
		if estacion==f_dtos[0] and check==3:
			for ano in range(len(anos)):
				dtos_x.append(float(f_dtos[ano+1]))
			check=4
	if check==4:
		dtos_m.append(dtos_x)

	if check<4:
		if check>=1:
			delete(esta_n[-1])
			delete(cord_x[-1])
			delete(cord_y[-1])
			delete(cord_z[-1])
		if check>=2:
			delete(wrms_e[-1])
			delete(wrms_n[-1])
			delete(wrms_u[-1])
		if check==3:
			delete(brks_m[-1])

def norm_m(mf):
	tem=[]
	for ano in range(len(anos)):
		df=mf[:,ano]
		res=(df - df.min()) / ( df.max() - df.min())
		tem.append(res)
	tem=np.array(tem)
	return (tem)

def suma(mf):
	tem=[]
	for i in range(len(esta_n)):
		df=mf[i,:]
		res=np.sum(df)
		tem.append(res)
	tem=np.array(tem)
	return (tem)

def norm(df):
	res=(df - df.min()) / ( df.max() - df.min())
	return (res)

def dist(xx,yy,zz):
	dista=[]
	bx=cord_base[0]
	by=cord_base[1]
	bz=cord_base[2]
	for i in range(len(esta_n)):
		difx=bx-xx[i]
		dify=by-yy[i]
		difz=bz-zz[i]
		dista.append(np.sqrt(np.square(difx)+np.square(dify)+np.square(difz)))
	dista=np.array(dista)
	return (dista)

def drms(xx,yy,zz):
	dista=[]
	for i in range(len(esta_n)):
		difx=xx[i]
		dify=yy[i]
		difz=0.5*zz[i]
		dista.append(np.sqrt(np.square(difx)+np.square(dify)+0.1*np.square(difz)))
	dista=np.array(dista)
	return (dista)

def final_dist(aa,bb,cc,dd):
	dista=[]
	for i in range(len(esta_n)):
		difa=aa[i]
		difb=bb[i]
		difc=cc[i]
		difd=dd[i]
		dista.append(np.sqrt(np.square(difa)+np.square(difb)+np.square(difc))*difd/dias_tot)
	dista=np.array(dista)
	return (dista)

cord_x=np.array(cord_x)
cord_y=np.array(cord_y)
cord_z=np.array(cord_z)

disn=dist(cord_x,cord_y,cord_z)
norm_dist=norm(disn)

wrms_e=np.array(wrms_e)
wrms_n=np.array(wrms_n)
wrms_u=np.array(wrms_u)

rmsn=drms(wrms_e,wrms_n,wrms_u)
norm_wrms=norm(rmsn)

norm_brks=norm(suma(np.array(brks_m)))
norm_dtos=norm(suma(np.array(dtos_m)))
suma_dtos=suma(np.array(dtos_m))

peso_brks=1
peso_dist=2
peso_wrms=1
peso_dtos=1
peso_repo=1

norm_brks=(1-norm_brks)*peso_brks
norm_dist=(1-norm_dist)*peso_dist
norm_wrms=(1-norm_wrms)*peso_wrms
norm_dtos=norm_dtos*peso_dtos

norm_repo=[]

for i in range(len(esta_n)):
	for j in range(len(repo)):
		estacion_x=repo[j]
		if esta_n[i]==estacion_x[0]:
			norm_repo.append(estacion_x[1])

final_n=final_dist(norm_brks,norm_dist,norm_wrms,suma_dtos)

result=[]
for i in range(len(esta_n)):
	result.append([esta_n[i].lower(),final_n[i],norm_brks[i],norm_dist[i],norm_wrms[i], suma_dtos[i]])

result = sorted(result, reverse=True,key=lambda res: res[1])

archivo.write("MEJORES TOTALES SIN CALIDADES\n")
for i in result:
	for j in range(0,len(i)-1,1):
		archivo.write(str(i[j])+"	")
	archivo.write(str(i[len(i)-1])+"\n")


archivo.close()
wrms_fix.close()
cord_fix.close()
brks_fix.close()
dtos_fix.close()
