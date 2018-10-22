#include "Bina_ActionInitialization.hh"
#include "Bina_PrimaryGeneratorAction.hh"
#include "Bina_RunAction.hh"
#include "Bina_EventAction.hh"
#include "Bina_SteppingAction.hh"
#include "Bina_DetectorConstruction.hh"
#include "Bina_PhysicsList.hh"

Bina_ActionInitialization::Bina_ActionInitialization(Bina_DetectorConstruction* DC, Bina_PhysicsList* Physics) : G4VUserActionInitialization()
{

  myDC = DC;
  myPhysics = Physics;
}


void Bina_ActionInitialization::Build() const
{
  SetUserAction(new Bina_PrimaryGeneratorAction(myDC));
  SetUserAction(new Bina_EventAction);
  SetUserAction(new Bina_RunAction);
  SetUserAction(new Bina_SteppingAction(myPhysics));
}
