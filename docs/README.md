# BINA SIMULATION v3.01a

~~It isn't main branch~~. App provides 3-body breakup simulation with (SSA) (others rections in previous version v2.11)

## INSTALLATION

### building pragram

- `mkdir build`
- `cmake -DGeant4_Dir=<path to geant4 install dir> ../`
- `make -j<threads>`

## RUN

### pluto
- `root .l pluto.mac (need to set pluto_path) `
- `./pluto_convert`
- `./bina_run`

or

- `auto`

### SSA(\param/gen 1)

- just `./bina_run`


## Params

Main parameters can be found in geo.mac
