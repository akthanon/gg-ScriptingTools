can=1
eje=1
day=XXX
est=0
carpeta=${PWD##*/}
carpeta=${carpeta:0:4}
cont=0

while [ $eje -ne 0 ]
do
    clear
    ./checar.sh
    sleep 1m
    eje=$(wc -l < ejecutar_gamit_F.sh)
    can=$(wc -l < fatalitys.txt)
    cont=0
    if [ $can -gt 0 ]; then

        while IFS= read -r line; do
            est=$(printf '%s\n' "$line")
            est=${est:0:3}
            rm -r $est
            echo "Linea:    " $cont"/"${can}
            echo "Estacion: " $est
            sh_gamit -expt exme -d $carpeta $est -pres ELEV -orbit IGSF -copt x k p -dopts c ao
            cont=cont+1
        done < fatalitys.txt        
    fi
done


