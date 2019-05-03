#! /bin/bash

echo '#! /bin/bash' > ssu-align_ttol-cmds.sh  
echo '#generates .sh file of ssu-align commands for the ttol_rrna data' >> ssu-align_ttol-cmds.sh 

for file in /home/cory/projects/bacteria-diatom-16s/data/tol_rrna/*.fa  
 
do   
 
echo ssu-align -l 500 $file $(basename "${file%.fa}")";" >> ssu-align_ttol-cmds.sh  
        #-l 250 tells ssu-align to filter out sequences below 250 nucleotides  
done

chmod u+x ssu-align_ttol-cmds.sh 
		#makes ssu-align_ttol-cmds.sh executable w/o having to mess around
