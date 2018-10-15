#ifndef Bina_ActionInitialization_h
#define Bina_ActionInitialization_h 1

#include "G4VUserActionInitialization.hh"

/// Action initialization class.

class Bina_ActionInitialization : public G4VUserActionInitialization
{
  public:
    Bina_ActionInitialization();
    virtual ~Bina_ActionInitialization();

    virtual void BuildForMaster() const;
    virtual void Build() const;
};

#endif
