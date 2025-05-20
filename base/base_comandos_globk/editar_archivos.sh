esta=$(sed -n 10p parametros.txt)
nesta=$(sed -n 6p parametros.txt)
model=$(sed -n 12p parametros.txt)
elim=$(sed -n 14p parametros.txt)
let nesta=$nesta*5
echo "* Stabilisation list for example 
 stab_site clear 
 stab_site "${esta:0:nesta}"" > tables/regional_stab_site

echo "* Glorg command file for multi-year time series and velocity solution

* For velocity, set VEL as a globk or glorg command-line option

* Last edited by rwk 130707

* << column 1 must be blank if not comment >>
 
* Parameters to be estimated                                             
 pos_org  xtran ytran ztran xrot yrot zrot
VEL rate_org  xtran ytran ztran xrot yrot zrot 
# Optionally, if estimated scale in GLOBK:
x pos_org xtran ytran ztran xrot yrot zrot scale

#   or if translation-only
x pos_org xtran ytran ztran
xVEL rate_org xtran ytran ztran

* Downweight of height relative to horizontal (default is 10 10)
#   Heavy downweight if reference frame robust and heights suspect
x  cnd_hgt  1000 1000  
 
* Controls for removing sites from the stabilization 
#   Vary these to make the stabilization more robust or more precise                                             
 stab_it 4 0.8 3.0
x stab_it 4 0.5 4.0                                      
   
* A priori coordinates to define the analysis reference frame        
 apr_file ~/gg/tables/"${model}"
# Use a regional stablization if available from a prior solution (comment out the itrf08 file)
x apr_file ../tables/regional.apr

* List of stabilization sites
#   This should match the well-determined sites in the apr_file
 stab_site clear
x source ~/gg/tables/igb08_hierarchy.stab_site
# Use a regional stabililization if available from a prior solution
 source ../tables/regional_stab_site
  
* Estimate rotation (Euler) vectors to be used with sh_org2vel to
* to rotate the solution to a block- or region-specific reference frame
xVEL plate eurasia kosg_2ps onsa_2ps nyal_4ps graz_2ps tlse_2ps kit3_2ps
xVEL plate eurasia vill_3ps mars_3ps cbre
xVEL plate weura kosg_2ps tlse_2ps vill_3ps mars_3ps 
xVEL plate aegean milo kyra xris dioa leon mkn2 bodr roml omal koun seva   
xVEL# Constrain the center-of-mass to the apr-file in plate estimate (comment out for global solutions)
xVEL NOPLATETRAN

* Equate the velocities of co-located sites
VEL eq_dist 1000 ndot
VEL eq_dist 1000 edot
VEL eq_dist 1000 udot
 
* Equate a few horizontal velocities for sites farther apart
VEL equate trab_gps ndot akto_gps ndot
VEL equate trab_gps edot akto_gps edot
   
* Unequate velocities that are incompatible
VEL unequate mad2_gps ndot
VEL unequate mad2_gps edot
VEL unequate mad2_gps udot
 
 



                              


"> glorg_long.cmd

echo "* GLOBK command file for multiyear times series and velocity solution from combination h-files   

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
"${elim}"
* Solution file pointed to by the com file, if used
VEL sol_file @.sol 

* ITRF2008 augmented by now-defunct sites and recent IGS solutions;
* matched to itrf08_comb.eq 
 apr_file ~/gg/tables/"${model}"
# Optionally add additional apr files for other sites
 
* Set maximum chi2, prefit coordinate difference (m), and rotation (mas) for an h-file to be used;
 max_chii 13 3 100  
# increase tolerances to include all files for diagnostics
x  max_chi  10000000  50000000.0 20000000 

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
VEL del_scra no">globk_long.cmd
