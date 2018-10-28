#include "Bina_RunAction.hh"
#include "Bina_PrimaryGeneratorAction.hh"
#include "Bina_DetectorConstruction.hh"

#include "G4RunManager.hh"
#include "G4Run.hh"
#include "G4AccumulableManager.hh"
#include "G4LogicalVolumeStore.hh"
#include "G4LogicalVolume.hh"
#include "G4UnitsTable.hh"
#include "G4SystemOfUnits.hh"

#include <omp.h>


Bina_RunAction::Bina_RunAction() : G4UserRunAction()
{;}

Bina_RunAction::~Bina_RunAction()
{
}

void Bina_RunAction::BeginOfRunAction(const G4Run*)
{
        time1 = omp_get_wtime();
}

void Bina_RunAction::EndOfRunAction(const G4Run* run)
{
        G4cout<<"RA= "<<omp_get_wtime()-time1<<G4endl;
}
