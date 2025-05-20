#!/bin/bash
cd ..
carpeta=Comprimido_$(sed -n 10p comandos/parametros.txt)
echo "ANALIZANDO RESULTADOS DE GAMIT..."
echo "..."
ano1=$(sed -n 2p comandos/parametros.txt)
ano2=$(sed -n 4p comandos/parametros.txt)
rm -r $carpeta/datos
mkdir $carpeta/datos
grep 'Post RMS' $carpeta/*/gsoln/*.org > $carpeta/datos/globk_org_stats.txt

grep 'Number of stations used' $carpeta/*/*/*.summary > $carpeta/datos/NSU_summary_stats.txt
grep 'RMS  ' $carpeta/*/*/*.summary > $carpeta/datos/RMS_summary_stats.txt
grep ' Prefit nrms' $carpeta/*/*/*.summary > $carpeta/datos/NRMS_summary_stats.txt
grep 'Phase ambiguities WL' $carpeta/*/*/*.summary > $carpeta/datos/PAW_summary_stats.txt

rm -r $carpeta/resultados_gamit
rm -r $carpeta/graficas_gamit
mkdir $carpeta/resultados_gamit
mkdir $carpeta/graficas_gamit

python3 programas/globk_org_python.py $carpeta > $carpeta/resultados_gamit/globk_org.txt
python3 programas/NSU_python.py $carpeta > $carpeta/resultados_gamit/NSU.txt
python3 programas/RMS_python.py $carpeta > $carpeta/resultados_gamit/RMS.txt
python3 programas/NRMS_python.py $carpeta > $carpeta/resultados_gamit/NRMS.txt
python3 programas/PAW_python.py $carpeta > $carpeta/resultados_gamit/PAW.txt
python3 programas/graficas_gamit.py $carpeta $ano1 $ano2

#python3 programas/NRMS_python.py $carpeta
#python3 programas/NSU_python.py $carpeta
#python3 programas/RMS_python.py $carpeta
#python3 programas/PAW_python.py $carpeta

echo "AMO JORGE, SUS resultados_gamit ESTÁN LISTOS"
