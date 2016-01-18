# -*- coding: utf-8 -*-
from tools import survey
from tools import Pmf as pmf 

def load_table():
    table = survey.Pregnancies()
    table.ReadRecords()
    return table

def get_live_babies():
    table = load_table()
    return [record for record in table.records if record.outcome == 1]

def get_pregnancies():
    table = load_table()
    return table.records

def get_first_birth_and_other():
    live_babies = get_live_babies()
    first_birth_list = []
    other_birth_list = []
    for live_baby in live_babies: 
        if live_baby.birthord == 1:
            first_birth_list.append(live_baby.prglength) 
        else:
            other_birth_list.append(live_baby.prglength) 
    return (first_birth_list,other_birth_list)


def get_first_preg_pmf():
    live_babies = get_live_babies()
    first_birth_list = [live_baby.prglength for live_baby in live_babies if live_baby.birthord == 1]
    return pmf.MakePmfFromList( first_birth_list )

def get_other_preg_pmf():
    live_babies = get_live_babies()
    other_birth_list = [live_baby.prglength for live_baby in live_babies if live_baby.birthord != 1]
    return pmf.MakePmfFromList( other_birth_list )

def get_all_preg_pmf():
    values = [live_baby.prglength for live_baby in get_live_babies()]
    return pmf.MakePmfFromList( values )

if __name__ == '__main__':
    #怀孕总数
    print 'Number or pregnancies:', len(get_pregnancies())
    
    #活婴的数量
    live_babies = get_live_babies()
    print 'Number of live pregnancies:', len(live_babies)
    
    
    first_birth_list,other_birth_list = get_first_birth_and_other()
    first_birth_num = len(first_birth_list)
    other_birth_num = len(other_birth_list)
    
    print 'Number of live first pregnancies:', first_birth_num
    
    print 'Number of live nonfirst pregnancies:', other_birth_num
    
    first_total = reduce(lambda x, y: x+y, [ first_birth for first_birth in first_birth_list])
    print float(first_total)/float(first_birth_num)
    
    nonfirst_total = reduce(lambda x, y: x+y, [ nonfirst_birth for nonfirst_birth in other_birth_list])
    print float(nonfirst_total)/float(other_birth_num)




