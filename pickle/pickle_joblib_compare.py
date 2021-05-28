import time
import pickle
import joblib as jl

def get_big_dict():
    d = {}
    for i in range(10000000):
        key = 'k'+str(i)
        value = i
        d[key]=value


def test_pickle_dump_load_big_dict(d):
    dump_time_cost_list = []
    load_time_cost_list = []
    for i in range(100):
        # dump
        t1 = time.time()
        fw = open('tmpfile.bin','wb')
        pickle.dump(d, fw)
        fw.close()
        t2 = time.time()
        # load
        fr = open('tmpfile.bin','rb')
        d2 = pickle.load(fr)
        fr.close()
        t3 = time.time()
        dump_time_cost_list.append(t2-t1)
        load_time_cost_list.append(t3-t2)
    print('pickle dump time cost ave: {0}'.format(sum(dump_time_cost_list)/len(dump_time_cost_list)))
    print('pickle load time cost ave: {0}'.format(sum(load_time_cost_list)/len(load_time_cost_list)))


def test_joblib_dump_load_big_dict(d):
    dump_time_cost_list = []
    load_time_cost_list = []
    for i in range(100):
        # dump
        t1 = time.time()
        jl.dump(d, 'tmpfile.bin')
        t2 = time.time()
        # load
        d2 = jl.load('tmpfile.bin')
        t3 = time.time()
        dump_time_cost_list.append(t2-t1)
        load_time_cost_list.append(t3-t2)
    print('joblib dump time cost ave: {0}'.format(sum(dump_time_cost_list)/len(dump_time_cost_list)))
    print('joblib load time cost ave: {0}'.format(sum(load_time_cost_list)/len(load_time_cost_list)))



if __name__=='__main__':
    d = get_big_dict()
    test_pickle_dump_load_big_dict(d)
    test_joblib_dump_load_big_dict(d)



'''
python 3.6
pickle dump time costed: 0.0035102367401123047
pickle load time costed: 0.0010020732879638672
joblib dump time costed: 0.0030083656311035156
joblib load time costed: 0.0015039443969726562

conclusion:
1. pickle faster than joblib for big dict
2. total test time cost ~20s
'''