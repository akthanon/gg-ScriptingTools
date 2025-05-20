import matplotlib.pyplot as plt
import numpy as np
import sys
import os
from statistics import mean
from math import sqrt
import datetime

posvel_a = open("datos/rmsposvel.txt", "r")
archivo = open("datos/estadisticas_graficas.txt", "w")
posvel=posvel_a.readlines()



#*****************INICIALIZAR LOS VECTORES***********************

#*******************CODIGO PARA GLOBK_ORG**********************
posvel_nsit=[]
posvel_ewrms=[]
posvel_nwrms=[]
posvel_uwrms=[]
posvel_enrms=[]
posvel_nnrms=[]
posvel_unrms=[]
posvel_fecha=[]

for linea in range(1,len(posvel),1):
	temp=posvel[linea][0:-1].split("	")
	if not("nan" in str(float(temp[1])) or "nan" in str(float(temp[2])) or "nan" in str(float(temp[3])) or "nan" in str(float(temp[4])) or "nan" in str(float(temp[5])) or "nan" in str(float(temp[6]))):
		posvel_code=temp[7]
		il=int(float(posvel_code[1:3]))
		en=int(float(posvel_code[3:5]))
		am=int(float(posvel_code[5:7]))
		if il>50:
			year=il+1900
		else:
			year=il+2000
		date=datetime.datetime(year,en,am)
		day=date.timetuple().tm_yday
		yeardec=year+day/366
		posvel_fecha.append(yeardec)
		posvel_nsit.append(float(temp[0]))
		posvel_ewrms.append(float(temp[1]))
		posvel_nwrms.append(float(temp[2]))
		posvel_uwrms.append(float(temp[3]))
		posvel_enrms.append(float(temp[4]))
		posvel_nnrms.append(float(temp[5]))
		posvel_unrms.append(float(temp[6]))

posvel_fecha= np.array(posvel_fecha)
posvel_ewrms= np.array(posvel_ewrms)
posvel_nwrms= np.array(posvel_nwrms)
posvel_uwrms= np.array(posvel_uwrms)
posvel_enrms= np.array(posvel_enrms)
posvel_nnrms= np.array(posvel_nnrms)
posvel_unrms= np.array(posvel_unrms)
posvel_nsit= np.array(posvel_nsit)

ano1=int(min(posvel_fecha))
ano2=int(max(posvel_fecha))
x = posvel_fecha
y = posvel_ewrms
plt.plot(x,y,".",color="red",label='ewrms')
plt.xlabel('fecha')
plt.ylabel('ewrms')
plt.xlim(ano1,ano2)
plt.title("EWRMS")
plt.savefig("graficas/ewrms.jpg")
plt.clf()

y = posvel_nwrms
plt.plot(x,y,".",color="blue",label='nwrms')
plt.xlabel('fecha')
plt.ylabel('nwrms')
plt.xlim(ano1,ano2)
plt.title("NWRMS")
plt.savefig("graficas/nwrms.jpg")
plt.clf()

y = posvel_uwrms
plt.plot(x,y,".",color="black",label='uwrms')
plt.xlabel('fecha')
plt.ylabel('uwrms')
plt.xlim(ano1,ano2)
plt.title("UWRMS")
plt.savefig("graficas/uwrms.jpg")
plt.clf()

y = posvel_enrms
plt.plot(x,y,".",color="red",label='enrms')
plt.xlabel('fecha')
plt.ylabel('enrms')
plt.xlim(ano1,ano2)
plt.title("ENRMS")
plt.savefig("graficas/enrms.jpg")
plt.clf()

y = posvel_nnrms
plt.plot(x,y,".",color="blue",label='nnrms')
plt.xlabel('fecha')
plt.ylabel('nnrms')
plt.xlim(ano1,ano2)
plt.title("NNRMS")
plt.savefig("graficas/nnrms.jpg")
plt.clf()

y = posvel_unrms
plt.plot(x,y,".",color="black",label='unrms')
plt.xlabel('fecha')
plt.ylabel('unrms')
plt.xlim(ano1,ano2)
plt.title("UNRMS")
plt.savefig("graficas/unrms.jpg")
plt.clf()

y = posvel_nsit
plt.plot(x,y,".",color="green",label='nsit')
plt.xlabel('fecha')
plt.ylabel('nsit')
plt.xlim(ano1,ano2)
plt.title("NSIT")
plt.savefig("graficas/znsit.jpg")
plt.clf()


archivo.write("RESULTADOS WRMS\n")
archivo.write("TIPO	MEDIA	MAXIMO	MINIMO	DESV_EST\n")
archivo.write("WEAST	"+str(mean(posvel_ewrms))[0:8]+"	"+str(max(posvel_ewrms))+"	"+str(min(posvel_ewrms))+"	"+str(np.std(posvel_ewrms))[0:8]+"\n")
archivo.write("WNORTH	"+str(mean(posvel_nwrms))[0:8]+"	"+str(max(posvel_nwrms))+"	"+str(min(posvel_nwrms))+"	"+str(np.std(posvel_nwrms))[0:8]+"\n")
archivo.write("WUP	"+str(mean(posvel_uwrms))[0:8]+"	"+str(max(posvel_uwrms))+"	"+str(min(posvel_uwrms))+"	"+str(np.std(posvel_uwrms))[0:8]+"\n")

archivo.write("\nRESULTADOS NRMS\n")
archivo.write("TIPO	MEDIA	MAXIMO	MINIMO	DESV_EST\n")
archivo.write("NEAST	"+str(mean(posvel_enrms))[0:8]+"	"+str(max(posvel_enrms))+"	"+str(min(posvel_enrms))+"	"+str(np.std(posvel_enrms))[0:8]+"\n")
archivo.write("NNORTH	"+str(mean(posvel_nnrms))[0:8]+"	"+str(max(posvel_nnrms))+"	"+str(min(posvel_nnrms))+"	"+str(np.std(posvel_nnrms))[0:8]+"\n")
archivo.write("NUP	"+str(mean(posvel_unrms))[0:8]+"	"+str(max(posvel_unrms))+"	"+str(min(posvel_unrms))+"	"+str(np.std(posvel_unrms))[0:8]+"\n")

archivo.write("\nRESULTADOS NEST\n")
archivo.write("TIPO	MEDIA	MAXIMO	MINIMO	DESV_EST\n")
archivo.write("NEST	"+str(mean(posvel_nsit))[0:8]+"	"+str(max(posvel_nsit))+"	"+str(min(posvel_nsit))+"	"+str(np.std(posvel_nsit))[0:8]+"\n")


#*******************************CERRAR ARCHIVOS************************************
posvel_a.close()
archivo.close()