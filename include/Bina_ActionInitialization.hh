#ifndef Bina_ActionInitialization_h
#define Bina_ActionInitialization_h 1

#include "G4VUserActionInitialization.hh"
#include "Bina_DetectorConstruction.hh"
#include "Bina_PhysicsList.hh"
/// Action initialization class.

class Bina_ActionInitialization : public G4VUserActionInitialization
{
  public:
    Bina_ActionInitialization(Bina_DetectorConstruction*, Bina_PhysicsList*);

    Bina_DetectorConstruction* myDC;
    Bina_PhysicsList* myPhysics;
    virtual void Build() const;
};

#endif
