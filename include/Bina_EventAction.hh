
#ifndef Bina_EventAction_h
#define Bina_EventAction_h 1

#include "G4UserEventAction.hh"
#include "globals.hh"
#include <omp.h>

struct MyOMP;

class Bina_EventAction : public G4UserEventAction
{
        public:
        Bina_EventAction(MyOMP*);
        virtual ~Bina_EventAction();

public:
        virtual void BeginOfEventAction(const G4Event*);
        //virtual void   EndOfEventAction(const G4Event*);
        MyOMP* mp;

inline static int getNb(int num = -1 )
{
        static int temp;
        if (num != -1) temp = num;
        return temp;
};
};
#endif
