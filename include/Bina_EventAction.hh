
#ifndef Bina_EventAction_h
#define Bina_EventAction_h 1

#include "G4UserEventAction.hh"
#include "globals.hh"
#include <omp.h>

class Bina_EventAction : public G4UserEventAction
{
public:
        Bina_EventAction(bool);
        virtual ~Bina_EventAction();
public:
        virtual void   BeginOfEventAction(const G4Event*);
        //virtual void   EndOfEventAction(const G4Event*);
        bool enable_omp;
inline static int getNb(int num = -1 )
{
        static int temp;
        if (num != -1) temp = num;
        return temp;
};
};


#endif
