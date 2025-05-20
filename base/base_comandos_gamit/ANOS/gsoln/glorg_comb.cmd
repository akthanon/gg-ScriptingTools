* Glorg command file for daily repeatabilities or combinations  

* Last edited by rwk 130701
    
* Parameters to be estimated                                             
 pos_org  xtran ytran ztran xrot yrot zrot 
#   or if translation-only
x pos_org xtran ytran ztran

* Downweight of height relative to horizontal (default is 10)
#   Heavy downweight if reference frame robust and heights suspect
x  cnd_hgt  1000    
 
* Controls for removing sites from the stabilization 
#   Vary these to make the stabilization more robust or more precise                                             
 stab_it 4 0.8 3.0
x stab_it 4 0.5 4.0                                      
   
* A priori coordinates
#  ITRF2008 may be replaced by an apr file from a priori velocity solution         
 apr_file ~/gg/tables/itrf14_noam08.apr
x apr_file ../../tables/regional.apr
 
* List of stabilization sites
#   This should match the well-determined sites in the apr_file
 stab_site clear
x source ~/gg/tables/igb08_hierarchy.stab_site
 source ../../tables/regional_stab_site


                              



