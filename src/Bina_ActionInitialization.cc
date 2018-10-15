#include "Bina_ActionInitialization.hh"
#include "Bina_PrimaryGeneratorAction.hh"
#include "Bina_RunAction.hh"
#include "Bina_EventAction.hh"
#include "Bina_SteppingAction.hh"

Bina_ActionInitialization::Bina_ActionInitialization() : G4VUserActionInitialization(){}


Bina_ActionInitialization::~Bina_ActionInitialization(){}


void Bina_ActionInitialization::BuildForMaster() const
{
//  Bina_RunAction* runAction = new Bina_RunAction;
//  SetUserAction(runAction);
}


void Bina_ActionInitialization::Build() const
{
//  SetUserAction(new Bina_PrimaryGeneratorAction);

//  Bina_RunAction* runAction = new Bina_RunAction;
  //SetUserAction(runAction);

  //Bina_EventAction* eventAction = new Bina_EventAction(runAction);
//  SetUserAction(eventAction);

  //SetUserAction(new Bina_SteppingAction(eventAction));
}
