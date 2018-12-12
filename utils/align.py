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

from .common import *
import numpy

class Align(object):
    skip_list = ['sil', 'sp']

    def __init__(self, align_path):
        self.build(align_path)

    def build(self, align_path):
        f = open(align_path, 'r')
        lines = f.readlines()
        f.close()
        # words: list([op, ed, word])
        words = []
        for line in lines:
            op, ed, word = line.strip().split(' ')
            if(not word in Align.skip_list):
                words.append((int(op), int(ed), word))


        self.words = words
        self.n_words = len(words)
        self.sentence_str = " ".join([w[2] for w in self.words])
        self.sentence_length = len(self.sentence_str)

    def sentence(self, padding=75):
        v = word_to_vector(self.sentence_str)
        v += [-1] * (padding - self.sentence_length)
        return np.array(v, dtype=np.int32)

    def word(self, id, padding=75):
        word = self.words[id][2]
        v = word_to_vector(word)
        v += [-1] * (padding - len(v))
        return np.array(v, dtype=np.int32)

    def word_length(self, id):
        return len(self.words[id][2])

    def word_frame_pos(self, id, frames):
        left = int(self.words[id][0]/1000)
        right = max(left+1,int(self.words[id][1]/1000))
        return (left, right)