#ifndef Bina_ActionInitialization_h
#define Bina_ActionInitialization_h 1

#include "G4VUserActionInitialization.hh"
#include "Bina_DetectorConstruction.hh"
#include "Bina_PhysicsList.hh"

class Bina_ActionInitialization : public G4VUserActionInitialization
{
	public:
		Bina_ActionInitialization(Bina_DetectorConstruction*, Bina_PhysicsList*);
		virtual void Build() const;
		Bina_DetectorConstruction*  myDC;
		Bina_PhysicsList*           myPhysics;

	private:


};
#endif
