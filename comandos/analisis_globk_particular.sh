rm -r datos
grep 'stats' vsoln/*.orbit.res > estadisticas.txt
grep 'POS STAT' vsoln/*.org > posiciones.txt
grep 'VEL STAT' vsoln/*.org > velocidades.txt
ls vsoln/*.res > lista.txt

python3 separar_estadisticas.py > rms.txt
python3 separar_posvel.py > rmsposvel.txt

mkdir datos
mv rms.txt datos
mv rmsposvel.txt datos

rm estadisticas.txt
rm posiciones.txt
rm velocidades.txt
rm lista.txt
