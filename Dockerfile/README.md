# Bina-detector Dockerfile

## Usage

Download container (Building image instructions can be found [here](https://github.com/aszadzinski/dockerfiles/tree/master/physics-simulations/mc-sim)):

`docker pull aszadzinski/mc-sim:v1.0b`

Edit 'run.sh' and 'run.mac' file in `.../Dockerfile/ToPublic`

Execute simulation:

`docker run -v <full_path>/Bina-detector/Dockerfile/ToPublic/:/root/Public/ -it aszadzinski/mc-sim:v1.0b bash`

`[Docker_container] $: sh init.sh`



` ..../Dockerfile/ToPublic/build` folder contains all simulation outputs.
