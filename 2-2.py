# -*- coding: utf-8 -*-
from tools import survey
from tools import thinkstats
from first import get_first_birth_and_other

first_birth_list,other_birth_list = get_first_birth_and_other()


print 'Number or 第一胎:', len(first_birth_list)
print 'Number or 非第一胎:', len(other_birth_list)

t1 = [first_birth.prglength for first_birth in first_birth_list ]
t2 = [other_birth.prglength for other_birth in other_birth_list ]

var1 = thinkstats.Var(t1)

var2 = thinkstats.Var(t2)

print '第一胎婴儿怀孕周期标准差:',var1 ** 0.5

print '非第一胎婴儿怀孕周期标准差:',var2 ** 0.5


