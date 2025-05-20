* Glorg command file for multi-year time series and velocity solution

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
 apr_file ~/gg/tables/itrf14_comb_noam.apr
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
 
 



                              



