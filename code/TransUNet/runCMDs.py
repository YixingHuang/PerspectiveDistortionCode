import os
os.environ["CUDA_VISIBLE_DEVICES"]="0"
cmd = 'py train.py --vit_name ViT-L_16 --n_skip 0  --dataset beadphantom512 --img_size 512 --batch_size 5'

cmd2 = 'py test.py --vit_name ViT-L_16 --n_skip 0  --dataset beadphantom512 --img_size 512 --batch_size 6 --is_savenii '

cmd3 = 'py train.py --vit_name R50-ViT-B_16 --n_skip 3  --dataset beadphantom512 --img_size 512 --batch_size 8'

cmd4 = 'py test.py --vit_name R50-ViT-B_16 --n_skip 3  --dataset beadphantom512 --img_size 512 --batch_size 8 --is_savenii'

cmd5 = 'py train.py --vit_name ViT-B_16 --n_skip 0  --dataset beadphantom512 --img_size 512 --batch_size 8'

cmd6 = 'py test.py --vit_name ViT-B_16 --n_skip 0  --dataset beadphantom512 --img_size 512 --batch_size 8 --is_savenii'

cmd7 = 'py train.py --vit_name R50-ViT-B_16 --n_skip 3   --dataset beadphantom512_ortho --img_size 512 --batch_size 8'

cmd8 = 'py test.py --vit_name R50-ViT-B_16 --n_skip 3   --dataset beadphantom512_ortho --img_size 512 --batch_size 8 --is_savenii'

cmd9 = 'py train.py --vit_name R50-ViT-B_16 --n_skip 3   --dataset 0TrainingPolar --img_size 512 --batch_size 8'

cmd10 = 'py test.py --vit_name R50-ViT-B_16 --n_skip 3   --dataset 0TrainingPolar --img_size 512 --batch_size 8 --is_savenii'


cmd11 = 'py train.py --vit_name R50-ViT-B_16 --n_skip 3   --dataset 0and180Training --img_size 512 --batch_size 8'

cmd12 = 'py test.py --vit_name R50-ViT-B_16 --n_skip 3   --dataset 0and180Training --img_size 512 --batch_size 8 --is_savenii'

cmd13 = 'py train.py --vit_name R50-ViT-B_16 --n_skip 3   --dataset 0and90BPOPTraining --img_size 512 --batch_size 8'

cmd14 = 'py test.py --vit_name R50-ViT-B_16 --n_skip 3   --dataset 0and90BPOPTraining --img_size 512 --batch_size 8 --is_savenii'

#in the above, only R50-ViT-B_16 is considered.

cmd15 = 'py train.py --vit_name R50-ViT-L_16 --n_skip 3  --dataset beadphantom512 --img_size 512 --batch_size 3 --n_gpu 2'

cmd16 = 'py test.py --vit_name R50-ViT-L_16 --n_skip 3  --dataset beadphantom512 --img_size 512 --batch_size 3 --is_savenii --n_gpu 2'

cmd17 = 'py train.py --vit_name R50-ViT-L_16 --n_skip 3   --dataset beadphantom512_ortho --img_size 512 --batch_size 3 --n_gpu 2'

cmd18 = 'py test.py --vit_name R50-ViT-L_16 --n_skip 3   --dataset beadphantom512_ortho --img_size 512 --batch_size 3 --is_savenii --n_gpu 2'

#With perceptual loss
cmd20 = 'py train.py --vit_name R50-ViT-B_16 --n_skip 3   --dataset 0and180Training --img_size 512 --batch_size 13'
cmd21 = 'py test.py --vit_name R50-ViT-B_16 --n_skip 3   --dataset 0and180Training --img_size 512 --batch_size 13 --is_savenii'

cmd22 = 'py train.py --vit_name R50-ViT-B_16 --n_skip 3   --dataset beadphantom512 --img_size 512 --batch_size 12'
cmd23 = 'py test.py --vit_name R50-ViT-B_16 --n_skip 3   --dataset beadphantom512 --img_size 512 --batch_size 12 --is_savenii'

cmd24 = 'py train.py --vit_name R50-ViT-B_16 --n_skip 3   --dataset 0and90Training --img_size 512 --batch_size 12'
cmd25 = 'py test.py --vit_name R50-ViT-B_16 --n_skip 3   --dataset 0and90Training --img_size 512 --batch_size 12 --is_savenii'

cmd26 = 'py train.py --vit_name R50-ViT-B_16 --n_skip 3   --dataset 0and90and180Training --img_size 512 --batch_size 10'
cmd27 = 'py test.py --vit_name R50-ViT-B_16 --n_skip 3   --dataset 0and90and180Training --img_size 512 --batch_size 10 --is_savenii'


# With Perceptual loss, 0 and 5 degrees, 2024. Feb. 6th
cmd30 = 'py train.py --vit_name R50-ViT-B_16 --n_skip 3   --dataset 0and5Training --img_size 512 --batch_size 13'
cmd31 = 'py test.py --vit_name R50-ViT-B_16 --n_skip 3   --dataset 0and5Training --img_size 512 --batch_size 13 --is_savenii'

cmd32 = 'py train.py --vit_name R50-ViT-B_16 --n_skip 3   --dataset 0and10Training --img_size 512 --batch_size 12'
cmd33 = 'py test.py --vit_name R50-ViT-B_16 --n_skip 3   --dataset 0and10Training --img_size 512 --batch_size 12 --is_savenii'

cmd34 = 'py train.py --vit_name R50-ViT-B_16 --n_skip 3   --dataset 0and15Training --img_size 512 --batch_size 12'
cmd35 = 'py test.py --vit_name R50-ViT-B_16 --n_skip 3   --dataset 0and15Training --img_size 512 --batch_size 12 --is_savenii'

cmd36 = 'py train.py --vit_name R50-ViT-B_16 --n_skip 3   --dataset 0and5PolarTraining --img_size 512 --batch_size 13'
cmd37 = 'py test.py --vit_name R50-ViT-B_16 --n_skip 3   --dataset 0and5PolarTraining --img_size 512 --batch_size 13 --is_savenii'

cmd38 = 'py train.py --vit_name R50-ViT-B_16 --n_skip 3   --dataset 0and10PolarTraining --img_size 512 --batch_size 12'
cmd39 = 'py test.py --vit_name R50-ViT-B_16 --n_skip 3   --dataset 0and10PolarTraining --img_size 512 --batch_size 12 --is_savenii'

cmd40 = 'py train.py --vit_name R50-ViT-B_16 --n_skip 3   --dataset 0and15PolarTraining --img_size 512 --batch_size 12'
cmd41 = 'py test.py --vit_name R50-ViT-B_16 --n_skip 3   --dataset 0and15PolarTraining --img_size 512 --batch_size 12 --is_savenii'

# cmds = [cmd20, cmd21]
cmd50 = 'py train.py --vit_name R50-ViT-B_16 --n_skip 3   --dataset Cephalo0and5 --img_size 512 --batch_size 12 --list_dir ./lists/lists_cephalo --max_epochs 150'
cmd51 = 'py test.py --vit_name R50-ViT-B_16 --n_skip 3   --dataset Cephalo0and5 --img_size 512 --batch_size 12 --is_savenii  --list_dir ./lists/lists_cephalo --max_epochs 150'

cmd52 = 'py train.py --vit_name R50-ViT-B_16 --n_skip 3   --dataset Cephalo0and90RGB --img_size 512 --batch_size 12 --list_dir ./lists/lists_cephalo --max_epochs 150'
cmd53 = 'py test.py --vit_name R50-ViT-B_16 --n_skip 3   --dataset Cephalo0and90RGB --img_size 512 --batch_size 12 --is_savenii  --list_dir ./lists/lists_cephalo --max_epochs 150'

cmd54 = 'py train.py --vit_name R50-ViT-B_16 --n_skip 3   --dataset Cephalo0Deg --img_size 512 --batch_size 12 --list_dir ./lists/lists_cephalo --max_epochs 150'
cmd55 = 'py test.py --vit_name R50-ViT-B_16 --n_skip 3   --dataset Cephalo0Deg --img_size 512 --batch_size 12 --is_savenii  --list_dir ./lists/lists_cephalo --max_epochs 150'

cmd56 = 'py train.py --vit_name R50-ViT-B_16 --n_skip 3   --dataset Cephalo0and180 --img_size 512 --batch_size 12 --list_dir ./lists/lists_cephalo --max_epochs 150'
cmd57 = 'py test.py --vit_name R50-ViT-B_16 --n_skip 3   --dataset Cephalo0and180 --img_size 512 --batch_size 12 --is_savenii  --list_dir ./lists/lists_cephalo --max_epochs 150'

cmds = [cmd50, cmd51, cmd52, cmd53, cmd54, cmd55, cmd56, cmd57]

for cmd in cmds:
    os.system(cmd)