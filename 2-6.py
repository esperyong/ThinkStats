# -*- coding: utf-8 -*-

from first import (get_all_preg_pmf,
                   get_first_preg_pmf,
                   get_other_preg_pmf)

from tools import risk

if __name__ == '__main__':
    all_pmf = get_all_preg_pmf()
    first_pmf = get_first_preg_pmf()
    other_pmf = get_other_preg_pmf()

    print '/***==========================***/'

    print '提前出生===>', risk.ProbEarly(all_pmf)
    print '足月正常出生===>', risk.ProbOnTime(all_pmf)
    print '晚生===>', risk.ProbLate(all_pmf)

    print '/***==========================***/'

    print '头胎提前出生===>', risk.ProbEarly(first_pmf)
    print '头胎足月正常出生===>', risk.ProbOnTime(first_pmf)
    print '头胎晚生===>', risk.ProbLate(first_pmf)

    print '/***==========================***/'

    print '非头胎提前出生===>', risk.ProbEarly(other_pmf)
    print '非头胎足月正常出生===>', risk.ProbOnTime(other_pmf)
    print '非头胎晚生===>', risk.ProbLate(other_pmf)

    print '/***==========================***/'

