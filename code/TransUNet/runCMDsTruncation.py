import os
os.environ["CUDA_VISIBLE_DEVICES"]="0"

cmd26 = 'python train.py --vit_name R50-ViT-B_16 --n_skip 3   --dataset shoulderTruncation --list_dir ./lists/lists_truncation --img_size 512 --batch_size 10 --num_classes 1'
cmd27 = 'python test.py --vit_name R50-ViT-B_16 --n_skip 3   --dataset shoulderTruncation --list_dir ./lists/lists_truncation --img_size 512 --batch_size 10 --is_savenii  --num_classes 1 --isTiff'


cmd28 = 'python train.py --vit_name R50-ViT-B_16 --n_skip 3   --dataset THzRGB --list_dir ./lists/lists_THz --img_size 256 --batch_size 40 --num_classes 3'
cmd29 = 'python test.py --vit_name R50-ViT-B_16 --n_skip 3   --dataset THzRGB --list_dir ./lists/lists_THz --img_size 256 --batch_size 40 --is_savenii  --num_classes 3'

cmd30 = 'python train.py --vit_name R50-ViT-B_16 --n_skip 3   --dataset THz --list_dir ./lists/lists_THz --img_size 256 --batch_size 10 --num_classes 1'
cmd31 = 'python test.py --vit_name R50-ViT-B_16 --n_skip 3   --dataset THz --list_dir ./lists/lists_THz --img_size 256 --batch_size 10 --is_savenii  --num_classes 1'


# cmds = [cmd20, cmd21]

# cmds = [cmd26, cmd27]
cmds = [cmd27]
for cmd in cmds:
    os.system(cmd)