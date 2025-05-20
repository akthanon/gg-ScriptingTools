carpeta=${PWD##*/}
carpeta=${carpeta:0:4}
rename -f 'y/A-Z/a-z/' rinex/*
./pre_inicio.sh

eje=1
while [ $eje -ne 0 ]; do
	temp=0
	echo "VERIFICANDO SI EXISTEN DATOS EXTRA"
	echo "..."
	for i in {001..366..1}; do #DIAS
		if [[ $(ls rinex/*${i}0* | wc -l) -gt 80 ]]
		then
			let temp=temp+$(ls rinex/*${i}0* | wc -l)
			echo $i $(ls rinex/*${i}0* | wc -l)
		fi
	done
	eje=$temp
	echo "NO PUEDES PROCESAR DATOS, HAY DATOS EXTRA"
	sleep 5s
	clear
done

echo "YA PUEDES PROCESAR DATOS"
./checar.sh
./progreso.sh



