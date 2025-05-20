separador=" : "
direc=(esta_10_2014_noam esta_15_2014_noam esta_20_2014_noam esta_5_2014_noam esta_break_2014_noam esta_dist_2014_noam esta_medi_2014_noam esta_wrms_10_noam IGS08.apr itrf00.apr itrf00_noam.apr itrf00_pcfc.apr itrf05.apr itrf05_noam.apr itrf05_pcfc.apr itrf08.apr itrf08_comb_na12.apr itrf08_comb_noam.apr itrf08_comb_pcfc.apr itrf08_noam.apr itrf08_pcfc.apr itrf14.apr itrf14_comb_na12.apr itrf14_comb_noam.apr itrf14_comb_pcfc.apr itrf14_na12.apr itrf14_noam08.apr itrf14_noam.apr itrf14_pcfc08.apr)
ruta="$(pwd) "

for j in {0..28..1}; do
	cd ${direc[j]}
	./ejecutar.sh
	cd ..
done
cd $ruta
echo "MODELO	ID	NWRMS	EWRMS	UWRMS	NNRMS	ENRMS	UNRMS"
grep 'ACAP' */datos/rms.txt
grep 'ALBH' */datos/rms.txt
grep 'ALGO' */datos/rms.txt
grep 'AMC2' */datos/rms.txt
grep 'AZCO' */datos/rms.txt
grep 'BRMU' */datos/rms.txt
grep 'CAM2' */datos/rms.txt
grep 'CAYA' */datos/rms.txt
grep 'CHET' */datos/rms.txt
grep 'CIC1' */datos/rms.txt
grep 'CICE' */datos/rms.txt
grep 'CNC0' */datos/rms.txt
grep 'COL2' */datos/rms.txt
grep 'COOB' */datos/rms.txt
grep 'COYU' */datos/rms.txt
grep 'CPDP' */datos/rms.txt
grep 'CRIP' */datos/rms.txt
grep 'CULI' */datos/rms.txt
grep 'DAEX' */datos/rms.txt
grep 'DOAR' */datos/rms.txt
grep 'DRAO' */datos/rms.txt
grep 'DUBO' */datos/rms.txt
grep 'FARO' */datos/rms.txt
grep 'FLIN' */datos/rms.txt
grep 'GODE' */datos/rms.txt
grep 'GOL2' */datos/rms.txt
grep 'GOLD' */datos/rms.txt
grep 'HER2' */datos/rms.txt
grep 'HOLB' */datos/rms.txt
grep 'ICAM' */datos/rms.txt
grep 'IGUA' */datos/rms.txt
grep 'INEG' */datos/rms.txt
grep 'IPAZ' */datos/rms.txt
grep 'JPLM' */datos/rms.txt
grep 'LPAZ' */datos/rms.txt
grep 'MDO1' */datos/rms.txt
grep 'MERI' */datos/rms.txt
grep 'MEXI' */datos/rms.txt
grep 'MMD1' */datos/rms.txt
grep 'MMX1' */datos/rms.txt
grep 'MONP' */datos/rms.txt
grep 'MPR1' */datos/rms.txt
grep 'MSD1' */datos/rms.txt
grep 'MTY2' */datos/rms.txt
grep 'NANO' */datos/rms.txt
grep 'NLIB' */datos/rms.txt
grep 'OAX2' */datos/rms.txt
grep 'OAXA' */datos/rms.txt
grep 'OXEC' */datos/rms.txt
grep 'OXLP' */datos/rms.txt
grep 'OXMC' */datos/rms.txt
grep 'OXPE' */datos/rms.txt
grep 'OXTH' */datos/rms.txt
grep 'OXTU' */datos/rms.txt
grep 'PIE1' */datos/rms.txt
grep 'PINO' */datos/rms.txt
grep 'POPN' */datos/rms.txt
grep 'POSW' */datos/rms.txt
grep 'PRDS' */datos/rms.txt
grep 'PSTX' */datos/rms.txt
grep 'PTAX' */datos/rms.txt
grep 'PTEX' */datos/rms.txt
grep 'PURI' */datos/rms.txt
grep 'QUEX' */datos/rms.txt
grep 'SA27' */datos/rms.txt
grep 'SA33' */datos/rms.txt
grep 'SG21' */datos/rms.txt
grep 'SPMX' */datos/rms.txt
grep 'TAMP' */datos/rms.txt
grep 'TGMX' */datos/rms.txt
grep 'TNAM' */datos/rms.txt
grep 'TNCN' */datos/rms.txt
grep 'TNMO' */datos/rms.txt
grep 'TNTB' */datos/rms.txt
grep 'TOL2' */datos/rms.txt
grep 'UCOE' */datos/rms.txt
grep 'UNIP' */datos/rms.txt
grep 'UNPM' */datos/rms.txt
grep 'USMX' */datos/rms.txt
grep 'UTON' */datos/rms.txt
grep 'VNDP' */datos/rms.txt
grep 'WILL' */datos/rms.txt
grep 'YAIG' */datos/rms.txt
grep 'YESX' */datos/rms.txt
grep 'ZIHP' */datos/rms.txt

for j in {0..28..1}; do
	cd ${direc[j]}
	echo ""
	echo ""
	echo ${direc[j]}
	cat datos/rms.txt
	cd ..
done