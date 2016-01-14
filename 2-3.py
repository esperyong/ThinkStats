# -*- coding: utf-8 -*-
from tools import Pmf as pmf 
from first import get_first_birth_and_other
from matplotlib import pyplot


if __name__ == '__main__':
    hist = pmf.MakeHistFromList( [1,2,2,2,3,3,5,6] )
    print pmf.Mode(hist)
    print pmf.AllModes( hist )

    first_birth_list,other_birth_list = get_first_birth_and_other()

    first_hist = pmf.MakeHistFromList( first_birth_list )
    other_hist = pmf.MakeHistFromList( other_birth_list )

    vals,freqs = first_hist.Render() 
    rectangles = pyplot.bar(vals,freqs)   
    pyplot.show()

