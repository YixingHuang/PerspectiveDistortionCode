import os
import random
import h5py
import numpy as np
import torch
from scipy import ndimage
from scipy.ndimage.interpolation import zoom
from torch.utils.data import Dataset
from PIL import Image

def random_rot_flip(image, label):
    k = np.random.randint(0, 4)
    image = np.rot90(image, k)
    label = np.rot90(label, k)
    axis = np.random.randint(0, 2)
    image = np.flip(image, axis=axis).copy()
    label = np.flip(label, axis=axis).copy()
    return image, label


def random_rotate(image, label):
    angle = np.random.randint(-20, 20)
    image = ndimage.rotate(image, angle, order=0, reshape=False)
    label = ndimage.rotate(label, angle, order=0, reshape=False)
    return image, label


def format_data(sample):
        image, label = sample['image'], sample['label']

        # if random.random() > 0.5:
        #     image, label = random_rot_flip(image, label)
        # elif random.random() > 0.5:
        #     image, label = random_rotate(image, label)
        # x, y, z = image.shape
        image = torch.from_numpy(image.astype(np.float32))
        label = torch.from_numpy(label.astype(np.float32))
        image = image.permute(2, 0, 1)
        label = label.permute(2, 0, 1)
        sample = {'image': image, 'label': label}
        return sample


class Synapse_dataset(Dataset):
    def __init__(self, base_dir, list_dir, split, transform=None):
        self.transform = transform  # using transform in torch!
        self.split = split
        self.sample_list = open(os.path.join(list_dir, self.split+'.txt')).readlines()
        self.data_dir = base_dir

    def __len__(self):
        return len(self.sample_list)

    # def __getitem__(self, idx):
    #     if self.split == "train":
    #         slice_name = self.sample_list[idx].strip('/n')
    #         data_path = os.path.join(self.data_dir, slice_name+'.npz')
    #         data = np.load(data_path)
    #         image, label = data['image'], data['label']
    #     else:
    #         vol_name = self.sample_list[idx].strip('/n')
    #         filepath = self.data_dir + "/{}.npy.h5".format(vol_name)
    #         data = h5py.File(filepath)
    #         image, label = data['image'][:], data['label'][:]
    #
    #     sample = {'image': image, 'label': label}
    #     if self.transform:
    #         sample = self.transform(sample)
    #     sample['case_name'] = self.sample_list[idx].strip('/n')
    #     return sample
    def __getitem__(self, idx):
        slice_name = self.sample_list[idx].strip('\n')
        data_path = os.path.join(self.data_dir, slice_name + '.png')
        AB = Image.open(data_path).convert('RGB')
        # split AB image into A and B
        w, h = AB.size
        w2 = int(w / 2)
        image = AB.crop((0, 0, w2, h))
        label = AB.crop((w2, 0, w, h))
        image = np.array(image)/255.0
        label = np.array(label)/255.0

        sample = {'image': image, 'label': label}

        sample = format_data(sample)
        sample['case_name'] = self.sample_list[idx].strip('\n')
        return sample
#
# # For Tiff
# class Synapse_dataset(Dataset):
#     def __init__(self, base_dir, list_dir, split, transform=None):
#         self.transform = transform  # using transform in torch!
#         self.split = split
#         self.sample_list = open(os.path.join(list_dir, self.split+'.txt')).readlines()
#         self.data_dir = base_dir
#
#     def __len__(self):
#         return len(self.sample_list)
#
#     # def __getitem__(self, idx):
#     #     if self.split == "train":
#     #         slice_name = self.sample_list[idx].strip('/n')
#     #         data_path = os.path.join(self.data_dir, slice_name+'.npz')
#     #         data = np.load(data_path)
#     #         image, label = data['image'], data['label']
#     #     else:
#     #         vol_name = self.sample_list[idx].strip('/n')
#     #         filepath = self.data_dir + "/{}.npy.h5".format(vol_name)
#     #         data = h5py.File(filepath)
#     #         image, label = data['image'][:], data['label'][:]
#     #
#     #     sample = {'image': image, 'label': label}
#     #     if self.transform:
#     #         sample = self.transform(sample)
#     #     sample['case_name'] = self.sample_list[idx].strip('/n')
#     #     return sample
#     def __getitem__(self, idx):
#         slice_name = self.sample_list[idx].strip('\n')
#         data_path = os.path.join(self.data_dir, slice_name + '.tif')
#         AB = Image.open(data_path)
#         # split AB image into A and B
#         w, h = AB.size
#         w2 = int(w / 2)
#         image = AB.crop((0, 0, w2, h))
#         label = AB.crop((w2, 0, w, h))
#         image = np.array(image)
#         label = np.array(label)
#         image = np.reshape(image, (h, w2, 1))
#         label = np.reshape(label, (h, w2, 1))
#         # image = np.swapaxes(image, 0, 2)
#         # label = np.swapaxes(label, 0, 2)
#         sample = {'image': image, 'label': label}
#
#         # saveImageName = 'C:/MachineLearning/model/predictions/TU_beadphantom224224/TU_pretrain_R50-ViT-B_16_skip3_epo150_bs2_224/' \
#         #                 + self.sample_list[idx].strip('\n') + '_label_load.png'
#         # temp = (label * 255).astype(np.uint8)
#         # img = Image.fromarray(temp, 'RGB')
#         # img.save(saveImageName)
#
#         sample = format_data(sample)
#         sample['case_name'] = self.sample_list[idx].strip('\n')
#         return sample

