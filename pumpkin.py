# -*- coding: utf-8 -*-
from tools import thinkstats

def Pumpkin(t):

    mu,var = thinkstats.MeanVar(t)

    print '均值:', mu
    print '方差:', var
    print '标准差:', var ** 0.5

    

pumpkins = [1,1,1,3,3,591]

Pumpkin( pumpkins )
