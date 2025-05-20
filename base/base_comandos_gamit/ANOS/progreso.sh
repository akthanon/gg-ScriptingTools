can=1
eje=1
day=XXX
est=0
carpeta=${PWD##*/}
carpeta=${carpeta:0:4}
cont=0

bisiesto=(1996 2004 2008 2012 2016 2020)
es_bisiesto=0


for j in {0..5..1}; do
	if [[ $carpeta -eq ${bisiesto[j]} ]]
	then
   		es_bisiesto=1
	fi	
done

while [ $eje -ne 0 ]
do
	./base_progreso.sh > ejecutar_gamit_X.sh
	ls ???/GAMIT.fatal > fatalitys_opcion.txt
    eje=$(wc -l < ejecutar_gamit_X.sh)
    can=$(wc -l < fatalitys.txt)

    echo "FALTANTES"
	echo $eje
	echo "ERRORES"
	cat fatalitys_opcion.txt | wc -l
	echo ""
	echo "PORCENTAJE COMPLETADO:"

	for j in {030..001..-1}; do
		FILE=$j
		if [ -d "$FILE" ]; then
		    echo ${FILE}/030
		    break
		fi
	done
	for j in {060..031..-1}; do
		FILE=$j
		if [ -d "$FILE" ]; then
		    echo ${FILE}/060
		    break
		fi
	done
	for j in {090..061..-1}; do
		FILE=$j
		if [ -d "$FILE" ]; then
		    echo ${FILE}/090
		    break
		fi
	done
	for j in {120..091..-1}; do
		FILE=$j
		if [ -d "$FILE" ]; then
		    echo ${FILE}/120
		    break
		fi
	done
	for j in {150..121..-1}; do
		FILE=$j
		if [ -d "$FILE" ]; then
		    echo ${FILE}/150
		    break
		fi
	done
	for j in {180..151..-1}; do
		FILE=$j
		if [ -d "$FILE" ]; then
		    echo ${FILE}/180
		    break
		fi
	done
	for j in {210..181..-1}; do
		FILE=$j
		if [ -d "$FILE" ]; then
		    echo ${FILE}/210
		    break
		fi
	done
	for j in {240..211..-1}; do
		FILE=$j
		if [ -d "$FILE" ]; then
		    echo ${FILE}/240
		    break
		fi
	done
	for j in {270..241..-1}; do
		FILE=$j
		if [ -d "$FILE" ]; then
		    echo ${FILE}/270
		    break
		fi
	done
	for j in {300..271..-1}; do
		FILE=$j
		if [ -d "$FILE" ]; then
		    echo ${FILE}/300
		    break
		fi
	done
	for j in {330..301..-1}; do
		FILE=$j
		if [ -d "$FILE" ]; then
		    echo ${FILE}/330
		    break
		fi
	done
	for j in {360..331..-1}; do
		FILE=$j
		if [ -d "$FILE" ]; then
		    echo ${FILE}/360
		    break
		fi
	done
	if [[ $es_bisiesto -eq 0 ]]
	then
		for j in {365..361..-1}; do
			FILE=$j
			if [ -d "$FILE" ]; then
			    echo ${FILE}/365
			    break
			fi
		done
	else
		for j in {366..361..-1}; do
			FILE=$j
			if [ -d "$FILE" ]; then
			    echo ${FILE}/366
			    break
			fi
		done
	fi


	sleep 60s
	clear
done