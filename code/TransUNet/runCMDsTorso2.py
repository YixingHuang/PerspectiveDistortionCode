import os
os.environ["CUDA_VISIBLE_DEVICES"]="1"


cmd26 = 'python train.py --vit_name R50-ViT-B_16 --n_skip 3   --dataset TorsoDualTraining2Crop --img_size 512 --batch_size 12 --list_dir ./lists/lists_torso'
cmd27 = 'python test.py --vit_name R50-ViT-B_16 --n_skip 3   --dataset TorsoDualTraining2Crop --img_size 512 --batch_size 12 --is_savenii --list_dir ./lists/lists_torso'


cmds = [cmd26, cmd27]
for cmd in cmds:
    os.system(cmd)