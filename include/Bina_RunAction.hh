#ifndef Bina_RunAction_h
#define Bina_RunAction_h 1

#include "G4UserRunAction.hh"
#include "G4Accumulable.hh"
#include "globals.hh"

class G4Run;

class Bina_RunAction : public G4UserRunAction
{
  public:
    Bina_RunAction();
    virtual ~Bina_RunAction();

    virtual void   BeginOfRunAction(const G4Run*);
    virtual void   EndOfRunAction(const G4Run*);
    double time1;
//  private:

};

#endif
