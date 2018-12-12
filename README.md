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
                        |--images
                           |--trainval
                              |--ZzugJPASNB8
                                 |--50001
                                    |--mouth_000.png
                                       ...
                           |--test
                               ...
                        |--npy
                           |--data_sizes_py.npy
                           |--file_id_feature_size.npy
                           |--file_key_p3.npy
                           |--speech_text_dict_p3.npy
                           |--speech_text_pad_dict_p3.npy

```
