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

#def char2int(char):
#    if(char == ' '):
#        return 27
#    return ord(char)-ord('a')+1
    
#def int2char(num):
#    if(num == 27):
#        return ' '
#    return chr(ord('a')+num-1)

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



