from PIL import Image
import numpy as np
class Canvas():
    
    def __init__(self,height,width,color):
        self.height=height
        self.width=width
        self.color=color
        # 3d Numpy array of zeroes
        self.data=np.zeros((self.height,self.width,3),dtype=np.uint8)
        #changing[0,0,0] with user given values of color
        self.data[:] =self.color
    def make(self,imagepath):
        img=Image.fromarray(self.data,'RGB')
        img.save(imagepath)