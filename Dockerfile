FROM archlinux/base

RUN pacman -Syu --noconfirm

RUN pacman -S filesystem cmake make vim gcc kdelibs4support  xorg-server libglvnd libx11  --noconfirm

WORKDIR /root/

RUN mkdir geant4
RUN mkdir geant4-install
RUN mkdir geant4-build

COPY geant4.10.05/  geant4/
WORKDIR /root/geant4-build

RUN cmake -DCMAKE_INSTALL_PREFIX=/root/geant4-install -DGEANT4_INSTALL_DATA=ON -DGEANT4_BUILD_MULTITHREADED=ON -DGEANT4_USE_OPENGL_X11=ON /root/geant4

RUN make -j6
RUN make install
WORKDIR /root/
RUN mkdir BINA-build

COPY run .
CMD ./run
