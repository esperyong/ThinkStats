# -*- coding: utf-8 -*-
from tools import Pmf as pmf 
from first import get_first_birth_and_other

def PmfMean(pmf):
    return sum([v*p for v,p in pmf.Items()])

def PmfVar(pmf,mean=None):
    if mean is None:
        mean = PmfMean(pmf)
    return sum( [p * ( (v-mean)**2 ) for v,p in pmf.Items()] )

if __name__ == '__main__':
    first_birth_list,other_birth_list = get_first_birth_and_other()

    pmf = pmf.MakePmfFromList(first_birth_list)
    mean = PmfMean(pmf)
    print 'PmfMean',mean
    print 'Mean',pmf.Mean()

    print 'PmfVar',PmfVar(pmf,mean)
    print 'Var',pmf.Var()
        
