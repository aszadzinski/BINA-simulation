echo "Executing run.sh..."

#Edit this line if you're using own source code
git clone https://github.com/aszadzinski/BINA-detector.git

# Better keep unchanged
mkdir /root/Public/build
source geant4-install/bin/geant4.sh
cd /root/Public/build

#Remember to change paths  
cmake -DGeant4_Dir= /root/geant4-install/lib64/Geant4-10.5.1 /root/BINA-detector/

make -j3


./bina_run /root/Public/run.mac

