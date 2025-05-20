mkdir rinex2
mkdir referen
mkdir almacen
carpeta=${PWD##*/}
carpeta=${carpeta:0:4}

ano=${carpeta:2:2}
can=0
est='pepino'

mkdir ${carpeta}

stations=(pie1 drao jplm gode monp albh will vndp gold mdo1 algo gol2 nano nlib dubo holb prds amc2 brmu flin)



for j in {001..366..1}; do
	for i in {0..19..1}; do
		x=2
		mv rinex/${stations[i]}${j}0.${ano}o referen/${stations[i]}${j}0.${ano}o
	done
	cd almacen
	ls ../rinex/*${j}0.${ano}o > ${j}.txt
	can=$(wc -l < ${j}.txt)
	can=$((can/2+1))
	while IFS= read -r line; do
		est=$(printf '%s\n' "$line")
		est=${est:9:4}
		mv ../rinex/${est}${j}0.${ano}o ../rinex2/${est}${j}0.${ano}o
		if [ $can -lt 1 ]; then			
			break
		fi
		can=$(($can-1))
	done < ${j}.txt
	cd ..
	echo $j
done

mv rinex2 ${carpeta}/rinex
cp -r igs ${carpeta}/igs
cp -r brdc ${carpeta}/brdc
cp -r ../comprimidos_base/* ${carpeta}
cp -r referen/* ${carpeta}/rinex
mv referen/* rinex

mv ${carpeta} ../${carpeta}_2
cd ..
mv ${carpeta} ${carpeta}_1
cd ${carpeta}_1