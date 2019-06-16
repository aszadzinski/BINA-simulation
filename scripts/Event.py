import numpy as np
import matplotlib.pyplot as plt
from sys import argv
import time 

class Events:
    def __init__(self, filename):
        self.load(filename) #Nx3x20 data[i]->n,p,p
        self.filename = filename
        self.n = self.data.shape[0]*self.data.shape[1]

    def detectionFilter(self):
        print("started deta")
        detections = [[],[],[]] # ball,E, crossover ball,all,E
        self.detections = [0, 0, 0, 0 ]
        for event in  self.data:
            for particle in event[1:]:
                self.detections[3] += 1
                if particle[14]==0 and particle[15]==1 and particle[16]==1:#ball
                    detections[0].append(particle.tolist())
                    self.detections[0] += 1
                if particle[14]==1 and particle[15]==1 and particle[16]==0:#E
                    detections[1].append(particle.tolist())
                    self.detections[1] += 1
                if particle[15]==2:#ball
                    detections[2].append(particle.tolist())
                    self.detections[2] += 1
        for j,i in enumerate(detections):
            if len(i) == 0:
                detections[j].append([i for i in range(17)])
        detections = [np.array(detections[0]), np.array(detections[1]), np.array(detections[2])]
        print("copied detA and del tmp")
        return detections

    def coincidencesFilter(self):
        detections = [[[],[]],[[],[]],[[],[]]] #BB,WW,BW
        for event in self.data:
            if event[1][14]==0 and event[2][14]==0 and event[1][15]==1 and event[2][15]==1 and event[1][4]>11 and event[2][4]>11:#BB
                detections[0][0].append(event[1])
                detections[0][1].append(event[2])
            if event[1][14]==1 and event[2][14]==1 and event[1][15]==1 and event[2][15]==1:#WW
                detections[1][0].append(event[1])
                detections[1][1].append(event[2])
            if event[1][14]==1 and event[2][14]==0 and event[1][15]==1 and event[2][15]==1 and  event[2][4]>30:#BW
                detections[2][0].append(event[1])
                detections[2][1].append(event[2])
            if event[1][14]==0 and event[2][14]==1 and event[1][15]==1 and event[2][15]==1 and event[1][4]>30:#WB
                detections[2][0].append(event[1])
                detections[2][1].append(event[2])
        for j,i in enumerate(detections):
            if len(i[1]) == 0:
                detections[j][0].append(np.zeros(17))
                detections[j][1].append(np.zeros(17))
        detections = [np.array(detections[0]), np.array(detections[1]), np.array(detections[2])]
        return detections

    def load(self, filename):
        try:
            file = open(filename, 'r')
            print("opened dile")
            lines = file.readlines()
            print("loaded lines")
            file.close()
            data = []
            for i in lines[:int(len(lines)/4)]:
                line = i.split()
                tmp = [float(j) for j in line]
                data.append(tmp)
            del lines
            print("converted data")
            new_data = []
            tevt1, tevt2, tevt3 = [-1], [-1], [-1]
            for i,j in enumerate(data):
                if j[0] == tevt1[0]:
                    if j[0]==tevt2[0]:
                        tevt3 = [tevt1, tevt2, j]
                        new_data.append(tevt3)
                    else:
                        tevt2 = j
                else:
                    tevt1 = j
            print("loaded data to array")
        finally:
            print("loaded file")
        del data
        self.data = np.array(new_data)
        print("copied file")
        del new_data
        return None


def scat(x,y,filename,lx,ly,color="black", s=0.9):
    print("creating plot: {}".format(filename))
    fig = plt.figure(figsize=(18,8))
    plt.scatter(x,y, s=s, color=color)#, cmap=cmap)
    plt.xlabel(lx,fontsize=23)
    plt.ylabel(ly,fontsize=23)
    plt.savefig("data/{}.png".format(filename))
    plt.clf()

def hist1d(x,filename,lx,ly,bins=90):
    print("creating plot: {}".format(filename))
    fig = plt.figure(figsize=(18,8))
    plt.hist(x, bins=bins, histtype="step")#, cmap=cmap)
    plt.xlabel(lx,fontsize=23)
    plt.ylabel(ly,fontsize=23)
    plt.savefig("data/{}.png".format(filename))
    plt.clf()

def hist(x,y,filename,lx,ly,bins=[181,100],cmap="gist_heat_r"):
    global suf
    plt.rcParams.update({"font.size":20})
    print("creating plot: {}".format(filename))
    fig = plt.figure(figsize=(18,8))
    plt.hist2d(x,y, bins=bins, cmap=cmap)
    plt.xlabel(lx,fontsize=23)
    plt.ylabel(ly,fontsize=23)
    plt.colorbar()
    plt.savefig("data/{}{}.png".format(filename,suf))
    plt.clf()

if __name__ == "__main__":
    suf = ""
    print(1)
    evt = Events("Bina_out4.dat")   
    star = evt.coincidencesFilter()
    det = evt.detectionFilter()

    #energy
    hist(det[0][:,5], det[0][:,4], "balldet", "$\\phi [deg]$", "$\\Theta$ [deg]")
    hist(evt.data[:,1,4].tolist()+evt.data[:,2,4].tolist(), evt.data[:,1,6].tolist()+evt.data[:,2,6].tolist(), "ephi0", "$\\Theta [deg]$", "$E$ [MeV]")
    hist(det[0][:,4].tolist()+det[1][:,4].tolist(), det[0][:,6].tolist()+det[1][:,6].tolist(), "Edetected-phi", "$\\Theta [deg]$", "$E$ [MeV]")
    hist(det[0][:,4].tolist()+det[1][:,4].tolist(), det[0][:,7].tolist()+det[1][:,7].tolist(), "Edepo-phi", "$\\Theta [deg]$", "$E$ [MeV]")
  #  scat(det[0][:,7].tolist()+det[1][:,7].tolist(), det[0][:,6].tolist()+det[1][:,6].tolist(), "EandEd", "$E_D$ [MeV]", "$E$ [MeV]")
  #  EED = np.array(det[0][:,7].tolist()+det[1][:,7].tolist())
  #  EED2 = np.array(det[0][:,6].tolist()+det[1][:,6].tolist())
  #  EED3 = EED2 - EED
  #  scat(EED, EED3, "E-Ed", "$E$ [MeV]", "$E-E_D$ [MeV]")
  #  del EED, EED2, EED3
    
    #area
    hist(det[0][:,5], det[0][:,4], "balldet", "$\\phi [deg]$", "$\\Theta$ [deg]")
    hist(det[1][:,5], det[1][:,4], "walldet", "$\\phi [deg]$", "$\\Theta$ [deg]")
    hist(det[2][:,5], det[2][:,4], "crossdet", "$\\phi [deg]$", "$\\Theta$ [deg]",bins=[300,120])
    hist(det[0][:,5].tolist()+det[1][:,5].tolist(), det[0][:,4].tolist()+det[1][:,4].tolist(), "alldet", "$\\phi [deg]$", "$\\Theta$ [deg]")
    
    #coic
    #hist(star[0][0,:,11].tolist()+star[0][1,:,11].tolist(), star[0][0,:,12].tolist()+star[0][1,:,12].tolist(), "alfaBB", "$\\alpha$", "$\\beta$")


    #star
    hist(det[0][:,11].tolist()+det[1][:,11].tolist(), det[0][:,4].tolist()+det[1][:,4].tolist(), "thetaAlfa", "$\\alpha$", "$\\Theta$")
    hist(det[0][:,11].tolist()+det[1][:,11].tolist(), det[0][:,12].tolist()+det[1][:,12].tolist(), "detab", "$\\alpha$", "$\\beta$")
    hist(det[0][:,11].tolist(), det[0][:,12].tolist(), "detballAB", "$\\alpha$", "$\\beta$")
    hist(det[1][:,11].tolist(), det[1][:,12].tolist(), "detWallAB", "$\\alpha$", "$\\beta$")
    hist(det[0][:,12].tolist()+det[1][:,12].tolist(), det[0][:,4].tolist()+det[1][:,4].tolist(), "thetaBeta", "$\\beta$", "$\\Theta$")
    hist(star[0][0,:,11].tolist()+star[0][1,:,11].tolist(), star[0][0,:,12].tolist()+star[0][1,:,12].tolist(), "alfaBB", "$\\alpha$", "$\\beta$")
    hist(star[2][0,:,11].tolist()+star[2][1,:,11].tolist(), star[2][0,:,12].tolist()+star[2][1,:,12].tolist(), "alfaBW", "$\\alpha$", "$\\beta$")

    suf = "-gray"

    #energy
    hist(det[0][:,5], det[0][:,4], "balldet", "$\\phi [deg]$", "$\\Theta$ [deg]",cmap="binary")
    hist(evt.data[:,1,4].tolist()+evt.data[:,2,4].tolist(), evt.data[:,1,6].tolist()+evt.data[:,2,6].tolist(), "ephi0", "$\\Theta [deg]$", "$E$ [MeV]",cmap="binary")
    hist(det[0][:,4].tolist()+det[1][:,4].tolist(), det[0][:,6].tolist()+det[1][:,6].tolist(), "Edetected-phi", "$\\Theta [deg]$", "$E$ [MeV]",cmap="binary")
    hist(det[0][:,4].tolist()+det[1][:,4].tolist(), det[0][:,7].tolist()+det[1][:,7].tolist(), "Edepo-phi", "$\\Theta [deg]$", "$E$ [MeV]",cmap="binary")
  #  scat(det[0][:,7].tolist()+det[1][:,7].tolist(), det[0][:,6].tolist()+det[1][:,6].tolist(), "EandEd", "$E_D$ [MeV]", "$E$ [MeV]")
  #  EED = np.array(det[0][:,7].tolist()+det[1][:,7].tolist())
  #  EED2 = np.array(det[0][:,6].tolist()+det[1][:,6].tolist())
  #  EED3 = EED2 - EED
  #  scat(EED, EED3, "E-Ed", "$E$ [MeV]", "$E-E_D$ [MeV]")
  #  del EED, EED2, EED3
    
    #area
    hist(det[0][:,5], det[0][:,4], "balldet", "$\\phi [deg]$", "$\\Theta$ [deg]",cmap="binary")
    hist(det[1][:,5], det[1][:,4], "walldet", "$\\phi [deg]$", "$\\Theta$ [deg]",cmap="binary")
    hist(det[2][:,5], det[2][:,4], "crossdet", "$\\phi [deg]$", "$\\Theta$ [deg]",bins=[300,120],cmap="binary")
    hist(det[0][:,5].tolist()+det[1][:,5].tolist(), det[0][:,4].tolist()+det[1][:,4].tolist(), "alldet", "$\\phi [deg]$", "$\\Theta$ [deg]",cmap="binary")
    
    #coic
    #hist(star[0][0,:,11].tolist()+star[0][1,:,11].tolist(), star[0][0,:,12].tolist()+star[0][1,:,12].tolist(), "alfaBB", "$\\alpha$", "$\\beta$")


    #star
    hist(det[0][:,11].tolist()+det[1][:,11].tolist(), det[0][:,4].tolist()+det[1][:,4].tolist(), "thetaAlfa", "$\\alpha$", "$\\Theta$",cmap="binary")
    hist(det[0][:,11].tolist()+det[1][:,11].tolist(), det[0][:,12].tolist()+det[1][:,12].tolist(), "detab", "$\\alpha$", "$\\beta$",cmap="binary")
    hist(det[0][:,11].tolist(), det[0][:,12].tolist(), "detballAB", "$\\alpha$", "$\\beta$",cmap="binary")
    hist(det[1][:,11].tolist(), det[1][:,12].tolist(), "detWallAB", "$\\alpha$", "$\\beta$",cmap="binary")
    hist(det[0][:,12].tolist()+det[1][:,12].tolist(), det[0][:,4].tolist()+det[1][:,4].tolist(), "thetaBeta", "$\\beta$", "$\\Theta$",cmap="binary")
    hist(star[0][0,:,11].tolist()+star[0][1,:,11].tolist(), star[0][0,:,12].tolist()+star[0][1,:,12].tolist(), "alfaBB", "$\\alpha$", "$\\beta$",cmap="binary")
    hist(star[2][0,:,11].tolist()+star[2][1,:,11].tolist(), star[2][0,:,12].tolist()+star[2][1,:,12].tolist(), "alfaBW", "$\\alpha$", "$\\beta$",cmap="binary")


