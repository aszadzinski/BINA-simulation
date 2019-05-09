import matplotlib.pyplot as plt
import numpy as np
from sys import argv
from time import sleep

def load1(path, n):
    
    with open(path,'r') as f:
        l = f.readlines()
        t=[]
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
    b1 = np.array(load1(argv[1], 15))
    b2 = np.array(load1(argv[2], 18))
    b3 = np.array(load1(argv[3], 9))
    print(b1[1])

    #plt.hist2d(b1[5],b1[6],bins=200)
    #plt.savefig("mwpc.png")
    #plt.clf()

    x,y = [],[]

    for i in b1[2]:
        if i == 1:
            x.append(b1[5])
            y.append(b1[6])
    plt.scatter(np.array(x[:200]),np.array(y[:200]))
    plt.show()
    plt.clf()
    x,y = [],[]

    for i in b3[2]:
        if i == 1:
            x.append(b1[6])
            y.append(b1[7])
    plt.hist2d(x,y,bins=len(x))
    plt.savefig("ptt.png")
    plt.clf()




    
