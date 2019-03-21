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
#include "G4Threading.hh" 
#include<string>
#include <fstream>
#include <omp.h>

Bina_RunAction::Bina_RunAction() : G4UserRunAction()
{;}

Bina_RunAction::~Bina_RunAction()
{
}

void Bina_RunAction::BeginOfRunAction(const G4Run*)
{
        time1 = omp_get_wtime();
	G4cout<<"t1= "<< time1<<G4endl;
}

void Bina_RunAction::EndOfRunAction(const G4Run* run)
{
        time2 = omp_get_wtime();
	float time3 = time2-time1;
       	G4cout<<"RA= "<<time3<<G4endl;

	std::string tid = std::to_string(G4Threading::G4GetThreadId()) + ".txt";

    std::fstream file;
    file.open(tid, std::ios::out | std::ios::app);
    if( file.good() == true )
    {
	    
	    file << time3;
	    file<<"\n";
        file.close();
    }
}
