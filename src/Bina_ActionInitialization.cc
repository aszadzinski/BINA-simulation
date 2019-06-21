#include "Bina_ActionInitialization.hh"
#include "Bina_PrimaryGeneratorAction.hh"
#include "Bina_RunAction.hh"
#include "Bina_EventAction.hh"
#include "Bina_SteppingAction.hh"
#include "Bina_DetectorConstruction.hh"
#include "Bina_PhysicsList.hh"
//#include "features.hh"

Bina_ActionInitialization::Bina_ActionInitialization(Bina_DetectorConstruction* mDC, Bina_PhysicsList* Physics) : G4VUserActionInitialization()
{
    myDC = mDC;
    myPhysics = Physics;
}

void Bina_ActionInitialization::Build() const
{
    bool rt = true;
    Bina_EventAction* Evt = new Bina_EventAction(rt);
    SetUserAction(new Bina_PrimaryGeneratorAction(myDC));
    SetUserAction(Evt);
    SetUserAction(new Bina_RunAction(rt));
    SetUserAction(new Bina_SteppingAction(myPhysics,Evt,rt));
}
