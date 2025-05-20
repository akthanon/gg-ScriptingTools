#!/bin/bash
cd ..
carpeta=$(sed -n 10p comandos/parametros.txt)
echo 'Iniciando analisis de datos.'
echo 'Por favor espere..........'
stations=$(sed -n 1p $carpeta/apriori/list_esta.txt)" "$(sed -n 1p $carpeta/apriori/list_referen.txt)
rm $carpeta/*/rinex/*a.*o
base=$PWD
anio=${carpeta:2:4}
ano1=$(sed -n 2p comandos/parametros.txt)
ano2=$(sed -n 4p comandos/parametros.txt)
mejores_estaciones=$(sed -n 8p comandos/parametros.txt)
peso=$(sed -n 12p comandos/parametros.txt)
mini=$(sed -n 14p comandos/parametros.txt)

int=$(sed -n 18p comandos/parametros.txt)
opc=$(sed -n 20p comandos/parametros.txt)
por=$(sed -n 22p comandos/parametros.txt)
graficar=$(sed -n 24p comandos/parametros.txt)
formula=$(sed -n 26p comandos/parametros.txt)

rm $carpeta/resultados/COM_SUM_.txt
rm $carpeta/COM_SUM_.txt
rm -r $carpeta/resultados_limpios
rm -r $carpeta/graficas
rm -r $carpeta/mejores*.txt
rm -r $carpeta/elim_esta.sh
rm -r $carpeta/resultados_calidad

mkdir $carpeta/graficas
mkdir $carpeta/resultados_limpios

python3 programas/graficas.py $carpeta $ano1 $ano2 $mejores_estaciones $peso $mini $int $opc $por $graficar $formula > $carpeta/resultados_calidad.txt
rm -r $carpeta/graficas/mulipath
rm -r $carpeta/graficas/observaciones
rm -r $carpeta/graficas/porcentaje
rm -r $carpeta/graficas/snr
rm -r $carpeta/graficas/obsporciclo

mkdir $carpeta/graficas/mulipath
mkdir $carpeta/graficas/observaciones
mkdir $carpeta/graficas/porcentaje
mkdir $carpeta/graficas/snr
mkdir $carpeta/graficas/obsporciclo
mkdir $carpeta/resultados_calidad

mv $carpeta/graficas/mpt_* $carpeta/graficas/mulipath
mv $carpeta/graficas/obs_* $carpeta/graficas/observaciones
mv $carpeta/graficas/por_* $carpeta/graficas/porcentaje
mv $carpeta/graficas/snr_* $carpeta/graficas/snr
mv $carpeta/graficas/opc_* $carpeta/graficas/obsporciclo
mv $carpeta/*.txt $carpeta/resultados_calidad


echo 'YA ESTÁ HECHA LA MACHACA MORRO'