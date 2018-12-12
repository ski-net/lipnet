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


## Training

- arguments
  - batch_size : Define batch size (defualt=64)
  - epoches : Define total epoches (default=50)
  - GPU_COUNT : Use GPU count (default=2)

## Results
```
[Target]
['set white in t three soon',
 'lay red in p two please',
 'set red at e six now',
 'bin red in c four now',
 'lay white in h seven soon',
 'bin white at m three please',
 'bin white with t six again',
 'lay red in q three again',
 'place white in p two again',
 'bin green at l three please',
 'set blue by g nine now',
 'bin green with l three soon',
 'lay green with r six please',
 'set green with n six now',
 'set white at v one again',
 'bin red with m seven now',
 'lay white by y one again',
 'set green by c six soon',
 'lay green in c nine again',
 'set green in s four soon',
 'lay green in l one please',
 'bin white at e eight soon',
 'set white with c three again',
 'bin blue at x two again',
 'set blue by a seven soon',
 'bin green with g seven now',
 'set blue in q six please',
 'set red in r one please',
 'lay green by k nine now',
 'lay green by j five now',
 'set blue with r seven please',
 'bin white by e nine now',
 'lay blue at j three again',
 'bin white by f three now',
 'set white in f zero again',
 'set red by s two please',
 'set white at a six please',
 'set blue by z six soon',
 'set white in r nine again',
 'place red in t nine soon',
 'bin white with n seven soon',
 'set white with a seven soon',
 'set blue by g three again',
 'bin blue with k two now',
 'place blue by a nine again',
 'place red in h one again',
 'set blue in e seven soon',
 'lay white with l six now']
 ```
 
 ```
[Pred]
['set   white    in   t  three   soon',
 'llay  rreeed   it   p  thro  please',
 'set   rreeed   an   z  six   nnow',
 'bin   rreeed   in   c  four    now',
 'llay  white    in   h  seven  soon',
 'bin   white    at   m  three  please',
 'bin   white   witt   t  six   again',
 'llay  rreeed   in   q  three   again',
 'place white    an   p  two   again',
 'bin   green   at   l  three  please',
 'set   blue    by   g  nine    now',
 'bin   green  with   l  three   soon',
 'llayy green  with   r  eix  please',
 'set   green  with   s  six   nnow',
 'set   white    at   t one   again',
 'bin   rreeed  with   m  seven   now',
 'llay  white    by   p  one   again',
 'set   green   by   c  six   soon',
 'llay  green   in   c  nine   again',
 'set   green   in   s  four   soon',
 'llay  green   in   l one  please',
 'bin   white    at   d  eight   soon',
 'set   white   witth   g  three   again',
 'bin   blue    at   q  two   again',
 'set   blue    by   a  seven  soon',
 'bin   green  witth   g  seven   now',
 'set   blue    at   q  six  please',
 'set   rreen   ith   e one  please',
 'plac  breed   an   i  ine    now',
 'llayy green   by   j  five    now',
 'set   blue   wih   o  seven please',
 'bin   white    by   e  nine    now',
 'llay  blue    at   g  hree   again',
 'bin   white    by   f  three    now',
 'set   white    in   f  zero   again',
 'set   rreeed   by   f  two  please',
 'set   white    at   a  six  please',
 'set   blue    by   z  six   soon',
 'set   white    in   r  nine   again',
 'place rreeed   an   t  nine   soon',
 'bin   rreeed  with   h  seven  soon',
 'set   white   with   s  seven  soon',
 'set   blue    by   g  three   again',
 'bin   blue   with   x  two   nnow',
 'place blue    by   n  nine   again',
 'place rreeed   in   h one   again',
 'set   blue    in   e  seven  soon',
 'llay  white   witth   s  six    now']
 ```
  
## Reference
- https://github.com/kimhc6028/relational-networks
  - show_status : show loss and accuracy for each epoch (default=True)
