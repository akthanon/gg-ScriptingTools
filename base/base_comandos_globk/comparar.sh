separador=" : "
zruta="$(pwd) "
direc=$(ls resultados)
rm -r comparaciones
mkdir comparaciones
mkdir comparaciones/datos_posvel
mkdir comparaciones/datos_rms
mkdir comparaciones/graficas
cd resultados

for carpeta in $direc; do
	cd ${carpeta}
	echo $(grep "WEAST" datos/estadisticas_graficas.txt)"
"$(grep "WNORTH" datos/estadisticas_graficas.txt)"
"$(grep "WUP" datos/estadisticas_graficas.txt)"
"$(grep "NEAST" datos/estadisticas_graficas.txt)"
"$(grep "NNORTH" datos/estadisticas_graficas.txt)"
"$(grep "NUP" datos/estadisticas_graficas.txt)> ../../comparaciones/datos_posvel/${carpeta}.txt
	cat datos/rms.txt > ../../comparaciones/datos_rms/${carpeta}.txt
	cd ..
done
cd ..

python3 graficas_globk_general.py

