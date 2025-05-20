rm -r datos
grep 'stats' vsoln/*.orbit.res > estadisticas.txt
grep 'POS STAT' vsoln/globk_rep.org > posiciones.txt
ls vsoln/*.res > lista.txt

python3 separar_estadisticas.py > rms.txt
python3 separar_posvel.py > rmsposvel.txt

mkdir datos
mv rms.txt datos
mv rmsposvel.txt datos

python3 graficas_globk_particular.py

rm estadisticas.txt
rm posiciones.txt
rm lista.txt
