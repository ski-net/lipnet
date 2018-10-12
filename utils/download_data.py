from multi import multi_p_run, put_worker, _worker

def download_mp4(from_idx, to_idx):
    import os
    succ = set()
    fail = set()
    for idx in range(from_idx, to_idx):
        try:
            name = 's' + str(idx)
            script = "http://spandh.dcs.shef.ac.uk/gridcorpus/{nm}/video/{nm}.mpg_vcd.zip".format(nm=name)
            down_script = 'cd ../datasets && curl {script} --output {nm}.mpg_vcd.zip && unzip {nm}.mpg_vcd.zip'.format(script=script, nm=name)
            print (down_script)
            os.system(down_script)
            succ.add(idx)
        except:
            fail.add(idx)
    return (succ, fail)

def download_align(from_idx, to_idx):
    import os
    succ = set()
    fail = set()
    for idx in range(from_idx, to_idx):
        try:
            name = 's' + str(idx)
            script = "http://spandh.dcs.shef.ac.uk/gridcorpus/{nm}/align/{nm}.tar".format(nm=name)
            down_script = 'cd ../datasets && wget {script} && tar -xvf {nm}.tar'.format(script=script, nm=name)
            print (down_script)
            os.system(down_script)
            succ.add(idx)
        except:
            fail.add(idx)
    return (succ, fail)


if __name__ == '__main__':
    #res = multi_p_run(35, put_worker, _worker, 5)
    res = multi_p_run(5, put_worker, download_mp4, 7)    
    print (res)

    res = multi_p_run(35, put_worker, download_align, 7)
    print (res)

    os.system('rm -f datasets/*.zip && rm -f datasets/*/Thumbs.db')
    os.system('rm -f datasets/*.tar && rm -f datasets/align/Thumbs.db')

