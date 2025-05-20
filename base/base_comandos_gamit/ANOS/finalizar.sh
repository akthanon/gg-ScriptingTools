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
	sh_glred -s $carpeta 001 $carpeta 365 -expt exme -opt H G T
else
	sh_glred -s $carpeta 001 $carpeta 366 -expt exme -opt H G T
fi


for j in {1..10..1}; do
	./limpiar.sh
done

./mover_a_comprimido.sh

echo "TRABAJO FINALIZADO, POR FIN... -.- DESPUÉS DE UN AÑO"