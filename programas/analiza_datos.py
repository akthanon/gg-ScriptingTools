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
best_ref=int(sys.argv[4])
formula=int(sys.argv[5])

archivo = open (carpeta+"/reporte_resultados.txt","w")
archivo2 = open (carpeta+"/ESTACIONES_DE_REFERENCIA.txt","w")
eli = open(carpeta+"/elim_refe.sh", "w")

ref_archi = open (carpeta+"/apriori/list_referen.txt","r")
ref_sites=ref_archi.readlines()
ref_sites=ref_sites[0]
ref_sites=ref_sites.split(" ")
ref_archi.close()
for i in range(len(ref_sites)):
	ref_sites[i]=ref_sites[i].upper()
estaciones=ref_sites


cord_fix = open (carpeta+"/lista_cord.txt")
wrms_fix = open (carpeta+"/lista_wrms.txt")
brks_fix = open (carpeta+"/lista_breaks.txt")
dtos_fix = open (carpeta+"/lista_datos.txt")
repo_fix = open (carpeta+"/resultados_calidad/mejores_referencia.txt")
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

for i in repo_fix:
	temo=i.split(" ")
	name=temo[0]
	repo.append([name.upper(),float(temo[1])])

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

def final_dist(aa,bb,cc,dd,ee):
	dista=[]
	for i in range(len(esta_n)):
		difa=aa[i]
		difb=bb[i]
		difc=cc[i]
		difd=dd[i]
		dife=ee[i]
#		print(str(difa)+"	"+str(difb)+"	"+str(difc)+"	"+str(dife)+"	"+str(difd))
		if formula==1:
			dista.append(difa*difb*difc*dife*difd/dias_tot)
		elif formula==2:
			dista.append(np.sqrt(np.square(difa)+np.square(difb)+np.square(difc)+np.square(dife))*difd/dias_tot)
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
peso_dist=1
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

final_n=final_dist(norm_brks,norm_dist,norm_wrms,suma_dtos,norm_repo)

result=[]
for i in range(len(esta_n)):
	result.append([esta_n[i].lower(),final_n[i],norm_brks[i],norm_dist[i],norm_wrms[i], suma_dtos[i], norm_repo[i]])

result = sorted(result, reverse=True,key=lambda res: res[1])

archivo.write("MEJORES ESTACIONES EN GENERAL\n")
archivo2.write("MEJORES ESTACIONES EN GENERAL\n")
conta_referen=0
for i in result:
	archivo2.write(str(i[0])+" ")
	for j in range(0,len(i)-1,1):
		archivo.write(str(i[j])+"	")
	archivo.write(str(i[len(i)-1])+"\n")
	if conta_referen>=best_ref:
		for ano in anos:
			eli.write("rm -r "+str(ano)+"/rinex/"+str(i[0])+"*o""\n")
	conta_referen=conta_referen+1

result = sorted(result, reverse=True,key=lambda res: res[2])

archivo.write("\nMEJORES BREAKS\n")
archivo2.write("\n\nMEJORES BREAKS\n")
for i in result:
	archivo2.write(str(i[0])+" ")
	for j in range(0,len(i)-1,1):
		archivo.write(str(i[j])+"	")
	archivo.write(str(i[len(i)-1])+"\n")

result = sorted(result, reverse=True,key=lambda res: res[3])
archivo.write("\nMEJORES DISTANCIAS\n")
archivo2.write("\n\nMEJORES DISTANCIAS\n")
for i in result:
	archivo2.write(str(i[0])+" ")
	for j in range(0,len(i)-1,1):
		archivo.write(str(i[j])+"	")
	archivo.write(str(i[len(i)-1])+"\n")

result = sorted(result, reverse=True,key=lambda res: res[4])
archivo.write("\nMEJORES WRMS\n")
archivo2.write("\n\nMEJORES WRMS\n")
for i in result:
	archivo2.write(str(i[0])+" ")
	for j in range(0,len(i)-1,1):
		archivo.write(str(i[j])+"	")
	archivo.write(str(i[len(i)-1])+"\n")

result = sorted(result, reverse=True,key=lambda res: res[5])
archivo.write("\nMEJORES DIAS DE DATOS\n")
archivo2.write("\n\nMEJORES DIAS DE DATOS\n")
for i in result:
	archivo2.write(str(i[0])+" ")
	for j in range(0,len(i)-1,1):
		archivo.write(str(i[j])+"	")
	archivo.write(str(i[len(i)-1])+"\n")

result = sorted(result, reverse=True,key=lambda res: res[6])
archivo.write("\nMEJORES CALIDADES\n")
archivo2.write("\n\nMEJORES CALIDADES\n")
for i in result:
	archivo2.write(str(i[0])+" ")
	for j in range(0,len(i)-1,1):
		archivo.write(str(i[j])+"	")
	archivo.write(str(i[len(i)-1])+"\n")

archivo.close()
archivo2.close()
wrms_fix.close()
repo_fix.close()
cord_fix.close()
brks_fix.close()
dtos_fix.close()
eli.close()
