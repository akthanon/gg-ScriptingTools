#!/bin/bash
cd ..
carpeta=$(sed -n 10p comandos/parametros.txt)
ano1=$(sed -n 2p comandos/parametros.txt)
ano2=$(sed -n 4p comandos/parametros.txt)
mejores_referencia=$(sed -n 6p comandos/parametros.txt)
formula=$(sed -n 26p comandos/parametros.txt)

rm -r $carpeta/resultados_referencia
mkdir $carpeta/resultados_referencia

echo "ANALIZANDO ESTACIONES DE REFERENCIA..."
echo "..."
python3 programas/cuenta_datos.py $carpeta $ano1 $ano2
python3 programas/cuenta_breaks.py $carpeta $ano1 $ano2
python3 programas/extrae_datos.py $carpeta
python3 programas/analiza_datos.py $carpeta $ano1 $ano2 $mejores_referencia $formula
python3 programas/analiza_datos_sin_calidad.py $carpeta $ano1 $ano2 $formula

mv $carpeta/*.txt $carpeta/resultados_referencia

echo "LISTO EL PISTO"