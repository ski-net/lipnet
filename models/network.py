import numpy as np
import mxnet as mx
from mxnet import gluon, autograd ,nd
from mxnet.gluon import nn, rnn,utils
import mxnet.ndarray as F

class LipNet(nn.Block):
    def __init__(self,dr_rate, **kwargs):
        super(LipNet, self).__init__(**kwargs)
        
        with self.name_scope():
            self.conv1 = nn.Conv3D(32,kernel_size=(3,5,5),strides=(1,2,2),padding=(1,2,2))
            #self.bn1 = nn.BatchNorm()
            self.bn1 = nn.InstanceNorm(in_channels=32)
            self.dr1 = nn.Dropout(dr_rate)
            self.pool1 = nn.MaxPool3D((1,2,2),(1,2,2))
            
            self.conv2 = nn.Conv3D(64,kernel_size=(3,5,5),strides=(1,1,1),padding=(1,2,2))
            #self.bn2 = nn.BatchNorm()
            self.bn2 = nn.InstanceNorm(in_channels=64)
            self.dr2 = nn.Dropout(dr_rate)
            self.pool2 = nn.MaxPool3D((1,2,2),(1,2,2))
            
            self.conv3 = nn.Conv3D(96,kernel_size=(3,3,3),strides=(1,1,1),padding=(1,2,2))
            #self.bn3 = nn.BatchNorm()
            self.bn3 = nn.InstanceNorm(in_channels=96)
            self.dr3 = nn.Dropout(dr_rate)
            self.pool3 = nn.MaxPool3D((1,2,2),(1,2,2))
            
            self.gru1 = rnn.GRU(256,bidirectional=True)
            self.gru2 = rnn.GRU(256,bidirectional=True)
            
            self.dense = nn.Dense(27+1,flatten=False)
            
    def summary(self,desc,out):
        print("=======================================")
        print("{d} shape : {o}".format(d=desc,o=out.shape))
            
            
    def forward(self, x):
        out = self.conv1(x)
        out = self.bn1(out)
        out = F.relu(out)
        out = self.dr1(out)
        out = self.pool1(out)
        
        out = self.conv2(out)
        out = self.bn2(out)
        out = F.relu(out)
        out = self.dr2(out)
        out = self.pool2(out)
        
        out = self.conv3(out)
        out = self.bn3(out)
        out = F.relu(out)
        out = self.dr3(out)
        out = self.pool3(out)
        
        out = nd.transpose(out,(2,0,1,3,4))
        #out = out.swapaxes(1,2)
        out = out.reshape((out.shape[0],out.shape[1],-1))
        out = self.gru1(out)
        out = self.gru2(out)
        out = self.dense(out)
        out = F.log_softmax(out,axis=2)
        #out = out.swapaxes(0,1)
        out = nd.transpose(out,(1,0,2))
        
        return out
