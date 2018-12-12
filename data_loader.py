import os
import sys
import glob
from mxnet import nd
import mxnet.gluon.data.dataset as dataset
from mxnet.gluon.data.vision.datasets import image
from align import Align


class LipsDataset(dataset.Dataset):
    def __init__(self, root, align_root, flag=1, transform=None):
        self._root = os.path.expanduser(root)
        self._align_root = align_root
        self._flag = flag
        self._transform = transform
        self._exts = ['.jpg', '.jpeg', '.png']
        self._list_images(self._root)

    def _list_images(self, root):
        self.labels = []
        self.items = []
        
        folder_path = glob.glob(os.path.join(root, "*","*"))
    
        for folder in folder_path:
            label_index = os.path.split(folder)[-1]
            filename = glob.glob(os.path.join(folder, "*"))
            filename.sort()
            label = os.path.split(folder)[-1]
            self.items.append((filename, label))
            
    def align_generation(self,file_nm,padding=75):
        align = Align(self._align_root+file_nm+'.align')
        return nd.array(align.sentence(padding))
    
    def __getitem__(self, idx):
        img = list()
        for image_name in self.items[idx][0]:
            tmp_img = image.imread(image_name, self._flag)
            if self._transform is not None:
                tmp_img =  self._transform(tmp_img)
            img.append(tmp_img)
        img = nd.stack(*img)
        #print(self.items[idx][0][0])
        label = self.align_generation(self.items[idx][1])
        return img, label

    def __len__(self):
        return len(self.items)
    