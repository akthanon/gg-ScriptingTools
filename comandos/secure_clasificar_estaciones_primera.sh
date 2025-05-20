#!/bin/bash
cd ..
carpeta=$(sed -n 10p comandos/parametros.txt)
clusters=$(sed -n 28p comandos/parametros.txt)
ano1=$(sed -n 2p comandos/parametros.txt)
ano2=$(sed -n 4p comandos/parametros.txt)
echo "COMBINANDO DATOS PARA PROCESAR EN GAMIT..."
echo "..."

mkdir ${carpeta}_0
mkdir ${carpeta}_1

cp -r $carpeta/* ${carpeta}_0
cp -r $carpeta/* ${carpeta}_1 
python programas/clasificar_python.py $carpeta $clusters $ano1 $ano2 > comandos/class_temp.sh
chmod +x comandos/class_temp.sh
./comandos/class_temp.sh
rm -r $carpeta

echo "AMO JORGE, SUS ARCHIVOS ESTÁN LISTOS"
