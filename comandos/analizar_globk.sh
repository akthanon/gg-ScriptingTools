#!/bin/bash
cd ..
carpeta=$(sed -n 16p comandos/parametros.txt)
cd $carpeta
./comparar.sh