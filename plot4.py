import matplotlib.pyplot as plt
import numpy as np
from sys import argv
from time import sleep

def load1(path, nn):
    
    with open(path,'r') as f:
        l = f.readlines()
        t=[]
        n = len(l[1].split())
        for j in range(n):
            t.append([])
        
        for ii, i in enumerate(l):
            tt = i.split()
            #print(len(tt
           # sleep(1)
            #print(tt)
            if len(tt) == n:
                for kk,k in enumerate(tt):
                    try:
                        t[kk].append(float(k))
                    except:
                        print("{}---{}".format(kk,k))
    return t

if __name__ == "__main__":
    try:
        print('Loading {}'.format(argv[1]))
        b3 = np.array(load1(argv[1], 9)).transpose()
        print('Done.\n')
    except:
        print("Loading data error.\n Try python plot4.py <Bina_output4.data> <p/d> <save>\n\n")
        exit()
    if argv[2] == 'p':
        reaction = "$^1H(d,pp)n$"
    else:
        reaction="$^2H(p,pp)n$"

    dwp,dwt = [[],[],[]], [[],[],[]]
    dbp,dbt = [[],[],[]], [[],[],[]]
    mwx,mwy =[[],[],[]], [[],[],[]]
    mbx,mby =[[],[],[]], [[],[],[]]
    pdwp,pdwt = [[],[],[]], [[],[],[]]
    pdbp,pdbt = [[],[],[]], [[],[],[]]
    pmwx,pmwy =[[],[],[]], [[],[],[]]
    pmbx,pmby =[[],[],[]], [[],[],[]]

    bb3 = np.zeros((b3.shape[0],17*2))
    ndwp =[]
    ndbp =[]


    print("Getting detection area...")
    for i in range(b3.shape[0]):
        arr=[]
        first=True
        for particle in range(3):
            if b3[i][14 + particle*17]!=0 and b3[i][15 + particle*17]!=0:#detected in mwpc and wall
                dwp[particle].append(b3[i][particle*17 + 4])
                dwt[particle].append(b3[i][particle*17 + 5])
                mwx[particle].append(b3[i][particle*17 + 2])
                mwy[particle].append(b3[i][particle*17 + 3])
            if b3[i][16 + particle*17]!=0 and b3[i][15 + particle*17]!=0 and b3[i][14 +particle*17]==0 :#detected in ball
                dbp[particle].append(b3[i][particle*17 + 4])
                dbt[particle].append(b3[i][particle*17 + 5])
                mbx[particle].append(b3[i][particle*17 + 2])
                mby[particle].append(b3[i][particle*17 + 3])
            if b3[i][1+particle*17]==2:
                if first:
                    arr = list(b3[i][particle*17:particle*17 +17])
                    first=False
                else:
                    arr += list(b3[i][particle*17:particle*17+17])
                    bb3[i] = np.array(arr)
                    arr=[]
                    first=True

    n1=0
    n2=0
    alfab = [[],[]]
    betab =[[],[]]
    gammaw=[[],[]]
    gammab=[[],[]]
    alfaw = [[],[]]
    betaw =[[],[]]
    for i in range(bb3.shape[0]):
        n1+=1
        for particle in range(2):

            if bb3[i][14 + particle*17]!=0 and bb3[i][15 + particle*17]!=0 and bb3[i][1+particle*17]==2:#detected in mwpc and wall
                alfaw[particle].append(bb3[i][particle*17+11])
                betaw[particle].append(bb3[i][particle*17+12])
                gammaw[particle].append(bb3[i][particle*17+13])
                pdwp[particle].append(bb3[i][particle*17 + 4])
                pdwt[particle].append(bb3[i][particle*17 + 5])
                pmwx[particle].append(bb3[i][particle*17 + 2])
                pmwy[particle].append(bb3[i][particle*17 + 3])
            if bb3[i][16 + particle*17]!=0 and bb3[i][15 + particle*17]!=0 and bb3[i][14 +particle*17]==0  and bb3[i][1+particle*17]==2:#detected in ball
                alfab[particle].append(bb3[i][particle*17+11])
                betab[particle].append(bb3[i][particle*17+12])
                gammab[particle].append(bb3[i][particle*17+13])
                pdbp[particle].append(bb3[i][particle*17 + 4])
                pdbt[particle].append(bb3[i][particle*17 + 5])
                pmbx[particle].append(bb3[i][particle*17 + 2])
                pmby[particle].append(bb3[i][particle*17 + 3])
    print("DONE.")


#############################
#       DETECTION AREA
#############################
    print("Creating plots....")
    #detection area
    fig = plt.figure(figsize=(18, 8))
    plt.hist2d(dwt[1]+dwt[2]+dwt[0]+dbt[1]+dbt[2]+dbt[0],dwp[1]+dwp[2]+dwp[0]+dbp[1]+dbp[2]+dbp[0],bins=[180,90],cmap="inferno")
    plt.colorbar()
    plt.xlabel("$\phi$ [deg]")
    plt.ylabel("$\Theta$ [deg]")
    plt.title("Detection area {} $\eta$={}%".format(reaction, round(100*(len(dwt[1]+dwt[2]+dwt[0]+dbt[1]+dbt[2]+dbt[0]))/(n1*3),1)))
    if argv[3]=="save":
        plt.savefig("data/detection_area.png")
    else:
        plt.show()
    plt.clf()

    #WALL
    plt.hist2d(pdwt[1]+pdwt[0],pdwp[1]+pdwp[0],bins=[180,90],cmap="inferno")
    plt.colorbar()
    plt.xlabel("$\phi$ [deg]")
    plt.ylabel("$\Theta$ [deg]")
    plt.title("Detection area WALL {} $\eta$={}%".format(reaction,round(100*(len(pdwt[1]+pdwt[0]))/(n1*2),1)))
    if argv[3]=="save":
        plt.savefig("data/detection_areaWALL.png")
    else:
        plt.show()
    plt.clf()
    #BALL
    plt.hist2d(pdbt[1]+pdbt[0],pdbp[1]+pdbp[0],bins=[180,90],cmap="inferno")
    plt.colorbar()
    plt.xlabel("$\phi$ [deg]")
    plt.ylabel("$\Theta$ [deg]")
    plt.title("Detection area BALL {} $\eta$={}%".format(reaction,round(100*(len(pdbt[1]+pdbt[0]))/(2*n1),1)))
    if argv[3]=="save":
        plt.savefig("data/detection_areaBALL.png")
    else:
        plt.show()
    plt.clf()

    #MWPC
    fig = plt.figure(figsize=(9, 8))
    plt.hist2d(mwx[1]+mwx[2]+mwx[0],mwy[1]+mwy[2]+mwy[0],bins=96,cmap="inferno")
    plt.colorbar()
    plt.xlabel("$MWPC_x$ [mm]")
    plt.ylabel("$MWPC_y$ [mm]")
    plt.title("Detections in MWPC {}".format(reaction))
    if argv[3]=="save":
        plt.savefig("data/detection_MWPC.png")
    else:
        plt.show()
    plt.clf()

    
###################################
#       COINCIDENTIONS
###################################
    cdwp,cdwt = [],[]
    cdbp,cdbt = [],[]
    cmx,cmy =[], []
    cdbbp, cdbbt= [], []
    cdwwp, cdwwt = [], []
    nn=[]
    caw,cab,cbw,cbb,cgw,cgb,=[],[],[],[],[],[]
    cabb,cbbb,cgbb=[],[],[]
    caww,cbww,cgww=[],[],[]

    print(" coincidence pairs...")
    for i in range(bb3.shape[0]):
        nn.append(0)
        if bb3[i][14]==1 and bb3[i][15]==1 and bb3[i][31]==1 and bb3[i][32]==1 and bb3[i][33]==0 and bb3[i][16]==0:
            cdwwt.append(bb3[i][5])
            cdwwt.append(bb3[i][22])
            cdwwp.append(bb3[i][4])
            cdwwp.append(bb3[i][21])
            caww.append(bb3[i][11])
            cbww.append(bb3[i][12])
            cgww.append(bb3[i][13])
            caww.append(bb3[i][28])
            cbww.append(bb3[i][29])
            cgww.append(bb3[i][30])

        if bb3[i][14]==1 and bb3[i][15]==1 and bb3[i][32]==1 and bb3[i][33]==1:
            cmx.append(bb3[i][2])
            cmy.append(bb3[i][3])
            cdwp.append(bb3[i][4])
            cdwt.append(bb3[i][5])
            cdbp.append(bb3[i][21])
            cdbt.append(bb3[i][22])
            caw.append(bb3[i][11])
            cbw.append(bb3[i][12])
            cgw.append(bb3[i][13])
            cab.append(bb3[i][28])
            cbb.append(bb3[i][29])
            cgb.append(bb3[i][30])


        if bb3[i][16]==1 and bb3[i][15]==1 and bb3[i][32]==1 and bb3[i][31]==1:
            cmx.append(bb3[i][19])
            cmy.append(bb3[i][20])
            cdwp.append(bb3[i][21])
            cdwt.append(bb3[i][22])
            cdbp.append(bb3[i][4])
            cdbt.append(bb3[i][5])
            caw.append(bb3[i][28])
            cbw.append(bb3[i][29])
            cgw.append(bb3[i][30])
            cab.append(bb3[i][11])
            cbb.append(bb3[i][12])
            cgb.append(bb3[i][13])
        if bb3[i][16]!=0 and bb3[i][15]!=0 and bb3[i][32]!=0 and bb3[i][33]!=0 and bb3[i][14]==0 and bb3[i][31]==0:
            cdbbp.append(bb3[i][4])
            cdbbp.append(bb3[i][21])
            cdbbt.append(bb3[i][5])
            cdbbt.append(bb3[i][22])
            cabb.append(bb3[i][11])
            cbbb.append(bb3[i][12])
            cgbb.append(bb3[i][13])


    print("Done.")


    #MWPC and BALL
    plt.hist2d(cmx,cmy,bins=96,cmap="inferno")
    plt.colorbar()
    plt.xlabel("$MWPC_x$ [mm]")
    plt.ylabel("$MWPC_y$ [mm]")
    plt.title("Coincidence MWPC-BALL {} $\eta$={}%".format(reaction,round(100*len(cmx)/len(nn),1)))
    if argv[3]=="save":
        plt.savefig("data/coi_MB.png")
    else:
        plt.show()
    plt.clf()
    
    #WALL and BALL
    fig = plt.figure(figsize=(18, 8))
    plt.hist2d(cdwt,cdwp,bins=[180,90],cmap="inferno")
    plt.colorbar()
    plt.xlabel("$\phi$ [deg]")
    plt.ylabel("$\Theta$ [deg]")
    plt.title("Coincidence WALL-BALL {} $\eta$={}%".format(reaction,round(100*len(cdwt)/len(nn),1)))
    if argv[3]=="save":
        plt.savefig("data/coi_WB.png")
    else:
        plt.show()
    plt.clf()

    #WALL and BALL in BALL
    plt.hist2d(cdbt,cdbp,bins=[180,90],cmap="inferno")
    plt.colorbar()
    plt.xlabel("$\phi$ [deg]")
    plt.ylabel("$\Theta$ [deg]")
    plt.title("Coincidence BALL-WALL {} $\eta$={}%".format(reaction,round(100*len(cdbt)/len(nn),1)))
    if argv[3]=="save":
        plt.savefig("data/coi_BW.png")
    else:
        plt.show()
    plt.clf()
    
    plt.hist2d(cdwwt,cdwwp,bins=[180,90],cmap="inferno")
    plt.colorbar()
    plt.xlabel("$\phi$ [deg]")
    plt.ylabel("$\Theta$ [deg]")
    plt.title("Coincidence WALL-WALL {} $\eta$={}%".format(reaction,round(100*len(cdwwt)/len(nn),1)))
    if argv[3]=="save":
        plt.savefig("data/coi_WW.png")
    else:
        plt.show()
    plt.clf()
    #BALL-BALL
    plt.hist2d(cdbbt,cdbbp,bins=[180,90],cmap="inferno")
    plt.colorbar()
    plt.xlabel("$\phi$ [deg]")
    plt.ylabel("$\Theta$ [deg]")
    plt.title("Coincidence BALL-BALL {} $\eta$={}%".format(reaction,round(100*len(cdbbt)/len(nn),1)))
    if argv[3]=="save":
        plt.savefig("data/coi_BB.png")
    else:
        plt.show()
    plt.clf()



###################################
#       CROSS-OVER
###################################

    cowp, cowt, cobt,cobp = [], [], [], []
    nnn = []

    cca,ccb,ccg=[],[],[]
    for i in range(bb3.shape[0]):
        nnn.append(0)
        if bb3[i][15]==2:
            cowp.append(bb3[i][4])
            cowt.append(bb3[i][5])
            cca.append(bb3[i][11])
            ccb.append(bb3[i][12])
            ccg.append(bb3[i][13])
        if bb3[i][32]==2:
            cowp.append(bb3[i][21])
            cowt.append(bb3[i][22])
            cca.append(bb3[i][28])
            ccb.append(bb3[i][29])
            ccg.append(bb3[i][30])

    #Cross over
    plt.hist2d(cowt,cowp,bins=[180,90],cmap="inferno")
    plt.colorbar()
    plt.xlabel("$\phi$ [deg]")
    plt.ylabel("$\Theta$ [deg]")
    plt.title("Cross-over {} $\eta$={}%".format(reaction,round(100*len(cowt)/len(nnn),1)))
    if argv[3]=="save":
        plt.savefig("data/CC.png")
    else:
        plt.show()
    plt.clf()


###################################
#       Kinematic curve
###################################

    phi12 = 50
    dphi12 = 5
    th1 = 25
    th2 = 50
    dth = 5

    E1, E2 = [], [] 

    for i in range(bb3.shape[0]):
        _phi12 = bb3[i][21]-bb3[i][5]
        _th1 = bb3[i][4]
        _th2 = bb3[i][21]
        if _phi12 < phi12+dphi12 and _phi12 > phi12-dphi12 and _th1 < th1+dth and _th1 > th1-dth and _th2<th2+dth and _th2>th2-dth:
            E1.append(bb3[i][6])
            E2.append(bb3[i][23])

    
    plt.hist2d(E1,E2,bins=100,cmap="inferno")
    plt.colorbar()
    plt.xlabel("$E_1$ [MeV]")
    plt.ylabel("$E_2$ [MeV]")
    plt.title("Kinematic {} $\phi12$={} $\Theta_1$={} $\Theta_2$={}".format(reaction,phi12,th1,th2))
    if argv[3]=="save":
        plt.savefig("data/kinematicCurve.png")
    else:
        plt.show()
    plt.clf()


###################################
#       Beam
###################################

    t1,e1,e2,p1=[],[],[],[]
    ea,eb=[],[]
    for i in range(bb3.shape[0]):
        ea.append(bb3[i][11])
        eb.append(bb3[i][12])
        ea.append(bb3[i][28])
        eb.append(bb3[i][29])
        e2.append(bb3[i][7])
        e2.append(bb3[i][24])
        e1.append(bb3[i][6])
        e1.append(bb3[i][23])
        t1.append(bb3[i][5])
        t1.append(bb3[i][22])
        p1.append(bb3[i][4])
        p1.append(bb3[i][21])

    plt.hist2d(p1,e1,bins=180,cmap="inferno")
    plt.colorbar()
    plt.xlabel("$\Theta$ [deg]")
    plt.ylabel("$E$ [MeV]")
    plt.title("$E(\Theta)$ {}".format(reaction))
    if argv[3]=="save":
        plt.savefig("data/plutoEtheta.png")
    else:
        plt.show()
    plt.clf()
    plt.hist(e1,bins=90,histtype='step')
    plt.xlabel("$E [MeV]$")
    plt.ylabel("counts")
    plt.title("$E$ {}".format(reaction))
    if argv[3]=="save":
        plt.savefig("data/plutoE.png")
    else:
        plt.show()
    plt.clf()
    plt.hist(t1,bins=90,histtype='step',label="$\phi$")
    plt.hist(p1,bins=90,histtype='step',label="$\Theta$")
    plt.xlabel("[deg]")
    plt.legend()
    plt.ylabel("counts")
    plt.title("$E$ {}".format(reaction))
    if argv[3]=="save":
        plt.savefig("data/plutothetaphi.png")
    else:
        plt.show()
    plt.clf()

    #========================
    #====    SSA analysis
    #==========================
    plt.hist(alfaw[0]+alfaw[1],bins=90,histtype='step',label="$\\alpha$")
    plt.hist(betaw[0]+betaw[1],bins=90,histtype='step',label="$\\beta$")
    plt.xlabel("$\\alpha$")
    plt.ylabel("counts")
    plt.legend()
    plt.title("Wall detection area: Star configurations")
    if argv[3]=="save":
        plt.savefig("data/starw.png")
    else:
        plt.show()
    plt.clf()


    plt.hist(alfab[0]+alfab[1],bins=90,histtype='step',label="$\\alpha$")
    plt.hist(betab[0]+betab[1],bins=90,histtype='step',label="$\\beta$")
    plt.legend()
    plt.xlabel("$\\alpha$")
    plt.ylabel("counts")
    plt.title("Ball detection area: Star configurations")
    if argv[3]=="save":
        plt.savefig("data/starb.png")
    else:
        plt.show()
    plt.clf()

    plt.hist(caw,bins=90,histtype='step',label="$\\alpha$")
    plt.hist(cbw,bins=90,histtype='step',label="$\\beta$")
    plt.legend()
    plt.title("Ball-Wall$^*$ coincidences: Star configurations")
    plt.xlabel("$\\alpha$")
    plt.ylabel("counts")
    if argv[3]=="save":
        plt.savefig("data/starbww.png")
    else:
        plt.show()
    plt.clf()

    plt.hist(cab,bins=90,histtype='step',label="$\\alpha$")
    plt.hist(cbb,bins=90,histtype='step',label="$\\beta$")
    plt.legend()
    plt.xlabel("$\\alpha$")
    plt.ylabel("counts")
    plt.title("Ball$^*$-Wall coincidences: Star configurations")
    if argv[3]=="save":
        plt.savefig("data/starbbw.png")
    else:
        plt.show()
    plt.clf()
    
    plt.hist(cabb,bins=90,histtype='step',label="$\\alpha$")
    plt.hist(cbbb,bins=90,histtype='step',label="$\\beta$")
    plt.xlabel("$\\alpha$")
    plt.ylabel("counts")
    plt.legend()
    plt.title("Ball-Ball coincidences: Star configurations")
    if argv[3]=="save":
        plt.savefig("data/starbb.png")
    else:
        plt.show()
    plt.clf()


    plt.hist(caww,bins=90,histtype='step',label="$\\alpha$")
    plt.hist(cbww,bins=90,histtype='step',label="$\\beta$")
    plt.legend()
    plt.xlabel("$\\alpha$")
    plt.ylabel("counts")
    plt.title("Wall-Wall coincidences: Star configurations")
    if argv[3]=="save":
        plt.savefig("data/starww.png")
    else:
        plt.show()
    plt.clf()

    plt.hist2d(cab,cbb,bins=[90,180],cmap='inferno')
    plt.colorbar()
    plt.xlabel("$\\alpha$")
    plt.ylabel("$\\beta$")
    plt.title("Ball$^*$-Wall coincidences: Star configurations")
    if argv[3]=="save":
        plt.savefig("data/starbbww.png")
    else:
        plt.show()
    plt.clf()
    plt.hist2d(caw,cbw,bins=[90,180],cmap='inferno')
    plt.xlabel("$\\alpha$")
    plt.ylabel("$\\beta$")
    plt.colorbar()
    plt.title("Ball-Wall$^*$ coincidences: Star configurations")
    if argv[3]=="save":
        plt.savefig("data/starbww2.png")
    else:
        plt.show()
    plt.clf()


    plt.hist2d(cabb,cbbb,bins=[90,180],cmap='inferno')
    plt.colorbar()
    plt.xlabel("$\\alpha$")
    plt.ylabel("$\\beta$")
    plt.title("Ball-Ball coincidences: Star configurations")
    if argv[3]=="save":
        plt.savefig("data/starbb2.png")
    else:
        plt.show()
    plt.clf()
    
    plt.hist2d(caww,cbww,bins=[90,180],cmap='inferno')
    plt.colorbar()
    plt.xlabel("$\\alpha$")
    plt.ylabel("$\\beta$")
    plt.title("Ball-Ball coincidences: Star configurations")
    if argv[3]=="save":
        plt.savefig("data/starww2.png")
    else:
        plt.show()
    plt.clf()

    plt.hist2d(ea,e1,bins=[180,100],cmap='inferno')
    plt.xlabel("$\\alpha$")
    plt.ylabel("E [MeV]")
    plt.colorbar()
    plt.title("$E(\\alpha)$: Star configurations")
    if argv[3]=="save":
        plt.savefig("data/starea.png")
    else:
        plt.show()
    plt.clf()

    plt.hist2d(eb,e1,bins=[180,100],cmap='inferno')
    plt.xlabel("$\\beta$")
    plt.ylabel("E [MeV]")
    plt.colorbar()
    plt.title("$E(\\beta)$: Star configurations")
    if argv[3]=="save":
        plt.savefig("data/stareb.png")
    else:
        plt.show()
    plt.clf()
    plt.hist2d(ea,p1,bins=[180,100],cmap='inferno')
    plt.xlabel("$\\alpha$")
    plt.ylabel("$\\Theta$ [deg]")
    plt.colorbar()
    plt.title("$\\Theta(\\alpha)$: Star configurations")
    if argv[3]=="save":
        plt.savefig("data/starat.png")
    else:
        plt.show()
    plt.clf()

    plt.hist2d(eb,p1,bins=[180,100],cmap='inferno')
    plt.xlabel("$\\beta$")
    plt.ylabel("$\Theta$ [deg]")
    plt.colorbar()
    plt.title("$\\Theta(\\beta)$: Star configurations")
    if argv[3]=="save":
        plt.savefig("data/starbt.png")
    else:
        plt.show()
    plt.clf()
