# LipNet: End-to-End Sentence-level Lipreading

---

Gluon inplementation of [LipNet: End-to-End Sentence-level Lipreading] (https://arxiv.org/abs/1611.01599)

## Requirements
- Python 3.6.4
- MXnet 1.3.0


## Test Environment
- 4 cores
- 1 GPU (Tesla K80)


## Data Structure

```
The training data folder should look like : 
<train_data_root>
                |--datasets
                        |--s1
                           |--bbir7s
                               |--mouth_000.png
                               |--mouth_001.png
                                   ...
                           |--bgaa8p
                               |--mouth_000.png
                               |--mouth_001.png
                                  ...
                        |--s2
                            ...
                 |--align
                         |--bw1d8a.align
                         |--bggzzs.align
                             ...

```
