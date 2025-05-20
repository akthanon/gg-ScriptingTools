* GLOBK command file to generate daily time series and to combine 
* h-files over 2 to 30 days.  

* For combination, set COMB as a globk command-line option to
* invoke the saving of the output h-file

* Last edited by rwk 150618

* << column 1 must be blank if not comment >>    
            
* This group of commands must appear before any others:                                                       
 srt_file @.srt 
 srt_dir +1
 eq_file ~/gg/tables/itrf08_comb.eq 
# Optionally add a second eq_file for analysis-specific renames 
* End commands that must appear first

* ITRF2008 augmented by now-defunct sites and recent IGS solutions;
# matched to itrf08_comb.eq 
 apr_file ~/gg/tables/itrf14_noam08.apr
# Optionally add additional apr files for other sites
x apr_file ../../tables/regional.apr 
 
* Set maximum chi2 and prefit coordinate difference (m),for an h-file to be used;
 max_chii 13 3  
# increase tolerances to include all files for diagnostics
x  max_chi  100  5.0  

# Not necessary unless combining h-files with different a priori EOP
 in_pmu ../tables/pmu.usno        

* Invoke glorg
 org_cmd glorg_comb.cmd

* Print file options    
 crt_opt NOPR
 prt_opt NOPR GDLF CMDS MIDP
 org_opt PSUM CMDS GDLF MIDP FIXA RNRP  
# sh_glred will name the glorg print files 
x org_out globk_comb.org                                         
                                       
* Coordinate parameters to be estimated and a priori constraints
 apr_neu  all 10 10 10  0 0 0    

* Rotation parameters to be estimated and a priori constraints 
x apr_wob  10 10 0 0     
x apr_ut1  10 0   
# If combining with global h-files, allow EOPS to change 
# between days
x mar_wob 3650 3650 365 365
x mar_ut1 365  365 
# EOP tight if translation-only stabilization in glorg 
 apr_wob .25 .25 .1 .1 
 apr ut1 .25 .1                                  
 
* Write out a combined H-file
# Can substitute your analysis name for 'COMB' in the file name below
COMB out_glb  H------_COMB.GLX 
              
* Optionally put a uselist and/or sig_neu and mar_neu reweight in a source file           
x  source ../tables/uselist       
x  source ../tables/daily_reweights

* Turn off quake log estimates if in the eq_file
 free_log -1
 
* Remove scratch files for repeatability runs
  del_scra yes

* Correct the pole tide when not compatible with GAMIT
  app_ptid all 
* If orbits free in GAMIT (RELAX) and you want them fixed, use:
x  apr_svs all F F F F F F FR 
* but if you are combining with globk h-files, better to leave them
* on but, if the models are incompatible, turn off radiation-pressure parameters,
x apr_svs all 100 100 100 10 10 10 0R  
  

* When using MIT GLX files which have satellite phase center positions 
* estimated use:
  apr_svan all  F F F     ! Fix antenna offset to IGS apriori values.




