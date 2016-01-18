# -*- coding: utf-8 -*-

def ProbRange(pmf, 
              prglength_min=None,
              prglength_max=None):

    prob_result = 0.0

    if prglength_min is not None and prglength_max is None:
        for prglength,prob in pmf.Items():
            if prglength >= prglength_min:
                prob_result = prob_result + prob

    elif prglength_min is None and prglength_max is not None:
        for prglength,prob in pmf.Items():
            if prglength <= prglength_max:
                prob_result = prob_result + prob

    elif prglength_min is not None and prglength_max is not None:
        for prglength,prob in pmf.Items():
            if prglength >= prglength_min and prglength <= prglength_max:
                prob_result = prob_result + prob

    return prob_result

def ProbEarly(pmf):
    return ProbRange(pmf,prglength_max=37)

def ProbOnTime(pmf):
    return ProbRange(pmf,prglength_min=38,prglength_max=40)

def ProbLate(pmf):
    return ProbRange(pmf,prglength_min=41)


