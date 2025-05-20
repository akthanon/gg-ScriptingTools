#!/bin/bash
cd ..
carpeta=$(sed -n 10p comandos/parametros.txt)

echo 'Iniciando analisis de datos.'
echo 'Por favor espere..........'
stations=$(sed -n 1p $carpeta/apriori/list_esta.txt)" "$(sed -n 1p $carpeta/apriori/list_referen.txt)
stations_elim=$(sed -n 1p $carpeta/apriori/list_elim.txt)
rm -r $carpeta/resultados
rename -f 'y/A-Z/a-z/' $carpeta/*/rinex/*
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

j=0
for (( cyear=$ano1; cyear<=$ano2; cyear++ )); do #AÑOS
    anio=${cyear:2:4}
    for station in $stations; do #ESTACIONES
        rename -f 'y/A-Z/a-z/' $carpeta/${cyear}/rinex/${station}*.${anio}o
    done
    for elima in $stations_elim; do #ESTACIONES
        rm -r $carpeta/${cyear}/rinex/${elima}*.${anio}o
    done      
    echo $anio
    let j=$j+1
done

j=0
for (( cyear=$ano1; cyear<=$ano2; cyear++ )); do #AÑOS
    anio=${cyear:2:4}
    rm -r $base/$carpeta/${cyear}/rinex/*S
    for i in {001..366..1}; do #DIAS
        for station in $stations; do #ESTACIONES
            ./programas/teqc +qc -set_mask 10 -nav $base/$carpeta/${cyear}/brdc/brdc${i}0.${anio}n $base/$carpeta/${cyear}/rinex/${station}${i}0.${anio}o
        done
    done
    let j=$j+1
done

for station in $stations; do #ESTACIONES
    j=0
    for (( cyear=$ano1; cyear<=$ano2; cyear++ )); do #AÑOS
        for k in {001..366..1}; do #DIAS
            anio=${cyear:2:4}
            FILE=$base/$carpeta/${cyear}/rinex/${station}${k}0.${anio}S
            echo $FILE
            if [ -f $FILE ]; then
                echo ${cyear}" "${k} >> $carpeta/"OUT_NAM_"${station}"_"${anio}.txt
                grep -e 'SSN ' $base/$carpeta/${cyear}/rinex/${station}${k}0.${anio}S >> $base/$carpeta/${cyear}/rinex/"OUT_SSN_"${station}"_"${anio}.txt
                grep -e 'SUM ' $base/$carpeta/${cyear}/rinex/${station}${k}0.${anio}S >> $base/$carpeta/${cyear}/rinex/"OUT_SUM_"${station}"_"${anio}.txt
            fi
        done
        mv $base/$carpeta/${cyear}/rinex/"OUT_NAM_"${station}"_"${anio}.txt $base/$carpeta
        mv $base/$carpeta/${cyear}/rinex/"OUT_SSN_"${station}"_"${anio}.txt $base/$carpeta
        mv $base/$carpeta/${cyear}/rinex/"OUT_SUM_"${station}"_"${anio}.txt $base/$carpeta
        let j=$j+1
    done
    cat $carpeta/OUT_NAM_${station}*.txt > $carpeta/"FINAL_NAM_"${station}.txt 
    cat $carpeta/OUT_SSN_${station}*.txt > $carpeta/"FINAL_SSN_"${station}.txt 
    cat $carpeta/OUT_SUM_${station}*.txt > $carpeta/"FINAL_SUM_"${station}.txt
    echo | paste $carpeta/"FINAL_NAM_"${station}.txt $carpeta/"FINAL_SSN_"${station}.txt $carpeta/"FINAL_SUM_"${station}.txt > $carpeta/"COM_SUM_"${station}.txt
    tam="$(ls -lrt $carpeta/"COM_SUM_"${station}.txt | nawk '{print $5}') "
    if [ $tam -lt 0 ]
    then
        rm $carpeta/"COM_SUM_"${station}.txt
    echo $tam
    fi
done


#cd $base
rm $carpeta/resultados/COM_SUM_.txt
rm $carpeta/COM_SUM_.txt
rm -r $carpeta/OUT*
rm -r $carpeta/FINAL*
rm -r $carpeta/resultados
rm -r $carpeta/resultados_limpios
rm -r $carpeta/mejores*.txt
rm -r $carpeta/elim_esta.sh
rm -r $carpeta/resultados_calidad

rm -r $carpeta/graficas
rm -r $carpeta/sta_*
mkdir $carpeta/resultados
mv $carpeta/COM_SUM* $carpeta/resultados
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


j=0
for (( cyear=$ano1; cyear<=$ano2; cyear++ )); do
    anio=${cyear:2:4}
    for station in $stations; do #ESTACIONES
        rm -r $carpeta/${cyear}/rinex/${station}*.${anio}S
    done
    rm -r $carpeta/${cyear}/rinex/*S
    echo $anio
    let j=$j+1
done


echo 'Ya está hecha la machaca morro'