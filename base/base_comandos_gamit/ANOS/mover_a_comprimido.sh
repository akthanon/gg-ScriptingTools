carpeta=${PWD##*/}
carpeta=${carpeta:0:4}
cd ..
carpeta_base=${PWD##*/}
mkdir Comprimido_${carpeta_base}
mkdir Comprimido_${carpeta_base}/$carpeta
mkdir Comprimido_${carpeta_base}/${carpeta}/gsoln
mkdir Comprimido_${carpeta_base}/${carpeta}/glbf
cp -r $carpeta/gsoln/*.org Comprimido_${carpeta_base}/${carpeta}/gsoln
cp -r $carpeta/glbf/h*glx Comprimido_${carpeta_base}/${carpeta}/glbf

for i in {001..366..1}; do #DIAS
	mkdir Comprimido_${carpeta_base}/$carpeta/$i
	cp $carpeta/$i/*.summary Comprimido_${carpeta_base}/$carpeta/$i
	rm -r $carpeta/$i/otl.grid
	rm -r $carpeta/$i/antmod.dat
	rm -r $carpeta/$i/atl.grid
	rm -r $carpeta/$i/*.gz
	rm -r $carpeta/$i/DPH*
done
rm -r $carpeta/rinex
mkdir rinex
rar a ${carpeta}.rar $carpeta
cd ..
mkdir RAR_${carpeta_base}
mkdir Comprimido_${carpeta_base}
mkdir Comprimido_${carpeta_base}/$carpeta
mv ${carpeta_base}/${carpeta}.rar RAR_${carpeta_base}
rm -r Comprimido_${carpeta_base}/$carpeta
mv ${carpeta_base}/Comprimido_${carpeta_base}/* Comprimido_${carpeta_base}/$carpeta
rm -r ${carpeta_base}/Comprimido_${carpeta_base}
echo "LISTO EL BURRO"