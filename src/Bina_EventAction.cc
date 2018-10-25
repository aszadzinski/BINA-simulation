#include "Bina_EventAction.hh"

//#include "Bina_CalorHit.hh"
//#include "Bina_EventActionMessenger.hh"

#include "G4Event.hh"
#include "G4EventManager.hh"
#include "G4HCofThisEvent.hh"
#include "G4VHitsCollection.hh"
#include "G4TrajectoryContainer.hh"
#include "G4Trajectory.hh"
#include "G4VVisManager.hh"
#include "G4SDManager.hh"
#include "G4UImanager.hh"
#include "G4ios.hh"
#include "G4UnitsTable.hh"

//#include <omp.h>
//#include <unistd.h>

Bina_EventAction::Bina_EventAction(bool en_omp)
{
        enable_omp = en_omp;
}

Bina_EventAction::~Bina_EventAction()
{
        ;
}

void Bina_EventAction::BeginOfEventAction(const G4Event* evt)
{
        G4int evtNb = evt->GetEventID();
        getNb(evtNb);
        if (!(evtNb%100))
        {
                if(enable_omp)
                {
                        G4cout<<"(omp)";
                }
                G4cout << "\n--> Begin of event: " << evtNb <<G4endl;
        }
}

/*
void Bina_EventAction::EndOfEventAction(const G4Event* evt)
{

        NOTE G4cout outputs mix each other

        G4int evtNb = evt->GetEventID();
        getNb(evtNb);
        const int unitime=100000;
        if (!(evtNb%100))
        {
                #pragma omp parallel
                {
                        #pragma omp for schedule(dynamic,2)
                for(int i=0;i<20;i++)
                {
                G4cout << " Thread:"<<omp_get_thread_num()<<" i="<<i<<G4endl;
                usleep(unitime);
                }
                }
        }
}
*/
