int albertGenerator (Double_t alpha, Double_t beta, Double_t beamEnergy=160,  Double_t beamMass=1875.613, Double_t targetMass=938.2720813)
{
const Double_t mp=938.2720813;
const Double_t mn=939.5654133;
const Double_t md=1875.613;
Double_t p_plusCMarr[4];

Double_t beamMoment=sqrt(beamEnergy*beamEnergy+2.*beamMass*beamEnergy);
Double_t betaLAB=beamMoment/(sqrt(pow(beamMoment,2)+pow(beamMass,2)));
Double_t Ecm=sqrt(2*targetMass*beamEnergy+targetMass*targetMass+beamMass*beamMass);
Double_t betaCM=beamMoment/(sqrt(pow(beamMoment,2)+pow(beamMass,2))+targetMass);//beam beta in CM

const TVector3 b(0,0,betaCM);
const TVector3 bLAB(0,0,betaLAB);
TLorentzVector beam(0,0,beamMoment,sqrt(pow(beamMoment,2)+pow(beamMass,2)));
TLorentzVector target(0,0,0,targetMass);
TLorentzVector beamCM(0,0,beamMoment*targetMass/Ecm,sqrt(pow(beamMoment*targetMass/Ecm,2)+pow(beamMass,2)));
beamCM.Boost((bLAB-b));
beam.Boost(-b);
target.Boost(-b);


Double_t beamEnergyCM=beam.E();
Double_t targetEnergyCM=sqrt(pow(beam.Z(),2)+pow(targetMass,2));
Double_t deuteriumBindingE=0.;//-2.22452; //positive if breakup is exoergic, usually negative!
//Double_t binding=deuteriumBindingE;

Double_t totalEnergy=beamEnergyCM+targetEnergyCM+deuteriumBindingE;
Double_t totalKinEnergy=totalEnergy-targetMass-beamMass;
Double_t pCM=beam.Z();


Double_t pSS=
 sqrt(5.*md*md/9. + mn*mn/3. - 7.*mp*mp/9. + 10.*pCM*pCM/9. +10./9.*sqrt(md*md+pCM*pCM)*sqrt(mp*mp+pCM*pCM) - //alternative - instead of +
 1./18.* sqrt(64. *md*md*md*md +192.*md*md*mn*mn+192.*md*md*mp*mp+192.*mn*mn*mp*mp-128.*mp*mp*mp*mp+512.*md*md*pCM*pCM+384.*mn*mn*pCM*pCM +
 128.*mp*mp*pCM*pCM+512.*pCM*pCM*pCM*pCM+256.*md*md*sqrt(md*md+pCM*pCM)*sqrt(mp*mp+pCM*pCM)+384.*mn*mn*sqrt(md*md+pCM*pCM)*sqrt(mp*mp+pCM*pCM)-
 128.*mp*mp*sqrt(md*md+pCM*pCM)*sqrt(mp*mp+pCM*pCM)+512.*pCM*pCM*sqrt(md*md+pCM*pCM)*sqrt(mp*mp+pCM*pCM)
 ));
 

Double_t eSS=2*sqrt(pSS*pSS+mp*mp)+sqrt(pSS*pSS+mn*mn)-2*mp-mn;

if (eSS<0) {cout<<"Negative energy -- increase beam energy\n"; return 1;}

Double_t totalMomentumCM=pSS;


TLorentzVector *p1=new TLorentzVector(0,-totalMomentumCM,0,sqrt(pow(totalMomentumCM,2)+pow(mp,2)));
TLorentzVector *p2=(TLorentzVector*)p1->Clone();
p1->RotateZ(2.*TMath::Pi()/3.);
p2->RotateZ(-2.*TMath::Pi()/3.);
TLorentzVector *n=new TLorentzVector(0,-totalMomentumCM,0,sqrt(pow(totalMomentumCM,2)+pow(mn,2)));


p1->RotateZ(TMath::Pi()*beta/180.);
p2->RotateZ(TMath::Pi()*beta/180.);
n->RotateZ(TMath::Pi()*beta/180.);
p1->RotateX(TMath::Pi()*(alpha+90.)/180.);
p2->RotateX(TMath::Pi()*(alpha+90.)/180.);
n->RotateX(TMath::Pi()*(alpha+90.)/180.);


p1->Boost(b);//transform to beam reference frame
p2->Boost(b);
n->Boost(b);

cout<<p1->Theta()*180/TMath::Pi()<<' '<<p1->Phi()*180/TMath::Pi()<<' '<<p1->E()-mp<<" P--> "<<p1->P()<<' '<<p1->Px()<<' '<<p1->Py()<<' '<<p1->Pz()<<'\n';
cout<<p2->Theta()*180/TMath::Pi()<<' '<<p2->Phi()*180/TMath::Pi()<<' '<<p2->E()-mp<<' '<<p2->P()<<'\n';
cout<<n->Theta()*180/TMath::Pi()<<' '<<n->Phi()*180/TMath::Pi()<<' '<<n->E()-mn<<' '<<n->P()<<'\n';


return 0;

}



