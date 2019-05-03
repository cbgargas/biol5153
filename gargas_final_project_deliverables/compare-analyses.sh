#! /bin/bash
#creates a .sh script to create a file containing the # of sequences of the different ssu-align analyses';

touch compare-analyses.txt;
echo Archaea_all > compare-analyses.txt;
grep -c ">" 2019-02-26_output_all/archaea_all.fa >> compare-analyses.txt;  
echo Bacteria_all >> compare-analyses.txt;
grep -c ">" 2019-02-26_output_all/bacteria_all.fa >> compare-analyses.txt;
echo Archaea_250bp >> compare-analyses.txt;
grep -c ">" 2019-02-26_output_250bp/archaea_250bp.fa >> compare-analyses.txt;
echo Bacteria_250bp >> compare-analyses.txt;
grep -c ">" 2019-02-26_output_250bp/bacteria_250bp.fa >> compare-analyses.txt;
echo Archaea_500bp >> compare-analyses.txt;
grep -c ">" 2019-02-27_output_500bp/archaea_500bp.fa >> compare-analyses.txt;
echo Bacteria_500bp >> compare-analyses.txt;
grep -c ">" 2019-02-27_output_500bp/bacteria_500bp.fa >> compare-analyses.txt;