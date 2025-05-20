./base_checar.sh > ejecutar_gamit_F.sh
chmod +x ejecutar_gamit_F.sh

echo "FALTANTES"
cat ejecutar_gamit_F.sh | wc -l
echo "ERRORES"
ls ???/GAMIT.fatal > fatalitys.txt
grep "FATAL  :" ???/GAMIT.fatal > fatalitys_detallado.txt
cat fatalitys.txt | wc -l