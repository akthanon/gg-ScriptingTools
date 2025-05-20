direc=$(ls resultados)

base=$PWD
cd resultados
for carpeta in $direc; do
	cp $base/graficas_globk_particular.py $carpeta
	mkdir $carpeta/graficas
	cd ${carpeta}
	./ejecutar.sh
	cd ..
done

