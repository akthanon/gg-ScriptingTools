import sys
import numpy as np
import matplotlib.pyplot as plt
#import seaborn as sns; sns.set()  # for plot styling
from sklearn.datasets.samples_generator import make_blobs
from sklearn.cluster import KMeans
from mpl_toolkits import mplot3d
from sklearn.neighbors import KNeighborsClassifier
import random

carpeta=sys.argv[1]
f = open(carpeta+"/apriori/cord_est.txt", "r")
archivo=f.readlines()
lista=[]
names=[]
clusters=int(sys.argv[2])

ano1=int(sys.argv[3])
ano2=int(sys.argv[4])+1

def dist(bx,by,bz,xx,yy,zz):
	difx=bx-xx
	dify=by-yy
	difz=bz-zz
	dista=np.sqrt(np.square(difx)+np.square(dify)+np.square(difz))
	return (dista)

for i in archivo:
	temp=i.split(" ")
	lista.append([float(temp[1]),float(temp[2]),float(temp[3])])
	names.append(temp[0])

npmatrix=np.array(lista)

X=npmatrix
ax1=-1
ax2=1
while abs(ax1-ax2)<8:
	#ax = plt.axes(projection='3d')
	#ax.scatter3D(X[:, 0], X[:, 1],X[:, 2], s=50);
	kmeans = KMeans(n_clusters=clusters,init="random")
	kmeans.fit(X)
	y_kmeans = kmeans.predict(X)

	#for i in range(len(y_kmeans)):
	#	print(y_kmeans[i])
	#	y_kmeans[i]=random.randint(0,1)
	centers = kmeans.cluster_centers_


	#centers=[]
	#for i in range(clusters):
	#	a1=random.randrange(int(min(X[:, 0])),int(max(X[:, 0])))
	#	a2=random.randrange(int(min(X[:, 1])),int(max(X[:, 1])))
	#	a3=random.randrange(int(min(X[:, 2])),int(max(X[:, 2])))
	#	centers.append([a1,a2,a3])
	#plt.plot(X[:, 0],X[:, 1],".",c=y_kmeans,label='esperado')

	itcentro=5

	centers=np.array(centers)

	for z in range(itcentro):

		clases=[]
		new_centers=[]
		for i in range(len(centers)):
			centri=centers[i]
			distan=[]
			coord=[]	
			for j in range(len(X)):
				Xi=X[j]
				distan.append([names[j],dist(centri[0],centri[1],centri[2],Xi[0],Xi[1],Xi[2]),Xi[0],Xi[1],Xi[2],y_kmeans[j]])
			distan = sorted(distan, reverse=False,key=lambda res: res[1])

			sumax1=0
			sumax2=0
			sumax3=0
			suman=0

			for l in range(len(distan)):
				if i==int(distan[l][5]):
					sumax1=sumax1+distan[l][2]
					sumax2=sumax2+distan[l][3]
					sumax3=sumax3+distan[l][4]
					suman=suman+1
			new_centers.append([sumax1/suman,sumax2/suman,sumax3/suman])

			for k in range(int((len(X)/clusters))):
				clases.append([distan[k][0],i])

		for i in range(len(names)):
			name=names[i]
			for j in clases:
				if j[0]==name:
					y_kmeans[i]=j[1]
		centers=np.array(new_centers)


	ax1=0
	ax2=0
	ax3=0
	ax4=0
	ax5=0
	ax6=0
	ax7=0
	ax8=0
	for i in range(len(y_kmeans)):
		if y_kmeans[i]==0:
			ax1+=1
		elif y_kmeans[i]==1:
			ax2+=1
		elif y_kmeans[i]==2:
			ax3+=1
		elif y_kmeans[i]==3:
			ax4+=1
		elif y_kmeans[i]==4:
			ax5+=1
		elif y_kmeans[i]==5:
			ax6+=1
		elif y_kmeans[i]==6:
			ax7+=1
		elif y_kmeans[i]==7:
			ax8+=1

anos=[]
for ano in range(ano1, ano2):
	anos.append(ano)

for i in range(len(distan)):
	colum=distan[i]
	for ano in anos:
		print("rm -r "+carpeta+"_"+str(colum[5])+"/"+str(ano)+"/rinex/"+colum[0]+"*")
#print(ax3)
#print(ax4)
#print(ax5)
#print(ax6)
#print(ax7)
#print(ax8)
#plt.scatter(X[:, 0], X[:, 1], c=y_kmeans, s=50, cmap='viridis')
#plt.scatter(centers[:, 0], centers[:, 1], c='black', s=200, alpha=0.5);
#plt.show()