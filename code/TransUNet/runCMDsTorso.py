import os
os.environ["CUDA_VISIBLE_DEVICES"]="0"


cmd26 = 'python train.py --vit_name R50-ViT-B_16 --n_skip 3   --dataset TorsoDualPolarTrainingCrop --img_size 512 --batch_size 12 --list_dir ./lists/lists_torso'
cmd27 = 'python test.py --vit_name R50-ViT-B_16 --n_skip 3   --dataset TorsoDualPolarTrainingCrop --img_size 512 --batch_size 12 --is_savenii --list_dir ./lists/lists_torso'

cmd28 = 'python train.py --vit_name R50-ViT-B_16 --n_skip 3   --dataset TorsoSingleTrainingCrop --img_size 512 --batch_size 12 --list_dir ./lists/lists_torso'
cmd29 = 'python test.py --vit_name R50-ViT-B_16 --n_skip 3   --dataset TorsoSingleTrainingCrop --img_size 512 --batch_size 12 --is_savenii --list_dir ./lists/lists_torso'

cmd30 = 'python train.py --vit_name R50-ViT-B_16 --n_skip 3   --dataset TorsoDualTrainingCropPlus --img_size 512 --batch_size 12 --list_dir ./lists/lists_torso'
cmd31 = 'python test.py --vit_name R50-ViT-B_16 --n_skip 3   --dataset TorsoDualTrainingCropPlus --img_size 512 --batch_size 12 --is_savenii --list_dir ./lists/lists_torso'

cmds = [cmd30, cmd31]
for cmd in cmds:
    os.system(cmd)