import matplotlib.pyplot as plt
import numpy as np
import sys
import os
from statistics import mean
from math import sqrt
import datetime
from matplotlib import cm

contenido_rms = os.listdir("comparaciones/datos_rms")
contenido_posvel = os.listdir("comparaciones/datos_posvel")

def norm(df):
	res=(df - df.min()) / ( df.max() - df.min())
	return res

contenido_rms = sorted(contenido_rms, reverse=True)
contenido_posvel = contenido_rms

archivo1 = open("comparaciones/rms_resultados.txt", "w")
archivo2 = open("comparaciones/posvel_resultados.txt", "w")
#*****************INICIALIZAR LOS VECTORES***********************
posvel_param=[]
posvel_wrms=[]
posvel_nrms=[]

for param in contenido_posvel:
	a = open("comparaciones/datos_posvel/"+param, "r")
	archivo=a.readlines()
	posvel_param.append(param)
	#print(param)
	ewrms=float(archivo[0].split(" ")[1])
	nwrms=float(archivo[1].split(" ")[1])
	uwrms=float(archivo[2].split(" ")[1])
	enrms=float(archivo[3].split(" ")[1])
	nnrms=float(archivo[4].split(" ")[1])
	unrms=float(archivo[5].split(" ")[1])
	wrms=sqrt(ewrms**2+nwrms**2+uwrms**2)
	nrms=sqrt(enrms**2+nnrms**2+unrms**2)
	posvel_wrms.append(wrms)
	posvel_nrms.append(nrms)
	a.close()

rms_param=[]
rms_wrms=[]
rms_nrms=[]
for param in contenido_rms:
	a = open("comparaciones/datos_rms/"+param, "r")
	archivo=a.readlines()
	rms_param.append(param[0:-4])
	num=0
	ewrms=0
	nwrms=0
	uwrms=0
	enrms=0
	nnrms=0
	unrms=0
	for i in range(1,len(archivo),1):
		ewrms=ewrms+float(archivo[i].split("	")[3])
		nwrms=nwrms+float(archivo[i].split("	")[1])
		uwrms=uwrms+float(archivo[i].split("	")[5])
		enrms=enrms+float(archivo[i].split("	")[4])
		nnrms=nnrms+float(archivo[i].split("	")[2])
		unrms=unrms+float(archivo[i].split("	")[6])
		num=num+1

	ewrms=ewrms/num
	nwrms=nwrms/num
	uwrms=uwrms/num
	enrms=enrms/num
	nnrms=nnrms/num
	unrms=unrms/num

	wrms=sqrt(ewrms**2+nwrms**2+uwrms**2)
	nrms=sqrt(enrms**2+nnrms**2+unrms**2)
	rms_wrms.append(wrms)
	rms_nrms.append(nrms)
	a.close()

param=np.array(rms_param)
rms_wrms=np.array(rms_wrms)
posvel_wrms=np.array(posvel_wrms)

#*******************CODIGO PARA GLOBK_ORG**********************

x = np.arange(len(param))
y = rms_wrms
width=10
height=10

yc=norm(y)/2+0.4
colors = cm.gist_rainbow(1-(yc / float(max(yc)))-0.2)
plot = plt.scatter(y, y, c = y, cmap = 'gist_rainbow')
plt.clf()
plt.colorbar(plot)

plt.figure(figsize=(25, 10))
plt.barh(x,y,color=colors,align='center', alpha=1)
#plt.xlabel('parametros')
plt.yticks(x, param,rotation=-0, ha="right")
plt.title("WRMS")
plt.savefig("comparaciones/graficas/rms_wrms.jpg")
plt.clf()

y = posvel_wrms
yc=norm(y)/2+0.4
colorsa = cm.gist_rainbow(1-(yc / float(max(yc))))
plot = plt.scatter(y, y, c = y, cmap = 'gist_rainbow')
plt.clf()
plt.colorbar(plot)

plt.figure(figsize=(25, 10))
plt.barh(x,y,color=colorsa,align='center', alpha=1)
plt.yticks(x, param,rotation=-0, ha="right")
#plt.xlabel('parametros')
plt.title("WRMS")
plt.savefig("comparaciones/graficas/pos_wrms.jpg")
plt.clf()

for linea in range(len(param)):
	archivo1.write(str(param[linea])+"	"+str(rms_wrms[linea])+"\n")
	archivo2.write(str(param[linea])+"	"+str(posvel_wrms[linea])+"\n")

archivo1.close()
archivo2.close()
