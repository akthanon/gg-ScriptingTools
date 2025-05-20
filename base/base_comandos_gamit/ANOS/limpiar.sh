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
	sh_cleanup -s $carpeta 001 365 -copt x k p -dopts c ao
else
	sh_cleanup -s $carpeta 001 366 -copt x k p -dopts c ao
fi
