# $Id: GNUmakefile,v 1.2 2000/10/19 12:22:10 stanaka Exp $
# --------------------------------------------------------------
# GNUmakefile for examples module.  Gabriele Cosmo, 06/04/98.
# --------------------------------------------------------------

name := bina_breakup2.11
G4TARGET := $(name)
G4EXLIB := true

#ifndef G4INSTALL
#  G4INSTALL = /home/ja/geant4
#endif

.PHONY: all
all: lib bin

include $(G4INSTALL)/config/binmake.gmk

TEMP := ./bin

visclean:
	rm -f $(TEMP)/g4*.prim $(TEMP)/g4*.eps $(TEMP)/g4*.wrl
	rm -f $(TEMP)/.DAWN_*

