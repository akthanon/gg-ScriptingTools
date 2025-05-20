import matplotlib.pyplot as plt
import numpy as np
import sys
import os
from statistics import mean
from math import sqrt

carpeta=sys.argv[1]
ano1=int(sys.argv[2])
ano2=int(sys.argv[3])+1
best_est=int(sys.argv[4])
peso=sys.argv[5]

vinte=float(sys.argv[7])
vopc=float(sys.argv[8])
vpor=float(sys.argv[9])
vgraficar=int(float(sys.argv[10]))
formula=int(float(sys.argv[11]))

contenido = os.listdir(carpeta+"/resultados")

est_archi = open (carpeta+"/apriori/list_esta.txt","r")
est_sites=est_archi.readlines()
est_sites=est_sites[0]

ref_archi = open (carpeta+"/apriori/list_referen.txt","r")

ref_sites=ref_archi.readlines()

ref_sites=ref_sites[0]


tot_sites=str(est_sites)+" "+str(ref_sites)
tot_sites=tot_sites.split(" ")

est_archi.close()
ref_archi.close()

est_sites=est_sites.split(" ")
aref_sites=ref_sites.split(" ")

anos=[]
for ano in range(ano1, ano2):
	anos.append(ano)

por_sel=0
sn1_sel=0
sn2_sel=0
mp1_sel=1
mp2_sel=1
opc_sel=600000
dias_por=0.0000001
best_ref=len(aref_sites)
cantidad_minima=float(sys.argv[6])

dias_tot=(ano2-ano1)*366
dias_por=dias_por/100
eliminadas=0
eliminadas_criterio=0
eliminadas_mejores=0
totales_buenas=0
tname=[]
tsn1=[]
tsn2=[]
tpor=[]
tmp1=[]
tmp2=[]
topc=[]
tdia=[]

ttsn1=[]
ttsn2=[]
ttpor=[]
ttmp1=[]
ttmp2=[]
ttopc=[]

opc_sel=140
por_sel=95

def norm(df):
	res=(df - df.min()) / ( df.max() - df.min())
	return res

def norm_alt(df):
	salidas=[]
	for ldif in df:
		temp_res=(float(ldif) - float(min(df))) / ( float(max(df)) - float(min(df)))
		salidas.append(temp_res)
	return np.array(salidas)

def suma(df):
	aax=0
	for ldif in df:
		aax=aax+float(ldif)
	return aax


def norm_alto(df):
	res=(df - float(df.min())) / ( float(df.max()) - float(df.min()))
	return res

def graficar():
	if dias>0:
		x = lfecha
		y = lsn1
		plt.plot(x,y,".",color="blue",label='sn1')
		y = lsn2
		plt.plot(x,y,".",color="purple",label='sn2')
		plt.xlabel('fecha')
		plt.ylabel('snr')
		plt.legend(loc='best')
		plt.xlim(ano1,ano2)
		plt.title(archivo[0:4])
			
		plt.savefig(carpeta+"/graficas/snr_"+archivo[0:4]+".jpg")
		plt.clf()

		y = lesp
		plt.plot(x,y,".",color="green",label='esperado')
		y = lobt
		plt.plot(x,y,".",color="red",label='obtenido')

		plt.xlabel('fecha')
		plt.ylabel('obs')

		plt.legend(loc='best')
		plt.xlim(ano1,ano2)
		plt.title(archivo[0:4])
		plt.savefig(carpeta+"/graficas/obs_"+archivo[0:4]+".jpg")
		plt.clf()

		y = lpor
		plt.plot(x,y,".",color="orange",)
		plt.xlabel('fecha')
		plt.ylabel('por')
		plt.xlim(ano1,ano2)
		plt.title(archivo[0:4])
		plt.savefig(carpeta+"/graficas/por_"+archivo[0:4]+".jpg")
		plt.clf()

		y = lmp1
		plt.plot(x,y,".",color="purple",label='mp1')
		y = lmp2
		plt.plot(x,y,".",color="crimson",label='mp2')
		plt.xlabel('fecha')
		plt.ylabel('multipath')
			
		plt.legend(loc='best')
		plt.title(archivo[0:4])
		plt.xlim(ano1,ano2)
		plt.savefig(carpeta+"/graficas/mpt_"+archivo[0:4]+".jpg")
		plt.clf()

		y = lopc
		plt.plot(x,y,"o",color="black",)
		plt.xlabel('fecha')
		plt.ylabel('opc')
		plt.title(archivo[0:4])
		plt.xlim(ano1,ano2)
		plt.savefig(carpeta+"/graficas/opc_"+archivo[0:4]+".jpg")
		plt.clf()

sta = open(carpeta+"/mejores_estaciones.txt", "a")
ref = open(carpeta+"/mejores_referencia.txt", "a")
eli = open(carpeta+"/elim_esta.sh", "a")
eli.write("#DIAS MALOS"+"\n")



#PURGA DE ARCHIVOS ERRONEOS
for archivo in contenido:
	com = open(carpeta+"/resultados/"+archivo)
	com_size=os.stat(carpeta+"/resultados/"+archivo)
	com_temp=0
	if com_size.st_size>0:
		new = open(carpeta+"/resultados_limpios/"+archivo[8:12]+"_datos.txt", "a")
		com_temp=1

	lfecha=[]
	lsn1=[]
	lsn2=[]
	lesp=[]
	lobt=[]
	lpor=[]
	lmp1=[]
	lmp2=[]
	lopc=[]

	l2fecha=[]
	l2sn1=[]
	l2sn2=[]
	l2esp=[]
	l2obt=[]
	l2por=[]
	l2mp1=[]
	l2mp2=[]
	l2opc=[]

	dias=0
	datos=1

	for fila in com:
		datos=1
		if len(fila)!=136:
#ERROR en un archivo (DATOS ERRONEOS), archivo "+archivo[8:12]+" "+fila[0:8]+" saltado...
			eli.write("rm -r "+fila[0:4]+"/rinex/"+archivo[8:12]+fila[5:8]+"0."+fila[2:4]+"o"+"\n")
			eliminadas=eliminadas+1
			datos=0
		try:			
			fila_fix = fila.split("	")
			fila_fix0 = fila_fix[0]
			fecha_fix=fila_fix0.split(" ")
			fila_fix1 = fila_fix[1]
			fila_fix2 = fila_fix[2]
		except:
			if datos==1:
				eli.write("rm -r "+fila[0:4]+"/rinex/"+archivo[8:12]+fila[5:8]+"0."+fila[2:4]+"o"+"\n")
				eliminadas=eliminadas+1
			datos=0
		try:
			fecha=float(fecha_fix[0])+float(fecha_fix[1])/366
			sn1=float(fila_fix1[34:38])
			sn2=float(fila_fix1[40:44])
			esp=float(fila_fix2[44:50])
			obt=float(fila_fix2[51:57])
			por=float(fila_fix2[58:61])
			mp1=float(fila_fix2[62:67])
			mp2=float(fila_fix2[68:73])
			opc=float(fila_fix2[74:80])
		except:
#ERROR en un archivo (FALTAN DATOS), archivo "+archivo[8:12]+" "+fila[0:8]+" saltado...
			if datos==1:
				eli.write("rm -r "+fila[0:4]+"/rinex/"+archivo[8:12]+fila[5:8]+"0."+fila[2:4]+"o"+"\n")
				eliminadas=eliminadas+1
			datos=0

		if datos==1:
			lfecha.append(fecha)
			lsn1.append(sn1)
			lsn2.append(sn2)
			lesp.append(esp)
			lobt.append(obt)
			lpor.append(por)
			lmp1.append(mp1)
			lmp2.append(mp2)
			lopc.append(opc)

			l2fecha.append(fecha)
			l2sn1.append(sn1)
			l2sn2.append(sn2)
			l2esp.append(esp)
			l2obt.append(obt)
			l2por.append(por)
			l2mp1.append(mp1)
			l2mp2.append(mp2)
			l2opc.append(opc)

			new.write(str(fila[0:8])+","+str(fecha)+","+str(sn1)+","+str(sn2)+","+str(esp)+","+str(obt)+","+str(por)+","+str(mp1)+","+str(mp2)+","+str(opc)+"\n")
			dias=dias+1
#	ESTA NO graficar()
	if dias>1:
		msn1=mean(np.array(lsn1))
		msn2=mean(np.array(lsn2))
		mpor=mean(np.array(lpor))
		mmp1=mean(np.array(lmp1))
		mmp2=mean(np.array(lmp2))
		mopc=mean(np.array(lopc))
		mopc=mean(np.array(lopc))

		tname.append(archivo[8:12])
		tsn1.append(msn1)
		tsn2.append(msn2)
		tpor.append(mpor)
		tmp1.append(mmp1)
		tmp2.append(mmp2)
		topc.append(mopc)

		for i in lsn1:
			ttsn1.append(i)
		for i in lsn2:
			ttsn2.append(i)
		for i in lpor:
			ttpor.append(i)
		for i in lmp1:
			ttmp1.append(i)
		for i in lmp2:
			ttmp2.append(i)
		for i in lopc:
			ttopc.append(i)	

	com.close()
	if com_temp==1:
		new.close()


sn1_sel=mean(ttsn1)-vinte*np.std(ttsn1)
sn2_sel=mean(ttsn2)-vinte*np.std(ttsn2)
mp1_sel=mean(ttmp1)+vinte*np.std(ttmp1)
mp2_sel=mean(ttmp2)+vinte*np.std(ttmp2)
#opc_sel=mean(ttopc)-vinte*np.std(ttopc)

opc_sel=vopc
por_sel=vpor
print("REPORTE DE RESULTADOS:")
print("")
print("SN1	SN2	POR	MP1	MP2	OPC")
print(str(sn1_sel)+"	"+str(sn2_sel)+"	"+str(por_sel)+"	"+str(mp1_sel)+"	"+str(mp2_sel)+"	"+str(opc_sel))

#Criterio de selección
eli.write("#ESTACIONES FUERA DEL CRITERIO DE SELECCION DE ESTACIONES A PROCESAR"+"\n")
contenido_limpio = os.listdir(carpeta+"/resultados_limpios")

aanos=[]
compara_fechas=[]
for ano in anos:
	aanos.append([])

for archivo in contenido_limpio:
	com = open(carpeta+"/resultados_limpios/"+archivo)

	lfecha=[]
	lsn1=[]
	lsn2=[]
	lesp=[]
	lobt=[]
	lpor=[]
	lmp1=[]
	lmp2=[]
	lopc=[]

	dias=0
	for fila in com:
		datos=1
		fila_fix = fila.split(",")
		fecha=float(fila_fix[1])
		sn1=float(fila_fix[2])
		sn2=float(fila_fix[3])
		esp=float(fila_fix[4])
		obt=float(fila_fix[5])
		por=float(fila_fix[6])
		mp1=float(fila_fix[7])
		mp2=float(fila_fix[8])
		opc=float(fila_fix[9])

		if sn1<sn1_sel or sn2<sn2_sel or por<por_sel or mp1>mp1_sel or mp2>mp2_sel or opc<opc_sel:
#CRITERIO DE SELECCION, archivo "+archivo[8:12]+" "+fila[0:8]+" saltado...
			eli.write("rm -r "+fila[0:4]+"/rinex/"+archivo[0:4]+fila[5:8]+"0."+fila[2:4]+"o"+"\n")
			eliminadas_criterio=eliminadas_criterio+1
			datos=0

		if datos==1:
			lfecha.append(fecha)
			lsn1.append(sn1)
			lsn2.append(sn2)
			lesp.append(esp)
			lobt.append(obt)
			lpor.append(por)
			lmp1.append(mp1)
			lmp2.append(mp2)
			lopc.append(opc)
			dias=dias+1
			totales_buenas=totales_buenas+1

	difecha=100000
	lanos=[]
	tdia.append([archivo[0:4],dias])
#	print(archivo[0:4]+"	"+str(dias))
	if dias>1:
		difecha=float((np.array(lfecha)).max()-(np.array(lfecha)).min())
		for ano in anos:
			afecha=[]
			asn1=[]
			asn2=[]
			aesp=[]
			aobt=[]
			apor=[]
			amp1=[]
			amp2=[]
			aopc=[]
			xdias=0
			for z in range(len(lfecha)):
				if ano==int(lfecha[z]):
					afecha.append(lfecha[z])
					asn1.append(lsn1[z])
					asn2.append(lsn2[z])
					aesp.append(lesp[z])
					aobt.append(lobt[z])
					apor.append(lpor[z])
					amp1.append(lmp1[z])
					amp2.append(lmp2[z])
					aopc.append(lopc[z])
					xdias=xdias+1
			if len(np.array(afecha)) >0 and (str(archivo[0:4]) in est_sites):	
				lanos.append([str(archivo[0:4]),ano,mean(asn1),mean(asn2),mean(aesp),mean(aobt),mean(apor),mean(amp1),mean(amp2),mean(aopc),xdias,1])
#				print(str(archivo[0:4])+"	"+str(mean(afecha)))
			elif not(len(np.array(afecha)) >0) and (str(archivo[0:4]) in est_sites):
#				lanos.append([str(archivo[0:4]),"NA","NA","NA","NA","NA","NA","NA","NA","NA"])
				lanos.append([str(archivo[0:4]),ano,max(lsn1),max(lsn2),max(lesp),max(lobt),max(lpor),max(lmp1),max(lmp2),max(lopc),0,0])
#		print(archivo[0:4]+"	"+str(xdias))
		if len(lanos)>0:
			for ano in range(len(anos)):
				if anos[ano]==int(lanos[ano][1]):
					aanos[ano].append(lanos[ano])
	compara_temp=[]
	for compara in lfecha:
		compara_temp.append([archivo[0:4],compara])	
	compara_fechas.append(compara_temp)

	if vgraficar==1:
		graficar()
	com.close()
aanos=np.array(aanos)
xanos=[]
for ano in range(len(anos)):
	xanos_temp=[]
	tempi=aanos[ano]
	tempi=np.array(tempi)
	xnam=tempi[:,0]
	xano=tempi[:,1]
	xsn1=np.array(tempi[:,2])
	xsn1=norm_alt(xsn1)
	xsn2=norm_alt(np.array(tempi[:,3]))
	xpor=norm_alt(np.array(tempi[:,6]))
	xmp1=norm_alt(np.array(tempi[:,7]))
	xmp2=norm_alt(np.array(tempi[:,8]))
	xopc=norm_alt(np.array(tempi[:,9]))
	xdia=tempi[:,10]
	xpunt=[]
	for i in range(len(xnam)):
		peso=0.5
		xpunt_t=(float(xdia[i])/366)*(peso+1/(sqrt(float(xsn1[i])**2+float(xsn2[i])**2+(1-float(xpor[i]))**2+float(xmp1[i])**2+float(xmp2[i])**2+(1-float(xopc[i]))**2)**2))
		xpunt.append(xpunt_t)
	xanos_temp.append([xnam,xano,xsn1,xsn2,xpor,xmp1,xmp2,xopc,xdia,xpunt])
	xanos.append([xnam,xano,xsn1,xsn2,xpor,xmp1,xmp2,xopc,xdia,xpunt])	
xanos=np.array(xanos)

xord=[]
for ano in range(len(anos)):
	xord_temp = xanos[ano]
	yord_temp = []
	for i in range(len(xord_temp[0])):
		yord_temp.append([xord_temp[0,i],float(xord_temp[9,i]),xord_temp[8,i]])	
	xord.append(yord_temp)
xord=np.array(xord)
xxord=[]
for linea in range(len(xord[0])):
	axnam=xord[:,linea,0]
	axnam=axnam[0]
	xxord.append([axnam,suma(xord[:,linea,1])])

xxord = sorted(xxord, reverse=True,key=lambda res: res[1])
xxord=np.array(xxord)
xxord_list=xxord[:,0]
xapend=[]

for ano in range(len(anos)):
	lon=0
	for linea in range(len(xord[ano])):
		if float(xord[ano,linea,2])>0:
			lon=lon+1
	con=0
#	con_bes=0
	yapend=[]
	if lon>best_est:
		for xlinea in xxord_list:	
			for linea in range(len(xord[ano])):
				xorname=xord[ano,linea,0]
				xordata=float(xord[ano,linea,1])
				if xorname==xlinea and xordata>0:
#				if xorname==xlinea and xordata>0 and con_bes<best_est:
					yapend.append(xorname)
#					con_bes=con_bes+1
	else:
		for xlinea in xxord_list:	
			for linea in range(len(xord[ano])):
				xorname=xord[ano,linea,0]
				xordata=float(xord[ano,linea,1])
				if xorname==xlinea and xordata>0:
					yapend.append(xorname)

	xapend.append(yapend)


compara_fechas=np.array(compara_fechas,dtype=object)

xapend2=[[]]
for i in range(len(xapend)):
	temporale=[]
	xapend_tem=xapend[i]
	for j in range(len(xapend_tem)):
		temporale.append(xapend_tem[j])
	xapend2.append(temporale)
#xapend2=np.array(xapend.copy())
xapend3=[]
vacio=[]


for lf in range(len(compara_fechas)):
	lanoss=compara_fechas[lf]
	lanoss_a=[]
	lanoss_b=[]
	lanoss_n="xxxnaxxx"
	for lg in lanoss:
		alg=int(float(lg[1]))
		lanoss_a.append(lg[1])
		lanoss_n=lg[0]

	
	for anal in range(len(anos)):
		ano=anos[anal]
		lanoss_c=[]
		for xla in lanoss_a:
			if int(xla)==ano:
				lanoss_c.append(xla)
		if len(lanoss_c)>0 and len(xapend2[anal])>0:
			dif=max(lanoss_c)-min(lanoss_c)
			asd=0
			for f in range(len(xapend2[anal])):
					if lanoss_n==xapend2[anal][f]:
						asd=f
			if dif>0:
				lanoss_b.append([lanoss_n,min(lanoss_c),max(lanoss_c),ano])
				xapend2[anal][asd]=lanoss_n
			else:
				del xapend2[anal][asd]


	if len(lanoss_b)>0:
		vacio.append(lanoss_b)

#print(xapend2)
#print(vacio)
vacio=np.array(vacio,dtype=object)
xapend=np.array(xapend,dtype=object)


void_n=[]
void_min=[]
void_max=[]
for ano in range(len(anos)):
	for ico in vacio:
		for ifi in ico:
			if anos[ano]==ifi[3]:
				if ifi[0] in xapend[ano]:
					void_n.append(ifi[0])
					void_min.append(ifi[1])
					void_max.append(ifi[2])

eli.write("#ESTACIONES ELIMINADAS POR NO SER LAS MEJORES"+"\n")
est_sites_datos=[]
vacio=[void_n,void_min,void_max]
for estacion in est_sites:
	minimo=10000000000
	maximo=0
	sista=0
	for lin in range(len(void_n)):
		if void_n[lin]==estacion:
			sista=1
			if void_min[lin]<minimo:
				minimo=float(void_min[lin])
			if void_max[lin]>maximo:
				maximo=float(void_max[lin])
	
	if (maximo-minimo)>cantidad_minima and sista==1:
		est_sites_datos.append(estacion)
eanos=[]

for ano in anos:
	eanos.append(0)
for ano in range(len(anos)):
	con_bes=0
	for lni in xapend[ano]:
		if not (lni in est_sites_datos):
			eli.write("rm -r "+str(anos[ano])+"/rinex/"+lni+"*o""\n")
			eliminadas_mejores=eliminadas_mejores+1
			eanos[ano]=eanos[ano]+1
		tama=len(xapend[ano])-eanos[ano]
		if con_bes>=best_est and tama>=best_est:
			eli.write("rm -r "+str(anos[ano])+"/rinex/"+lni+"*o""\n")
			eliminadas_mejores=eliminadas_mejores+1
			eanos[ano]=eanos[ano]+1
		else:
			con_bes=con_bes+1

canos=0
for esta in est_sites_datos:
	encontrada=0
	for ano in range(len(anos)):
		xalin=xapend[ano]
		xalin=xalin[0:int(len(xalin)-eanos[ano])]
		if esta in xalin and encontrada==0:
			encontrada=1
			canos=canos+1

nsn1=norm(np.array(tsn1))
nsn2=norm(np.array(tsn2))
npor=1-norm(np.array(tpor))
nmp1=norm(np.array(tmp1))
nmp2=norm(np.array(tmp2))
nopc=1-norm(np.array(topc))

fres=[]

for i in range(len(tname)):
	asd_dia=0
	for ldia in tdia:
		if tname[i]==ldia[0]:
			asd_dia=float(ldia[1])
	tempo=sqrt(nsn1[i]**2+nsn2[i]**2+npor[i]**2+nmp1[i]**2+nmp2[i]**2+nopc[i]**2)*float(asd_dia/dias_tot)
	tempo2=str(tname[i])+", "+str(tempo)
	tempo2=tempo2.split(",")
	fres.append(tempo2)


eres = sorted(fres, reverse=True,key=lambda res: res[1])
fres = sorted(fres, reverse=True,key=lambda res: res[1])
con_ref=0
con_est=0

eli.write("#ESTACIONES DE REFERENCIA NO ENCONTRADAS"+"\n")

for linea in fres:
	if linea[0] in ref_sites:
		con_ref=con_ref+1
		if con_ref>best_ref:
			eli.write("rm -r "+"*/rinex/"+str(linea[0])+"*o""\n")
		for i in linea:
			ref.write(str(i))
		ref.write("\n")
	else:
		con_est=con_est+1
		for i in linea:
			sta.write(str(i))
		sta.write("\n")

eli.write("#ESTACIONES NO ENCONTRADAS(BORRAR TODAS POR SI LAS DUDAS)"+"\n")
for linea in tot_sites:
	if not(linea in tname):
		eli.write("rm -r "+"*/rinex/"+str(linea)+"*o"+"\n")

print("")
print(str(eliminadas)+": datos eliminados por archivos erroneos")
print(str(eliminadas_criterio)+": datos bajo el criterio de seleccion")
print(str(totales_buenas)+": datos buenos en total")
print(str(eliminadas_criterio*100/(totales_buenas+eliminadas_criterio))[:5]+"%: porcentaje de datos eliminados bajo criterio de seleccion")
print(str(eliminadas_mejores)+": estaciones eliminadas por no ser las mejores\n")
print(str(canos)+": estaciones a procesar para todos los años")
print("de los cuales se procesaron:\n")
for ano in range(len(anos)):
	dif=str(float(len(xapend[ano])-float(eanos[ano])))
	print(dif+" de "+str(len(xapend[ano]))+": estaciones a procesar del año "+str(anos[ano]))
	estac=xapend[ano]
	for es in range(0,len(xapend[ano])-int(float(eanos[ano])),1):
		es=estac[es]
		print(es, end=" ")
	print("\n")

sta.close()
ref.close()
eli.close()



