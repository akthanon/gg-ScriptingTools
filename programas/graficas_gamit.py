import matplotlib.pyplot as plt
import numpy as np
import sys
import os
from statistics import mean
from math import sqrt

carpeta=sys.argv[1]
ano1=int(sys.argv[2])
ano2=int(sys.argv[3])+1

archivo = open (carpeta+"/resultados_gamit/reporte_resultados.txt","w")

glo_a = open(carpeta+"/resultados_gamit/globk_org.txt", "r")
nrm_a = open(carpeta+"/resultados_gamit/NRMS.txt", "r")
nsu_a = open(carpeta+"/resultados_gamit/NSU.txt", "r")
paw_a = open(carpeta+"/resultados_gamit/PAW.txt", "r")
rms_a = open(carpeta+"/resultados_gamit/RMS.txt", "r")

glo=glo_a.readlines()
nrm=nrm_a.readlines()
nsu=nsu_a.readlines()
paw=paw_a.readlines()
rms=rms_a.readlines()


#*****************INICIALIZAR LOS VECTORES***********************

#*******************CODIGO PARA GLOBK_ORG**********************
glo_day=[]
glo_pre=[]
glo_pos=[]

for linea in range(1,len(glo),1):
	temp=glo[linea][0:-1].split("	")
	if int(temp[0])>=ano1 and int(temp[0])<ano2:
		glo_day.append(float(temp[2]))
		glo_pre.append(float(temp[4]))
		glo_pos.append(float(temp[5]))

glo_day = np.array(glo_day)
glo_pre = np.array(glo_pre)
glo_pos = np.array(glo_pos)

x = glo_day
y = glo_pre
plt.plot(x,y,".",color="purple",label='pre rms')
plt.xlabel('fecha')
plt.ylabel('rms')
plt.xlim(ano1,ano2)
plt.ylim(-0.01,0.2)
plt.title("PRE RMS")
plt.savefig(carpeta+"/graficas_gamit/globk_org_pre.jpg")
plt.clf()

y = glo_pos
plt.plot(x,y,".",color="blue",label='pos rms')
plt.xlabel('fecha')
plt.ylabel('rms')
plt.xlim(ano1,ano2)
plt.ylim(-0.0025,0.01)
plt.title("POST RMS")
plt.savefig(carpeta+"/graficas_gamit/globk_org_pos.jpg")
plt.clf()

archivo.write("RESULTADOS GLOBK_ORG\n")
archivo.write("TIPO	MEDIA	MAXIMO	MINIMO	DESV_EST\n")
archivo.write("PRE_RMS	"+str(mean(glo_pre))[0:8]+"	"+str(max(glo_pre))+"	"+str(min(glo_pre))+"	"+str(np.std(glo_pre))[0:8]+"\n")
archivo.write("POS_RMS	"+str(mean(glo_pos))[0:8]+"	"+str(max(glo_pos))+"	"+str(min(glo_pos))+"	"+str(np.std(glo_pos))[0:8]+"\n")

#*******************CODIGO PARA NRMS**********************

nrm_day=[]
nrm_pre_1=[]
nrm_pos_1=[]
nrm_pre_2=[]
nrm_pos_2=[]
nrm_pre_3=[]
nrm_pos_3=[]
nrm_pre_4=[]
nrm_pos_4=[]
nrm_pre_m=[]
nrm_pos_m=[]

for linea in range(1,len(nrm),1):
	temp=nrm[linea][0:-1].split("	")
	if int(temp[0])>=ano1 and int(temp[0])<ano2:
		nrm_day.append(float(temp[2]))
		nrm_pre_1.append(float(temp[3]))
		nrm_pos_1.append(float(temp[4]))
		nrm_pre_2.append(float(temp[5]))
		nrm_pos_2.append(float(temp[6]))
		nrm_pre_3.append(float(temp[7]))
		nrm_pos_3.append(float(temp[8]))
		nrm_pre_4.append(float(temp[9]))
		nrm_pos_4.append(float(temp[10]))

for linea in range(len(nrm_day)):
	temp=[nrm_pre_1[linea],nrm_pre_2[linea],nrm_pre_3[linea],nrm_pre_4[linea]]
	nrm_pre_m.append(float(mean(temp)))
	temp=[nrm_pos_1[linea],nrm_pos_2[linea],nrm_pos_3[linea],nrm_pos_4[linea]]
	nrm_pos_m.append(float(mean(temp)))

nrm_day = np.array(nrm_day)
nrm_pre_m = np.array(nrm_pre_m)
nrm_pos_m = np.array(nrm_pos_m)

x = nrm_day
y = nrm_pre_m
plt.plot(x,y,".",color="purple",label='pre nrms')
plt.xlabel('fecha')
plt.ylabel('nrms')
plt.xlim(ano1,ano2)
plt.ylim(-0.01,5)
plt.title("PRE NRMS")
plt.savefig(carpeta+"/graficas_gamit/nrms_pre.jpg")
plt.clf()

y = nrm_pos_m
plt.plot(x,y,".",color="blue",label='pos nrms')
plt.xlabel('fecha')
plt.ylabel('nrms')
plt.xlim(ano1,ano2)
plt.ylim(-0.0025,1.2)
plt.title("POST NRMS")
plt.savefig(carpeta+"/graficas_gamit/nrms_pos.jpg")
plt.clf()

archivo.write("\nRESULTADOS NRMS\n")
archivo.write("TIPO	MEDIA	MAXIMO	MINIMO	DESV_EST\n")
archivo.write("PRE_NRMS	"+str(mean(nrm_pre_m))[0:8]+"	"+str(max(nrm_pre_m))+"	"+str(min(nrm_pre_m))+"	"+str(np.std(nrm_pre_m))[0:8]+"\n")
archivo.write("POS_NRMS	"+str(mean(nrm_pos_m))[0:8]+"	"+str(max(nrm_pos_m))+"	"+str(min(nrm_pos_m))+"	"+str(np.std(nrm_pos_m))[0:8]+"\n")

#*******************CODIGO PARA NSU**********************
nsu_day=[]
nsu_nsu=[]
nsu_neu=[]
nsu_net=[]
for linea in range(1,len(nsu),1):
	temp=nsu[linea][0:-1].split("	")

	if temp[0].isnumeric():
		if int(temp[0])>=ano1 and int(temp[0])<ano2:
			nsu_day.append(float(temp[2]))
			nsu_nsu.append(float(temp[3]))
			nsu_neu.append(float(temp[4]))
			nsu_net.append(float(temp[5]))

nsu_day = np.array(nsu_day)
nsu_nsu = np.array(nsu_nsu)
nsu_neu = np.array(nsu_neu)
nsu_net = np.array(nsu_net)

x = nsu_day
y = nsu_nsu
plt.plot(x,y,".",color="purple",label='Estaciones sin Utilizar')
plt.xlabel('fecha')
plt.ylabel('No de Estaciones')
plt.xlim(ano1,ano2)
#plt.ylim(-0.01,0.2)
plt.title("Numero de Estaciones sin Utilizar")
plt.savefig(carpeta+"/graficas_gamit/nsu_nsu.jpg")
plt.clf()

y = nsu_neu
plt.plot(x,y,".",color="red",label='Est Utilizadas')
y = nsu_net
plt.plot(x,y,".",color="blue",label='Est Totales')
plt.xlabel('fecha')
plt.ylabel('No de Estaciones')
plt.xlim(ano1,ano2)
#plt.ylim(-0.0025,0.01)
plt.legend(loc='best')
plt.title("Numero de Estaciones Utilizadas")
plt.savefig(carpeta+"/graficas_gamit/nsu_neu.jpg")
plt.clf()

archivo.write("\nRESULTADOS NSU\n")
archivo.write("TIPO	MEDIA	MAXIMO	MINIMO	DESV_EST\n")
archivo.write("EST_NSU	"+str(mean(nsu_nsu))[0:8]+"	"+str(max(nsu_nsu))+"	"+str(min(nsu_nsu))+"	"+str(np.std(nsu_nsu))[0:8]+"\n")
archivo.write("EST_NEU	"+str(mean(nsu_neu))[0:8]+"	"+str(max(nsu_neu))+"	"+str(min(nsu_neu))+"	"+str(np.std(nsu_neu))[0:8]+"\n")
archivo.write("EST_NET	"+str(mean(nsu_net))[0:8]+"	"+str(max(nsu_net))+"	"+str(min(nsu_net))+"	"+str(np.std(nsu_net))[0:8]+"\n")

#*******************CODIGO PARA PAW**********************
paw_day=[]
paw_pawlf=[]
paw_panlf=[]

for linea in range(1,len(paw),1):
	temp=paw[linea][0:-1].split("	")
	if temp[0].isnumeric():
		if int(temp[0])>=ano1 and int(temp[0])<ano2:
			paw_day.append(float(temp[2]))
			paw_pawlf.append(float(temp[3]))
			paw_panlf.append(float(temp[4]))

paw_day = np.array(paw_day)
paw_pawlf = np.array(paw_pawlf)
paw_panlf = np.array(paw_panlf)

x = paw_day
y = paw_pawlf
plt.plot(x,y,".",color="green",label='wl')
plt.xlabel('fecha')
plt.ylabel('WL')
plt.xlim(ano1,ano2)
#plt.ylim(-0.01,0.2)
plt.title("WIDE LANE")
plt.savefig(carpeta+"/graficas_gamit/paw_pawlf.jpg")
plt.clf()

y = paw_panlf
plt.plot(x,y,".",color="purple",label='nl')

plt.xlabel('fecha')
plt.ylabel('NL')
plt.xlim(ano1,ano2)
#plt.ylim(-0.0025,0.01)
#plt.legend(loc='best')
plt.title("NARROW LANE")
plt.savefig(carpeta+"/graficas_gamit/paw_panlf.jpg")
plt.clf()

archivo.write("\nRESULTADOS PAW\n")
archivo.write("TIPO	MEDIA	MAXIMO	MINIMO	DESV_EST\n")
archivo.write("PAWLF	"+str(mean(paw_pawlf))[0:8]+"	"+str(max(paw_pawlf))+"	"+str(min(paw_pawlf))+"	"+str(np.std(paw_pawlf))[0:8]+"\n")
archivo.write("PANLF	"+str(mean(paw_panlf))[0:8]+"	"+str(max(paw_panlf))+"	"+str(min(paw_panlf))+"	"+str(np.std(paw_panlf))[0:8]+"\n")

#*******************CODIGO PARA RMS**********************
rms_day=[]
rms_all=[]
rms_best1=[]
rms_best2=[]
rms_worst1=[]
rms_worst2=[]

for linea in range(1,len(rms),1):
	temp=rms[linea][0:-1].split("	")
	if temp[0].isnumeric() and len(temp)>7:
		if int(temp[0])>=ano1 and int(temp[0])<ano2:
			rms_day.append(float(temp[2]))
			rms_all.append(float(temp[3]))
			rms_best1.append(float(temp[4]))
			rms_best2.append(float(temp[5]))
			rms_worst1.append(float(temp[6]))
			rms_worst2.append(float(temp[7]))

rms_day = np.array(rms_day)
rms_all = np.array(rms_all)
rms_best1 = np.array(rms_best1)
rms_best2 = np.array(rms_best2)
rms_worst1 = np.array(rms_worst1)
rms_worst2 = np.array(rms_worst2)

x = rms_day
y = rms_all
plt.plot(x,y,".",color="black",label='all')
plt.xlabel('fecha')
plt.ylabel('RMS')
plt.xlim(ano1,ano2)
#plt.ylim(-0.01,0.2)
plt.title("RMS all")
plt.savefig(carpeta+"/graficas_gamit/rms_all.jpg")
plt.clf()

y = rms_best1
plt.plot(x,y,".",color="red",label='Best1')
y = rms_best2
plt.plot(x,y,".",color="blue",label='Best2')
plt.xlabel('fecha')
plt.ylabel('RMS')
plt.xlim(ano1,ano2)
plt.legend(loc='best')
plt.ylim(0.1,10)
plt.legend(loc='best')
plt.title("Best RMS")
plt.savefig(carpeta+"/graficas_gamit/rms_best.jpg")
plt.clf()

y = rms_worst2
plt.plot(x,y,".",color="green",label='Worst2')
y = rms_worst1
plt.plot(x,y,".",color="purple",label='Worst1')

plt.xlabel('fecha')
plt.ylabel('RMS')
plt.xlim(ano1,ano2)
plt.legend(loc='best')
#plt.ylim(-0.0025,0.01)
plt.legend(loc='best')
plt.title("Worst RMS")
plt.savefig(carpeta+"/graficas_gamit/rms_worst.jpg")
plt.clf()

archivo.write("\nRESULTADOS RMS\n")
archivo.write("TIPO	MEDIA	MAXIMO	MINIMO	DESV_EST\n")
archivo.write("BEST	"+str(mean(rms_all))[0:8]+"	"+str(max(rms_all))+"	"+str(min(rms_all))+"	"+str(np.std(rms_all))[0:8]+"\n")
archivo.write("BEST1	"+str(mean(rms_best1))[0:8]+"	"+str(max(rms_best1))+"	"+str(min(rms_best1))+"	"+str(np.std(rms_best1))[0:8]+"\n")
archivo.write("BEST2	"+str(mean(rms_best2))[0:8]+"	"+str(max(rms_best2))+"	"+str(min(rms_best2))+"	"+str(np.std(rms_best2))[0:8]+"\n")
archivo.write("WORST1	"+str(mean(rms_worst1))[0:8]+"	"+str(max(rms_worst1))+"	"+str(min(rms_worst1))+"	"+str(np.std(rms_worst1))[0:8]+"\n")
archivo.write("WORST2	"+str(mean(rms_worst2))[0:8]+"	"+str(max(rms_worst2))+"	"+str(min(rms_worst2))+"	"+str(np.std(rms_worst2))[0:8]+"\n")


#*******************************CERRAR ARCHIVOS************************************
archivo.close()
glo_a.close()
nrm_a.close()
nsu_a.close()
paw_a.close()
rms_a.close()
