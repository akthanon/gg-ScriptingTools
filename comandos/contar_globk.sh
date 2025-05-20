#!/bin/bash
cd ..
carpeta=$(sed -n 16p comandos/parametros.txt)
echo "PROCESANDO CON GLOBK DE ACUERDO A LOS DIFERENTES PARAMETROS..."
echo "..."

ano1=$(sed -n 2p comandos/parametros_globk.txt)
ano2=$(sed -n 4p comandos/parametros_globk.txt)
nerf=$(sed -n 6p comandos/parametros_globk.txt)
pser=$(sed -n 8p comandos/parametros_globk.txt)
mejot=$(sed -n 10p comandos/parametros_globk.txt)
mejok=$(sed -n 11p comandos/parametros_globk.txt)
mejod=$(sed -n 12p comandos/parametros_globk.txt)
mejow=$(sed -n 13p comandos/parametros_globk.txt)
mejos=$(sed -n 14p comandos/parametros_globk.txt)
mejoc=$(sed -n 15p comandos/parametros_globk.txt)
mejor=$mejot$mejok$mejod$mejow$mejos$mejoc
mode=$(sed -n 17p comandos/parametros_globk.txt)

nerfb=$(sed -n 19p comandos/parametros_globk.txt)
pserb=$(sed -n 21p comandos/parametros_globk.txt)
mejob=$(sed -n 23p comandos/parametros_globk.txt)
modeb=$(sed -n 25p comandos/parametros_globk.txt)

ano1b=$(sed -n 27p comandos/parametros_globk.txt)
ano2b=$(sed -n 29p comandos/parametros_globk.txt)

contador=0
#PARA TODAS LAS CONFIGURACIONES Y 2 MODELOS
for nano1 in $ano1; do
	for nano2 in $ano2; do
		for nnerf in $nerf; do
			conmej=0
			for npser in $pser; do
				for nmodex in $modeb; do
					let l1=conmej*20*5
					esta=${mejor:$l1:100}
					let contador=contador+1
				done
				let conmej=conmej+1
			done
		done
	done
done

#PARA 1 CONFIGURACIÓN Y TODOS LOS MODELOS
for nmode in $mode; do
	for nnerfb in $nerfb; do
		let contador=contador+1
	done
done
echo "AMO JORGE, Resultaron: "$contador" resultados posibles"
