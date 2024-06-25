import os
import glob
import re

folder = 'C:/MachineLearning/TransUNet/datasets/cephalo600PolarTraining/'
label_path = 'C:/MachineLearning/TransUNet/datasets/cephalo600PolarTraining/*.png'
label_names = glob.glob(label_path)

for name in label_names:
    basename = os.path.basename(name)
    id = int(basename[:-4]) - 5000
    print(id)
    newName = folder + str(id) + ".png"
    os.rename(name, newName)