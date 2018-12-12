import sys
import numpy as np
import mxnet as mx
from mxnet import gluon, autograd ,nd
import mxnet.ndarray as F
from mxnet.gluon.data.vision import transforms
from models.network import LipNet
from data_loader import LipsDataset
from tqdm import tqdm, trange
from BeamSearch import ctcBeamSearch
from utils.common import *


# set gpu count
def setting_ctx(use_gpu):
    if (use_gpu):
        ctx = mx.gpu()
    else :
        ctx = mx.cpu()
    return ctx


alphabet_encoding = ''
for i in range(27):
    alphabet_encoding += int2char(i)

def char_beam_search(out):
    out_conv = list()
    for i in range(out.shape[0]):
        probs = out[i]
        prob = probs.softmax().asnumpy()
        line_string_proposals = ctcBeamSearch(prob, alphabet_encoding, None, k=4, beamWidth=25)
        out_conv.append(line_string_proposals[0])
    return out_conv

class Train(object):
    def __init__(self, config):
        ##setting hyper-parameters
        self.batch_size = config.batch_size
        self.epochs = config.epochs
        self.image_path = config.image_path
        self.align_path = config.align_path
        self.dr_rate = config.dr_rate
        self.use_gpu = config.use_gpu
        self.ctx = setting_ctx(self.use_gpu)
        self.num_workers = config.num_workers
        self.build_model()
        
    
    def build_model(self):
        #set network
        self.net = LipNet(self.dr_rate)
        self.net.initialize(ctx=self.ctx)
        #set optimizer
        self.loss_fn = gluon.loss.CTCLoss()
        self.trainer = gluon.Trainer(self.net.collect_params(),optimizer='adam',optimizer_params={'learning_rate':1e-4,'beta1':0.9,'beta2':0.999})
        
    def save_model(self,e,i,current_loss):
        file_name = "checkpoint/best_model_epoches_"+str(e)+"iter_"+str(i)+"loss_"+str(round(current_loss,2))
        self.net.save_params(file_name)
    
    def train(self):
        input_transform  = transforms.Compose([transforms.ToTensor()
                                    , transforms.Normalize((0.7136,0.4906,0.3283),(0.1138,0.1078,0.0917))
                                 ])
        training_dataset = LipsDataset(self.image_path,self.align_path,transform=input_transform)
        
        train_dataloader = mx.gluon.data.DataLoader(training_dataset, batch_size=self.batch_size, shuffle=True,num_workers=self.num_workers)
        
        best_loss = sys.maxsize
        
        for e in trange(self.epochs):
            i = 0;
            for input_data, label in tqdm(train_dataloader):
                input_data = nd.transpose(input_data,(0,2,1,3,4))
                input_data = input_data.copyto(self.ctx)
                label = label.copyto(self.ctx)
                #print(input_data.shape)
                #print(label.shape)
        
                with autograd.record():
                    with autograd.train_mode():
                        out = self.net(input_data)
            
                        loss_val = self.loss_fn(out,label)
                        loss_val.backward()
                self.trainer.step(input_data.shape[0])
        
                if i % 20 == 0:
                    print("epoch:{e} iter:{i} loss:{l}".format(e=e,i=i,l=loss_val.mean().asscalar()))
                    self.infer(input_data, label)
                    current_loss = loss_val.mean().asscalar()
                    if best_loss > current_loss:
                        self.save_model(e,i,current_loss)
                        best_loss = current_loss
                i +=1
                
    def infer(self, input_data, label):
        pred = self.net(input_data)
        pred_convert = char_beam_search(pred)
        
        label_convert = char_conv(label.asnumpy())
        for t,p in zip(label_convert,pred_convert):
            print("target:{t}  pred:{p}".format(t=t,p=p))
        
        
        
        
        
