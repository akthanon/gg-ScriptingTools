* GLOBK command file for multiyear times series and velocity solution from combination h-files   

* For velocity, set VEL as a globk command-line option; since these commands
* follow the commands for repeatabilities, they will take precedence when invoked.

* Lasted edited 130701

* << column 1 must be blank if not comment >>    
            
* This group of commands must appear before any others:           
# The @ wildcard sets the name of the file to be the same as the gdl file                          
VEL com_file @.com                                                
 srt_file @.srt 
 srt_dir +1
 eq_file ~/gg/tables/itrf14_comb.eq 
# Optionally add a second eq_file for analysis-specific renames 
* End commands that must appear first
 eq_file valeq_file.eq

* Sites to include in the solution (default is all)
use_site -nayx -nvlx -oxp2 -pop1 -pb2y -sa61 -tnal -tnba -tncm -tncu -tnhm -tnmr -tnms -tnxx -tnpj -uigf -cn25 -cn24 -oxum -oxgu -tnnp -tncy
use_site -oxpl -tnmq -tnif -tncc -ugeo -pena -tnpc -mnzo -tnlc -rayn -sa50 -plpx -pltx -msx1 -phjx -pb1y -pjzx -palx -pin1 -teco -tnnx -tnat
use_site -morr -uxal -uagu -ucoc -pp04 -pp02 -pp03 -pp01 -pp05 -tngf -cecm -cega -moit -tsfx -tntl -tntm -nvdo -tnpp -cols -oxte -plcx -guax
use_site -pclx -tnct -cn26 -tnmz -tnmt -iagx -utac -uira -cefa -tnsl -corx -unva -unle -unto -yumx -ujur -tnza -utic -tnts -utul -lpig -spig
use_site -mxs1 -ujal -mxas -mrra -tncs -ufxn -pzul -ucom -tnsj
* Solution file pointed to by the com file, if used
VEL sol_file @.sol 

* ITRF2008 augmented by now-defunct sites and recent IGS solutions;
* matched to itrf08_comb.eq 
 apr_file ~/gg/tables/itrf14_noam08.apr
# Optionally add additional apr files for other sites
 
* Set maximum chi2, prefit coordinate difference (m), and rotation (mas) for an h-file to be used;
 max_chii 13 3 100  
# increase tolerances to include all files for diagnostics
x  max_chi  100  5.0 20000 

# Do not used an a priori rotation file with multi-day H-files
x in_pmu ../tables/pmu.usno        

* Invoke glorg
 org_cmd glorg_long.cmd

* Print file options    
 crt_opt NOPR
 prt_opt NOPR GDLF CMDS                                                
 org_opt PSUM CMDS GDLF FIXA RNRP  
VEL org_opt ERAS PSUM CMDS GDLF VSUM FIXA RNRP 
# Set an explicit name for the glorg print file; otherwise will use the
# globk print file name from the globk command line   
 org_out globk_rep.org                                         
VEL org_out globk_vel.org    
                                        
* Coordinate parameters to be estimated and a priori constraints
 apr_neu  all 10 10 10  0 0 0    
VEL apr_neu  all 10 10 10  1 1 1 

* Rotation parameters to be estimated and a priori constraints 
 apr_wob  10 10 0 0     
 apr_ut1  10 0   
VEL apr_wob  10 10 10 10    
VEL apr_ut1  10 10        
VEL mar_wob    3650 3650  0 0 
VEL mar_ut1    365 0 
# EOP tight if tanslation-only stabilization in glorg (also comment out mar_wob, mar_ut1)
x apr_wob .25 .25 .1 .1 
x apr ut1 .25 .1                                  
 
# Allow translation and scale variations for pre-1995 data and
# for data analyses that feature a a change in SV PCVs (e.g. 
# operational, pre-repro1 MIT or SOPAC h-files before Week 1400, Nov 2006)
x apr_tran 1 1 1 0 0 0 
xVEL apr_tran 1 1 1 1 1 1
xVEL mar_tran   3.65  3.65  3.65     0  0  0
x apr_scale 10 0
xVEL apr_scale 10 1.
xVEL mar_scale  365   0     
                                   
* Optionally put a uselist and/or sig_neu and mar_neu reweight in a source file           
x  source ../tables/uselist       
x  source ../tables/monthly_reweights

* Remove scracth files for repeatability runs
  del_scra yes
VEL del_scra no
