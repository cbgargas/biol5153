#! /bin/bash
#concatenates bacteria archaea seqs from each filtering for use in 
#plotting and otu clustering


cat /home/cory/projects/bacteria-diatom-16s/data/tol_rrna/2019-02-26_output_all/*/*.bacteria.fa > cat-all.fa;

cat /home/cory/projects/bacteria-diatom-16s/data/tol_rrna/2019-02-26_output_all/*/*.archaea.fa >> cat-all.fa;

cat /home/cory/projects/bacteria-diatom-16s/data/tol_rrna/2019-02-26_output_250bp/*/*.bacteria.fa > cat-250bp.fa;

cat /home/cory/projects/bacteria-diatom-16s/data/tol_rrna/2019-02-26_output_250bp/*/*.archaea.fa >> cat-250bp.fa;

cat /home/cory/projects/bacteria-diatom-16s/data/tol_rrna/2019-02-27_output_500bp/*/*.bacteria.fa > cat-500bp.fa;

cat /home/cory/projects/bacteria-diatom-16s/data/tol_rrna/2019-02-27_output_500bp/*/*.archaea.fa >> cat-500bp.fa;


