#ifndef Bina_ActionInitialization_h
#define Bina_ActionInitialization_h 1

#include "G4VUserActionInitialization.hh"
#include "Bina_DetectorConstruction.hh"
#include "Bina_PhysicsList.hh"

/// Action initialization class.
struct MyOMP;
class Bina_ActionInitialization : public G4VUserActionInitialization
{
public:
Bina_ActionInitialization(Bina_DetectorConstruction*, Bina_PhysicsList*, MyOMP*);

Bina_DetectorConstruction*  myDC;
Bina_PhysicsList*           myPhysics;
MyOMP*                      mp;

virtual void Build() const;
};
#endif
