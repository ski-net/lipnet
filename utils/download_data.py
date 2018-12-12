# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

from multi import multi_p_run, put_worker, _worker

def download_mp4(from_idx, to_idx, params):
    import os
    succ = set()
    fail = set()
    for idx in range(from_idx, to_idx):
        try:
            name = 's' + str(idx)
            script = "http://spandh.dcs.shef.ac.uk/gridcorpus/{nm}/video/{nm}.mpg_vcd.zip".format(nm=name)
            down_script = 'cd {src_path} && curl {script} --output {nm}.mpg_vcd.zip && unzip {nm}.mpg_vcd.zip'.format( \
                script=script, nm=name, src_path=params['src_path'])
            print (down_script)
            os.system(down_script)
            succ.add(idx)
        except Exception as e:
            print (e)
            fail.add(idx)
    return (succ, fail)

def download_align(from_idx, to_idx, params):
    import os
    succ = set()
    fail = set()
    for idx in range(from_idx, to_idx):
        try:
            name = 's' + str(idx)
            script = "http://spandh.dcs.shef.ac.uk/gridcorpus/{nm}/align/{nm}.tar".format(nm=name)
            down_script = 'cd {align_path} && wget {script} && tar -xvf {nm}.tar'.format(script=script, \
                          nm=name,  \
                          align_path=params['align_path'])
            print (down_script)
            os.system(down_script)
            succ.add(idx)
        except Exception as e:
            print (e)
            fail.add(idx)
    return (succ, fail)


if __name__ == '__main__':
    import argparse
    import os
    from os.path import exists
    parser = argparse.ArgumentParser()
    parser.add_argument('--src_path', type=str, default='../data/mp4s')
    parser.add_argument('--align_path', type=str, default='../data')
    config = parser.parse_args()    
    params = {'src_path':config.src_path, 'align_path':config.align_path}
    
    if exists('./shape_predictor_68_face_landmarks.dat') is False:
        os.system('wget http://dlib.net/files/shape_predictor_68_face_landmarks.dat.bz2 && bzip2 -d shape_predictor_68_face_landmarks.dat.bz2')
    
    ## download movie files
    os.makedirs('{src_path}'.format(src_path=params['src_path']), exist_ok=True)
    res = multi_p_run(tot_num=35, _func=put_worker, worker=download_mp4, params=params, n_process=5)    
    print (res)

    ## download align files
    res = multi_p_run(tot_num=35, _func=put_worker, worker=download_align, params=params, n_process=5)
    print (res)

    os.system('rm -f {src_path}/*.zip && rm -f {src_path}/*/Thumbs.db'.format(src_path=params['src_path']))
    os.system('rm -f {align_path}/*.tar && rm -f {align_path}/Thumbs.db'.format(align_path=params['align_path']))