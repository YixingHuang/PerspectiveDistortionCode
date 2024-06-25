import os
os.environ["CUDA_VISIBLE_DEVICES"]="1"


cmd22 = 'python train.py --vit_name R50-ViT-B_16 --n_skip 3   --dataset 0and90PolarTraining --img_size 512 --batch_size 12 --gpu cuda:0'
cmd23 = 'python test.py --vit_name R50-ViT-B_16 --n_skip 3   --dataset 0and90PolarTraining --img_size 512 --batch_size 12 --is_savenii --gpu cuda:0'

cmd24 = 'python train.py --vit_name R50-ViT-B_16 --n_skip 3   --dataset 0Training --img_size 512 --batch_size 12 --gpu cuda:0'
cmd25 = 'python test.py --vit_name R50-ViT-B_16 --n_skip 3   --dataset 0Training --img_size 512 --batch_size 12 --is_savenii --gpu cuda:0'
cmds = [cmd24, cmd25]
for cmd in cmds:
    os.system(cmd)