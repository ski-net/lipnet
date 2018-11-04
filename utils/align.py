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