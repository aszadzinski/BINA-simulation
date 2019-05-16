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
    b1 = np.array(load1(argv[1], 15)).transpose()
    b2 = np.array(load1(argv[2], 18)).transpose()
    b3 = np.array(load1(argv[3], 9)).transpose()
    #print(b1[1])

    #plt.hist2d(b1[5],b1[6],bins=200)
    #plt.savefig("mwpc.png")
    #plt.clf()

    x,y = [],[]

    #for i in b1[2]:
      #  if i == 1:
    #        x.append(b1[5])
     #       y.append(b1[6])
    #plt.scatter(np.array(x[:200]),np.array(y[:200]))
    #plt.show()
    #plt.clf()
    x,y = [],[]
    z,zz = [],[]

    for i in range(b3.shape[0]):
        if b3[i][12] == 1:
            x.append(b3[i][15]+180)
            y.append(b3[i][16])
    det = 999
    pr1, pr2 = 0,0
    ix = 0
    tmx,tmy,td,tt,tp=0,0,0,0,0
    dmx1,dmx2,dmy1,dmy2,dd1,dd2,dt1,dt2,dp1,dp2=[],[],[],[],[],[],[],[],[],[]
    for i in range(b1.shape[0]):
        if b1[i][1]==2:
            if b1[i][0]==ix:
                dmx1.append(tmx)
                dmy1.append(tmy)
                dmx2.append(b1[i][5])
                dmy2.append(b1[i][6])
                dd1.append(td)
                dd2.append(b1[i][12])
                dt2.append(b2[i][6])
                dp2.append(b2[i][7])
                dt1.append(tt)
                dp1.append(tp)
            tmx = b1[i][5]
            tmy = b1[i][6]
            td = b1[i][12]
            ix = b1[i][0]
            tt = b2[i][6]
            tp - b2[i][7]

        if b1[i][1] == 2 and b1[i][5]!=0 and b1[i][6]!=0:# and np.abs(b1[i][6])< 5:# and ix!=b1[i][0]:
            z.append(b1[i][5])
            zz.append(b1[i][6])
            #det = b1[i][12]


    #MWPC
    at,ap,mx,my,mxb,myb=[],[],[],[],[],[]
    for i in range(len(dd1)):
        if dmx2[i] == 0 and dmx1[i]==0 and dd1[i] < 150 and dd2[i]<150:
            mxb.append(dt2[i]+180)
            myb.append(dp2[i])
    for i in range(len(dd1)):
        if dmx2[i] !=0 and dd1[i] < 150 and dd1[i] != 0:
            mx.append(dmx2[i])
            my.append(dmy2[i])
            at.append(dt2[i]+180)
            ap.append(dp2[i])
        elif dmx1[i] !=0 and dd2[i] < 150 and dd2[i] != 0:
            mx.append(dmx1[i])
            my.append(dmy1[i])
    plt.hist2d(at,ap,bins=96)
    plt.colorbar()
    plt.title("Protons detected in wall with ball coincidence")
    plt.xlabel("$\phi$ [deg]")
    plt.ylabel("$\Theta$ [deg]")
    plt.show()
    #plt.savefig("ptt.png")
    plt.clf()
    plt.hist2d(mxb,myb,bins=96)
    plt.colorbar()
    plt.title("all protons detected in ball")
    plt.xlabel("$\phi$ [deg]")
    plt.ylabel("$\Theta$ [deg]")
    plt.show()
    #plt.savefig("ptt.png")
    plt.clf()
    plt.hist2d(mx,my,bins=96)
    plt.colorbar()
    plt.title("$p_2$ detected in ball")
    plt.xlabel("MWPC x[mm]")
    plt.ylabel("MWPC y[mm]")
    plt.show()
    #plt.savefig("ptt.png")
    plt.clf()
    plt.hist2d(z,zz,bins=96)
    plt.colorbar()
    plt.title("Detections in MWPC")
    plt.xlabel("MWPC x[mm]")
    plt.ylabel("MWPC y[mm]")
    plt.show()
    #plt.savefig("ptt.png")
    plt.clf()
    #ss
    plt.hist2d(x,y,bins=90)
    plt.colorbar()
    plt.xlabel("$\phi$")
    plt.ylabel("$\Theta$")
    plt.title("Detections in wall with MWPC")
    plt.show()
    #plt.savefig("ptt.png")
    plt.clf()


    max_n = b2[-1][0]
    temp = 0
    temp2 = 0
    de= 0 
    xx,yy=[],[]
    pp1,pp2,pp,tt1,tt2 = [],[],[],[],[]
    tempp=0
    tempt=0
    tempt2=0
    for i in range(int(max_n)):
        if b2[i][0] == temp and b2[i][1]==2:
            xx.append(de)
            yy.append(b2[i][5])
            pp.append(b2[i][6]-tempp)
            pp1.append(tempp)
            pp2.append(b2[i][6])
            tt1.append(tempt)
            tt2.append(b2[i][7])

        elif b2[i][1]==2:
            temp = b2[i][0]
            de = b2[i][5]
            tempp = b2[i][6]
            tempt = b2[i][7]
    xxx,yyy,ttt=[],[],[]
    for ii,i in enumerate(pp):
        if i < 125 and i >150:
            if tt1[ii] > 30 and tt1[ii] < 36 and tt2[ii] < 36 and tt2[ii] > 30:
                xxx.append(xx[ii])
                yyy.append(yy[ii])








    
