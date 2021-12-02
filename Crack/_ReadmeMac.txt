0. Run matlab setup from  "matlab_R2021b_maci64.dmg"  file

1. If you see login/password/signin form (installer has access to internet)
     then in upper right corner in  "Advanced Options"  select setup mode  "I have a File Installation Key"
     If internet access is absent then required setup mode will be auto-selected and you do not need to select in manually

2. When you will be asked to  "Enter File Installation Key"  enter
     62551-02011-26857-57509-64399-54230-13279-37181-62117-65158-40352-64197-45508-24369-45954-39446-39538-16936-10698-58393-44718-32560-10501-40058-34454

3. When you will be asked to  "Select License File"  select file  "license.lic"  from folder with Matlab911R2021b_Mac64.dmg file

4. When you will be asked to  "Select products"  select components you need
     If you all components are selected Matlab will need about 30Gb of disk space and somewhat longer startup time
     If you select only  "MATLAB"  then Matlab will need about  3Gb of disk space
     You better run Matlab from SSD disk for better startup time, so most likely you do not want to waste SSD-disk space for nothing

5. After installation is done copy file  "libmwlmgrimpl.dylib"  from folder with matlab_R2021b_maci64.dmg file
     to ALREADY EXISTING FOLDER  "<matlabfolder>\bin\maci64\matlab_startup_plugins\lmgrimpl"
     WITH OVERWRITING OF EXISTING FILE (<matlabfolder> - is where you installed Matlab, defaults to  "/Applications/Matlab_R2021b.app")

6. Work with Matlab :)


P.S.
During update/change of already working Matlab there is no need to execute step 3
Step 5 might be necessary to repeat (if during update/change of Matlab file  "libmwlmgrimpl.dylib"  was overwritten)
If after update/change you get error during startup of Matlab then first try to redo the step 5
