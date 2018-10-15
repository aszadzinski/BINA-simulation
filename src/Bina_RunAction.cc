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

//....oooOO0OOooo........oooOO0OOooo........oooOO0OOooo........oooOO0OOooo......

Bina_RunAction::Bina_RunAction()
: G4UserRunAction()//,
//  fEdep(0.),
//  fEdep2(0.)
{

}

Bina_RunAction::~Bina_RunAction()
{}

void Bina_RunAction::BeginOfRunAction(const G4Run*)
{
G4cout<<"TEST";
}

void Bina_RunAction::EndOfRunAction(const G4Run* run)
{


}
