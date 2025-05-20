carpeta=${PWD##*/}
carpeta=${carpeta:0:4}

bisiesto=(1996 2004 2008 2012 2016 2020)
es_bisiesto=0


for j in {0..5..1}; do
	if [[ $carpeta -eq ${bisiesto[j]} ]]
	then
   		es_bisiesto=1
	fi	
done


if [[ $es_bisiesto -eq 0 ]]
then
	for j in {361..365..1}; do
			sh_gamit -expt exme -d $carpeta ${j} -pres ELEV -orbit IGSF -copt x k p -dopts c ao
	done
else
	for j in {361..366..1}; do
			sh_gamit -expt exme -d $carpeta ${j} -pres ELEV -orbit IGSF -copt x k p -dopts c ao
	done
fi


./ciclo.sh