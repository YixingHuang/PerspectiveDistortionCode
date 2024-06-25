import os
os.environ["CUDA_VISIBLE_DEVICES"]="0"


cmd26 = 'python train.py --vit_name R50-ViT-B_16 --n_skip 3   --dataset kneeDual --img_size 512 --batch_size 10 --list_dir ./lists/lists_knee'
cmd27 = 'python test.py --vit_name R50-ViT-B_16 --n_skip 3   --dataset kneeDual --img_size 512 --batch_size 10 --is_savenii --list_dir ./lists/lists_knee'


cmds = [cmd26, cmd27]
for cmd in cmds:
    os.system(cmd)