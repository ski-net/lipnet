def multi_p_run(tot_num, _func, worker, n_process):
    from multiprocessing import Process, Queue
    import math

    out_q = Queue()
    procs = []
    
    split_num = split_seq(list(range(0, tot_num)), n_process) # start 0

    print (tot_num, ">>", split_num)

    for i in range(n_process):
        p = Process(
                target=_func,
                args=(worker, split_num[i][0], split_num[i][1], out_q))
        #p.daemon = True
        procs.append(p)
        p.start()

    try:
        result = []
        for i in range(n_process):
            result.append(out_q.get())
        for i in procs:
            i.join()
    except KeyboardInterrupt as e:
        print ('Killing all the childer in the pool.')
        for i in procs:
            i.terminate()
            i.join()
        return -1

    while not out_q.empty():
        print (out_q.get(block=False))

    return result

def split_seq(sam_num, n_tile):
    import math
    print (sam_num)
    print (n_tile)
    start_num = sam_num[0::int(math.ceil(len(sam_num) / (n_tile)))]
    end_num = start_num[1::]
    end_num.append(len(sam_num))
    return [[i,j] for i, j in zip(start_num, end_num)]

def put_worker(func, from_idx, to_idx, out_q):
    succ, fail = func(from_idx, to_idx)
    return out_q.put({'succ':succ, 'fail':fail})

def _worker(from_idx, to_idx):
    succ = set()
    fail = set()
    for idx in range(from_idx, to_idx):
        try:
            succ.add(idx)
        except:
            fail.add(idx)
    return (succ, fail)


if __name__ == '__main__':
    res = multi_p_run(35, put_worker, _worker, 5)
    print (res)   

