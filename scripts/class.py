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
        detections = [[],[],[]] # ball,E, crossover ball,all,E
        for event in  self.data:
            for particle in event[1:]:
                if particle[14]==0 and particle[15]==1 and particle[16]==1:#ball
                    detections[0].append(particle.tolist())
                if particle[14]==1 and particle[15]==1 and particle[16]==0:#E
                    detections[1].append(particle.tolist())
                if particle[15]==2:#ball
                    detections[2].append(particle.tolist())
        detections = [np.array(detections[0]), np.array(detections[1]), np.array(detections[2])]
        return detections

    def coincidencesFilter(self):
        detections = [[[],[]],[[],[]],[[],[]]] #BB,WW,BW
        for event in self.data:
            if event[1][14]==0 and event[2][14]==0 and event[1][15]==1 and event[2][15]==1 and event[1][4]>30 and event[2][4]>30:#BB
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
        detections = [np.array(detections[0]), np.array(detections[1]), np.array(detections[2])]
        return detections

    def load(self, filename):
        with open(filename, 'r') as file:
            lines = file.readlines()
            data = []
            for i in lines:
                line = i.split()
                tmp = [float(j) for j in line]
                data.append(tmp)
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
        self.data = np.array(new_data)
        return None


def hist(x,y,filename,lx,ly,bins=90,cmap="Greys"):
    fig = plt.figure(figsize=(18,8))
    plt.hist2d(x,y, bins=bins, cmap=cmap)
    plt.xlabel(lx,fontsize=23)
    plt.ylabel(ly,fontsize=23)
    plt.colorbar()
    plt.savefig("data/{}.png".format(filename))
    plt.clf()

if __name__ == "__main__":
    evt = Events("Bina_out4.dat")   
    star = evt.coincidencesFilter()
    det = evt.detectionFilter()
    hist(det[0][:,11].tolist()+det[1][:,11].tolist(), det[0][:,4].tolist()+det[1][:,4].tolist(), "thetaAlfa", "$\\alpha$", "$\\Theta$")
    hist(det[0][:,11].tolist()+det[1][:,11].tolist(), det[0][:,12].tolist()+det[1][:,12].tolist(), "detab", "$\\alpha$", "$\\beta$")
    hist(det[0][:,11].tolist(), det[0][:,12].tolist(), "detballAB", "$\\alpha$", "$\\beta$")
    hist(det[1][:,11].tolist(), det[1][:,12].tolist(), "detWallAB", "$\\alpha$", "$\\beta$")
    hist(det[0][:,12].tolist()+det[1][:,12].tolist(), det[0][:,4].tolist()+det[1][:,4].tolist(), "thetaBeta", "$\\beta$", "$\\Theta$")
    hist(star[0][0,:,11].tolist()+star[0][1,:,11].tolist(), star[0][0,:,12].tolist()+star[0][1,:,12].tolist(), "alfaBB", "$\\alpha$", "$\\beta$")
    hist(star[2][0,:,11].tolist()+star[2][1,:,11].tolist(), star[2][0,:,12].tolist()+star[2][1,:,12].tolist(), "alfaBW", "$\\alpha$", "$\\beta$")



