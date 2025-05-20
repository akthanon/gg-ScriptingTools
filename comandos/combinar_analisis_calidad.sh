#!/bin/bash
cd ..
carpeta=$(sed -n 10p comandos/parametros.txt)
echo "COMBINANDO ARCHIVOS..."
echo "..."
lista=$(ls $carpeta/resultados)
mkdir $carpeta/resultados3
for elemto in $lista; do
	cat $carpeta/resultados/$elemto $carpeta/resultados2/$elemto > $carpeta/resultados3/$elemto
	mv $carpeta/resultados3/$elemto $carpeta/resultados2/$elemto
done

rm -r $carpeta/resultados
mv $carpeta/resultados2 $carpeta/resultados
rm -r $carpeta/resultados2
rm -r $carpeta/resultados3
echo "ARCHIVOS COMBINADOS"