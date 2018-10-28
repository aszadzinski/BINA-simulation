#ifdef G4VIS_USE

#include "Bina_VisManager.hh"

// Supported drivers...

// Not needing external packages or libraries...
#include "G4ASCIITree.hh"
#include "G4DAWNFILE.hh"
#include "G4HepRepFile.hh"
#include "G4HepRep.hh"
#include "G4RayTracer.hh"
#include "G4VRML1File.hh"
#include "G4VRML2File.hh"

// Needing external packages or libraries...

#ifdef G4VIS_USE_DAWN
#include "G4FukuiRenderer.hh"
#endif

//#ifdef G4VIS_USE_OPENGLX
#include "G4OpenGLImmediateX.hh"
//#include "G4OpenGLStoredX.hh"
//#endif

#ifdef G4VIS_USE_OIX
#include "G4OpenInventorX.hh"
#endif

#ifdef G4VIS_USE_OIWIN32
//#include "G4OpenInventorWin32.hh"
#endif

#ifdef G4VIS_USE_VRML
#include "G4VRML1.hh"
#include "G4VRML2.hh"
#endif

Bina_VisManager::Bina_VisManager () {
}

void Bina_VisManager::RegisterGraphicsSystems () {

// Graphics Systems not needing external packages or libraries...
        RegisterGraphicsSystem (new G4ASCIITree);
        RegisterGraphicsSystem (new G4DAWNFILE);
        RegisterGraphicsSystem (new G4HepRepFile);
        RegisterGraphicsSystem (new G4HepRep);
        RegisterGraphicsSystem (new G4RayTracer);
        RegisterGraphicsSystem (new G4VRML1File);
        RegisterGraphicsSystem (new G4VRML2File);
// Graphics systems needing external packages or libraries...

#ifdef G4VIS_USE_DAWN
        RegisterGraphicsSystem (new G4FukuiRenderer);
#endif

#ifdef G4VIS_USE_OPACS
        RegisterGraphicsSystem (new G4Wo);
        RegisterGraphicsSystem (new G4Xo);
#endif

#ifdef G4VIS_USE_OPENGLX
        RegisterGraphicsSystem (new G4OpenGLImmediateX);
//RegisterGraphicsSystem (new G4OpenGLStoredX);
#endif

#ifdef G4VIS_USE_OPENGLWIN32
        RegisterGraphicsSystem (new G4OpenGLImmediateWin32);
        RegisterGraphicsSystem (new G4OpenGLStoredWin32);
#endif

//#ifdef G4VIS_USE_OPENGLXM
//RegisterGraphicsSystem (new G4OpenGLImmediateXm);
//RegisterGraphicsSystem (new G4OpenGLStoredXm);
//#endif

#ifdef G4VIS_USE_OIX
        RegisterGraphicsSystem (new G4OpenInventorX);
#endif

#ifdef G4VIS_USE_OIWIN32
        RegisterGraphicsSystem (new G4OpenInventorWin32);
#endif

#ifdef G4VIS_USE_VRML
        RegisterGraphicsSystem (new G4VRML1);
        RegisterGraphicsSystem (new G4VRML2);
#endif

        if (fVerbose > 0) {
//    G4cout <<
//      "\nYou have successfully registered the following graphics systems."
//	 << G4endl;
//    PrintAvailableGraphicsSystems ();
        }
}
#endif
