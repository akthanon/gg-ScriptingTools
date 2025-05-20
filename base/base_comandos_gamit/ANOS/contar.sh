rm contador
mkdir contador
carpeta=${PWD##*/}
carpeta=${carpeta:0:4}

ano=${carpeta:2:2}

cd contador
for j in {001..366..1}; do
	ls ../rinex/*${j}0.${ano}o > ${j}.txt
	can=$(wc -l < ${j}.txt)
	if [ $can -gt 80 ]; then			
		echo $j "	:	" $can
	fi
done