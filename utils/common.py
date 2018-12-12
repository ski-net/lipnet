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

import numpy as np

def char2int(char):
    if char >= 'a' and char <= 'z':
        return ord(char) - ord('a')
    elif char == ' ':
        return 26
    
def int2char(num):
    if num >= 0 and num < 26:
        return chr(num + ord('a'))
    elif num == 26:
        return ' '

def word_to_vector(word):
    vector = []
    for c in list(word):
        vector.append(char2int(c))
    return vector

def vector_to_word(vector):
    word = ""
    for x in vector:
        word = word + int2char(x)
    return word


def char_conv(out):
    out_conv = list()
    for i in range(out.shape[0]):
        tmp_str = ''
        for j in range(out.shape[1]):
            if int(out[i][j]) >=0:
                tmp_char = int2char(int(out[i][j]))
                if int(out[i][j]) == 27:
                    tmp_char = ''
                tmp_str = tmp_str+tmp_char
        out_conv.append(tmp_str)
    return out_conv



