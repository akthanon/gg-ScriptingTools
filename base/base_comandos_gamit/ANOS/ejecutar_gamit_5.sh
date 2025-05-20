carpeta=${PWD##*/}
carpeta=${carpeta:0:4}
for j in {121..150..1}; do
	sh_gamit -expt exme -d $carpeta ${j} -pres ELEV -orbit IGSF -copt x k p -dopts c ao
done