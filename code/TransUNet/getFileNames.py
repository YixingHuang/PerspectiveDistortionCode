import os
import glob
import re


label_path = 'C:/MachineLearning/pytorch-CycleGAN-and-pix2pix/datasets/THz/testRGB/*.png'
# label_path = 'C:/TruncationUKER/recon2DslicesD20/test/*.tif'
label_names = glob.glob(label_path)

for name in label_names:
    basename = os.path.basename(name)
    print(basename[:-4])