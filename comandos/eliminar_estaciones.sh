#!/bin/bash
cd ..
carpeta=$(sed -n 10p comandos/parametros.txt)
echo "ELIMINANDO LAS CAGADAS..."
echo "..."
chmod +x $carpeta/elim_refe.sh
chmod +x $carpeta/elim_esta.sh


stations=$(sed -n 1p $carpeta/apriori/list_esta.txt)" "$(sed -n 1p $carpeta/apriori/list_referen.txt)
stations_elim=$(sed -n 1p $carpeta/apriori/list_elim.txt)
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

cd $carpeta
./elim_esta.sh
./elim_refe.sh
cd ..

echo "YA BORRADA LA CAGADA"

j=0
for (( cyear=$ano1; cyear<=$ano2; cyear++ )); do #AÑOS
    cp $HOME/PROYECTOS/base/base_comandos_gamit/ANOS/* $carpeta/$cyear     
    let j=$j+1
done

cd comandos

./clasificar_estaciones.sh