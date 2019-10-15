FROM aszadzinski/geant4-multithreading:v1.0

RUN pacman -Syu --noconfirm

RUN pacman -S wget awk grep filesystem cmake make vim gcc kdelibs4support git  xorg-server libglvnd libx11 root --noconfirm

WORKDIR /root/

RUN	wget https://plutouser.github.io/v6.01/pluto_v6.01.tar.gz \
	&& tar xvf pluto_v6.01.tar.gz \
	&& rm pluto_v6.01.tar.gz \
	&& mkdir pluto_v6.01/build \
	&& cd /root/pluto_v6.01/build \
	&& cmake ../ . \
	&& make -j4 \
&& cd /root/ 
