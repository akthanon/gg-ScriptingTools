carpeta=${PWD##*/}
carpeta_base=$PWD
carpeta=${carpeta:0:4}
sh_setup -yr $carpeta
cp $HOME/gg/tables/ut1 tables/
cp $HOME/gg/tables/pole tables/
mv sites.defaults tables/sites.defaults
mv INFO_STATION tables
rm -r tables/station.info
ls rinex > listado_rinex.txt
mkdir errores
mkdir progreso

est="pepino"
tam=20000


while IFS= read -r line; do
	est=$(printf '%s\n' "$line")
	tam="$(ls -lrt rinex/${est} | nawk '{print $5}') "
	
	if [ $tam -lt 20000 ]
	then
   		rm rinex/${est}
	echo $tam
	fi	
done < listado_rinex.txt

python3 ../../programas/actualizar_estaciones.py $carpeta_base
chmod +x actualizar.sh
chmod +x eliminar.sh
mv actualizar.sh tables

./eliminar.sh
cd tables
./actualizar.sh
rm -r actualizar.sh

cd ..
#rm -r eliminar.sh

python3 ../../programas/limpiar_info.py $carpeta_base
python3 ../../programas/limpiar_estaciones.py $carpeta_base
python3 ../../programas/eliminar_estaciones.py $carpeta_base

chmod +x eliminar2.sh
./eliminar2.sh
#rm -r eliminar.sh


