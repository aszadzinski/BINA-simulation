##############################
# Event class for BINA sim.  #
# author: Albert Szadziński  #
# date: 06.06.19             #
##############################
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
