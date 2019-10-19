# BINA SIMULATION v3.01a

~~It isn't main branch~~. Program provides 3-body breakup simulation with (SSA) (others rections in previous version v2.11)

## INSTALLATION

### Building program

- Setup Geant4 enviroment `$: source path_to_geant4_install_Dir/bin/geant4.sh`
- `$: mkdir build`
- `$: cmake -DGeant4_Dir=<path to geant4 install dir> ../`
- `$: make -j<threads>`

#### Downloading Docker container with Geant4

Download container (Building image instructions can be found [here](https://github.com/aszadzinski/dockerfiles/tree/master/physics-simulations/mc-sim)):

`docker pull aszadzinski/mc-sim:v1.0b`

---

## RUN

### Generating kinematics data using [Pluto](https://www-hades.gsi.de/?q=pluto)
- `$: root .l pluto.mac`

```cpp
//Remember to load pluto.so
gSystem->Load("path to pluto.so")
```

- `$: ./pluto_convert`
- Remember to setup `/param/gen 1` in 'geo.mac' before

### Execution

#### With Docker

Edit 'run.sh' and 'run.mac' file in `.../Dockerfile/ToPublic`.

Example of 'run.sh':
```bash
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
```

Execute simulation:

`$: docker run -v <full_path>/Bina-detector/Dockerfile/ToPublic/:/root/Public/ -it aszadzinski/mc-sim:v1.0b bash`

`[Docker_container] $: sh init.sh`

' ..../Dockerfile/ToPublic/build' folder contains all simulation outputs.

#### Classic way after local installation

`$: ./bina_run`

## Params

Main  parameters can be found in geo.mac

## Output files (TODO)


| Num |  .dat | .root |
| :---: | :---: | :---: |
| 0 | event | Y |
| 1 | particle ID | Y |
| 2 | MWPC-X | Y |
| 3 | MWPC-Y | Y |
| 4 | Theta | Y |
| 5 | Phi | Y |
| 6 | Energy0 | Y |
| 7 | Energy dep. | Y |
| 8 | x | Y |
| 9 | Detector number | Y |
| 10 | x | Y |
| 11 | pos:X | Y |
| 12| pos:Y | Y |
| 13 | pos:Z | Y |
| 14 | flag| Y |
| 15 | flag | Y |
| 16 | flag | Y |
