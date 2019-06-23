#!/usr/bin/env python3

################################  
# Script for visualization and #
#    BINA data modyfications   #
################################
# author: Albert Szadziński    #
################################

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Data is loaded to numpy out[n][p][t] array                                                                  #
# where n-event, p-particle, t-data type.                                                                     #
# Particles ordered from smallest to largest mass.                                                            #  
# Input file structure:                                                                                       #
# 1.  <num of particles> <beam energy MeV>                                                                    #
# 2.  evt p mwpcx mwpcy phi theta intialE depositedE flag detector flag alpha beta gamma MWPCflag Eflg dEflg  #
# 3.  as above for next particle or event                                                                     #
# t-index has the same numbering from 0 to 16                                                                 #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

import argparse

import BinaVis
from BinaTools import *

def main():
    parser = argparse.ArgumentParser(description="Program to visualize and modify data from BINA simulation")
    parser.add_argument("--filename", '-f', help="Data filename",     default='None')
    parser.add_argument('--save',     '-s', help='Save plots',        action='store_true')
    parser.add_argument('--dir',      '-d', help='Dir for png imag',  default='images/')
    parser.add_argument("--reaction", '-r', help='Reaction name',     default=' ')
    parser.add_argument('--pluto',    '-p', help='Convert pluto .evt')


    args = parser.parse_args()
    print(args.filename)

if __name__ == "__main__":
    main()

