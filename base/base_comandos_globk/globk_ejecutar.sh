
rm -r vsoln
rm -r series
rm -r globk_long.cmd
rm -r glorg_long.cmd
mkdir series
mkdir vsoln
mkdir emed_rinex
mkdir graficas

./editar_archivos.sh

cp globk_long.cmd vsoln/
cp glorg_long.cmd vsoln/
cp valeq_file.eq vsoln/
ano1=$(sed -n 2p parametros.txt)
ano2=$(sed -n 4p parametros.txt)
cd vsoln

mkdir anos

nano1=${ano1:0:4}
nano2=${ano2:0:4}

for (( cyear=$nano1; cyear<=$nano2; cyear++ )); do #AÑOS
	mkdir anos/$cyear
	mkdir anos/$cyear/glbf
	echo "copiando año "$cyear" de "$nano2
	cp ../$cyear/glbf/* anos/$cyear/glbf
done

mkdir ../anos_temp
mv ../???? ../anos_temp
mv anos/* ../
rm -r anos
ls ../????/glbf/h*glx > exme.gdl
rm -r ../????
mv ../anos_temp/* ../

\rm globk_rep.log globk_rep.org
glred 6 globk_rep.prt globk_rep.log exme.gdl globk_long.cmd
grep 'POS STAT' *.org > estadisticas.txt
sh_plot_pos -f globk_rep.org -r -t RATE -t1 $ano1 -t2 $ano2 -u -k
\rm globk_vel.log globk_vel.org
globk 6 globk_vel.prt globk_vel.log exme.gdl globk_long.cmd VEL
sh_exglk -f globk_vel.org -vel velo.vel
sh_plotvel -ps exme -f globk_vel.org -R240/275/10/35 -factor 0.5 -arrow_value 10 -page L
cd ..
./ejecutar.sh
cd vsoln
mv exme.ps ../
mv *.ps ../series
rm -r *.pos
rm -r globk_rep.org
cd ..

modelo=$(sed -n 12p parametros.txt)
new_resultado=${modelo:0:-4}_$(sed -n 8p parametros.txt)_$(sed -n 6p parametros.txt)_${ano1:0:4}_${ano2:0:4}
rm -r resultados_g/$new_resultado
mkdir resultados_g
mkdir resultados_g/$new_resultado
mkdir resultados_g/$new_resultado/series
mkdir resultados_g/$new_resultado/vsoln
mkdir resultados_g/$new_resultado/datos
mkdir resultados_g/$new_resultado/graficas
mv series/* resultados_g/$new_resultado/series
mv vsoln/* resultados_g/$new_resultado/vsoln
mv datos/* resultados_g/$new_resultado/datos
mv graficas/* resultados_g/$new_resultado/graficas
mv exme.ps resultados_g/$new_resultado

#cp separar_estadisticas.py resultados/$new_resultado
#cp separar_posvel.py resultados/$new_resultado
#cp ejecutar.sh resultados/$new_resultado
