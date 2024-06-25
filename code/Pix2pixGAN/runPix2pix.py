import os
os.environ["CUDA_VISIBLE_DEVICES"]="0"
# os.system('py -m visdom.server')
# training
# os.system('py train.py --dataroot ./datasets/facades --name facades_pix2pix --model pix2pix --direction AtoB --display_id 0')

#test
# os.system('py test.py --dataroot ./datasets/facades --name facades_pix2pix --model pix2pix --direction AtoB')

# cmd1 = 'py train.py --dataroot ./datasets/leg256 --name leg_cycleganC1UNetSTD --model cycle_gan --display_id 0 --preprocess none --num_threads 0 --gpu_ids 0,1 --batch_size 20 --input_nc 1 --output_nc 1 --n_epochs_decay 200 --netG unet_standard --netD pixel'
#
# #!./scripts/test_cyclegan.sh
# cmd2 = 'python test.py --dataroot ./datasets/leg256 --name leg_cycleganC1UNetSTD  --model cycle_gan --preprocess none --direction AtoB --input_nc 1 --output_nc 1 --netG unet_standard'
#
# cmds = [cmd1, cmd2]
#
# for cmd in cmds:
#     os.system(cmd)


# #generator ResNet9
# cmd1 = 'py train.py --dataroot ./datasets/leg256 --name leg_cycleganDBData  --model cycle_gan --display_id 0 --direction AtoB --num_threads 0 --gpu_ids 0,1 --batch_size 35 --input_nc 1 --output_nc 1 --n_epochs_decay 100 --netG resnet_9blocks'
#
# #!./scripts/test_cyclegan.sh
# cmd2 = 'python test.py --dataroot ./datasets/leg256 --name leg_cycleganDBData  --model cycle_gan --direction AtoB --input_nc 1 --output_nc 1 --netG resnet_9blocks '
#
# cmds = [cmd1, cmd2]
#
# for cmd in cmds:
#     os.system(cmd)



# cmd1 = 'python train.py --dataroot ./datasets/shoulder --name shoulderFOV2 --model pix2pix --dataset_mode aligned --display_id 0 --preprocess none --num_threads 0 --gpu_ids 0 --batch_size 10 --input_nc 1 --output_nc 1 --n_epochs 5 --n_epochs_decay 5 --netG unet_standard --isTiff --norm batch --pool_size 0'
cmd1 = 'python train.py --dataroot ./datasets/shoulder --name shoulderFOV2 --model pix2pix --dataset_mode aligned --display_id 0 --preprocess none --num_threads 0 --gpu_ids 0 --batch_size 10 --input_nc 1 --output_nc 1 --n_epochs 100 --n_epochs_decay 50 --netG unet_256 --isTiff --norm batch --pool_size 0'

#!./scripts/test_cyclegan.sh
cmd2 = 'python test.py --dataroot ./datasets/shoulder --name shoulderFOV2  --model pix2pix --dataset_mode aligned --preprocess none --direction AtoB --input_nc 1 --output_nc 1 --netG unet_256  --isTiff --norm batch'


cmd3 =  'python train.py --dataroot ./datasets/shoulder --name shoulderFOV_standUNet --model pix2pix --dataset_mode aligned --display_id 0 --preprocess none --num_threads 0 --gpu_ids 0 --batch_size 10 --input_nc 1 --output_nc 1 --n_epochs 100 --n_epochs_decay 50 --netG unet_standard --isTiff --norm batch --pool_size 0'

cmd4 = 'python test.py --dataroot ./datasets/shoulder --name shoulderFOV_standUNet --model pix2pix --dataset_mode aligned --preprocess none --direction AtoB --input_nc 1 --output_nc 1 --netG unet_standard  --isTiff --norm batch'

cmd5 = 'python test.py --dataroot ./datasets/shoulder --name shoulderFOV2  --model pix2pix --dataset_mode aligned --preprocess none --direction AtoB --input_nc 1 --output_nc 1 --netG unet_256  --isTiff --norm batch --num_test 10752'

cmd6 = 'python trainAndVal.py --dataroot ./datasets/THz --name THzEnhancement4 --model pix2pix --dataset_mode aligned --display_id 0 --preprocess none --direction AtoB --num_threads 0 --gpu_ids 0 --batch_size 50 --input_nc 1 --output_nc 1 --n_epochs 50 --n_epochs_decay 150 --netG unet_256  --norm batch --pool_size 0'

cmd7 = 'python test.py --dataroot ./datasets/THz --name THzEnhancement4  --model pix2pix --dataset_mode aligned --preprocess none --direction AtoB --input_nc 1 --output_nc 1 --netG unet_256  --norm batch --num_test 34'

cmd12 = 'python test.py --dataroot ./datasets/THz --name THzEnhancement2  --model pix2pix --dataset_mode aligned --preprocess none --direction AtoB --input_nc 3 --output_nc 3 --netG unet_256  --norm batch --num_test 34'
cmd13 = 'python test.py --dataroot ./datasets/THz --name THzEnhancement3  --model pix2pix --dataset_mode aligned --preprocess none --direction AtoB --input_nc 3 --output_nc 3 --netG unet_256  --norm batch --num_test 34'
cmd14 = 'python test.py --dataroot ./datasets/THz --name THzEnhancement4  --model pix2pix --dataset_mode aligned --preprocess none --direction AtoB --input_nc 3 --output_nc 3 --netG unet_256  --norm batch --num_test 34'

cmd15 = 'python trainAndVal.py --dataroot ./datasets/THz --name THzEnhancementResNet --model pix2pix --dataset_mode aligned --display_id 0 --preprocess none --direction AtoB --num_threads 0 --gpu_ids 0 --batch_size 50 --input_nc 1 --output_nc 1 --n_epochs 50 --n_epochs_decay 150  --norm batch --pool_size 0'

cmd16 = 'python test.py --dataroot ./datasets/THz --name THzEnhancementResNet  --model pix2pix --dataset_mode aligned --preprocess none --direction AtoB --input_nc 1 --output_nc 1  --norm batch --num_test 34'

cmd17 = 'python trainAndVal.py --dataroot ./datasets/THz --name THzEnhancementResNet3 --model pix2pix --dataset_mode aligned  --display_id 0 --direction AtoB --num_threads 0 --gpu_ids 0 --batch_size 2 --input_nc 1 --output_nc 1'

cmd18 = 'python test.py --dataroot ./datasets/THz --name THzEnhancementResNet3  --model pix2pix --dataset_mode aligned --direction AtoB --input_nc 1 --output_nc 1  --norm batch --num_test 34'


cmd20 = 'py train.py --dataroot ./datasets/0and5Training --name Bead0and5Deg --model pix2pix --dataset_mode aligned --display_id 0 --preprocess none --num_threads 0 --gpu_ids 0 --batch_size 10 --input_nc 3 --output_nc 3 --n_epochs 100 --n_epochs_decay 50 --netG unet_256 --norm batch --pool_size 0 --no_flip'

cmd21 = 'py test.py --dataroot ./datasets/0and5Training --name Bead0and5Deg --model pix2pix --dataset_mode aligned --preprocess none --direction AtoB --input_nc 3 --output_nc 3 --netG unet_256   --norm batch --no_flip --num_test 60'

cmd22 = 'py train.py --dataroot ./datasets/0and5PolarTraining --name Bead0and5DegPolar --model pix2pix --dataset_mode aligned --display_id 0 --preprocess none --num_threads 0 --gpu_ids 0 --batch_size 10 --input_nc 3 --output_nc 3 --n_epochs 100 --n_epochs_decay 50 --netG unet_256 --norm batch --pool_size 0 --no_flip'

cmd23 = 'py test.py --dataroot ./datasets/0and5PolarTraining --name Bead0and5DegPolar --model pix2pix --dataset_mode aligned --preprocess none --direction AtoB --input_nc 3 --output_nc 3 --netG unet_256   --norm batch --no_flip --num_test 60'


# cmd24 = 'py train.py --dataroot ./datasets/0and180PolarTraining --name Bead0and180DegPolar --model pix2pix --dataset_mode aligned --display_id 0 --preprocess none --num_threads 0 --gpu_ids 0 --batch_size 10 --input_nc 3 --output_nc 3 --n_epochs 100 --n_epochs_decay 50 --netG unet_standard --norm batch --pool_size 0 --direction AtoB --no_flip'
#
# cmd25 = 'py test.py --dataroot ./datasets/0and180PolarTraining --name Bead0and180DegPolar --model pix2pix --dataset_mode aligned --preprocess none --direction AtoB --input_nc 3 --output_nc 3 --netG unet_standard   --norm batch --no_flip'

cmd26 = 'py train.py --dataroot ./datasets/0and180PolarTraining --name Bead0and180DegPolarUNet256 --model pix2pix --dataset_mode aligned --display_id 0 --preprocess none --num_threads 0 --gpu_ids 0 --batch_size 10 --input_nc 3 --output_nc 3 --n_epochs 100 --n_epochs_decay 50 --netG unet_256 --norm batch --pool_size 0 --direction AtoB --no_flip'

cmd27 = 'py test.py --dataroot ./datasets/0and180PolarTraining --name Bead0and180DegPolarUNet256 --model pix2pix --dataset_mode aligned --preprocess none --direction AtoB --input_nc 3 --output_nc 3 --netG unet_256   --norm batch --no_flip --num_test 60'

cmd28 = 'py train.py --dataroot ./datasets/0and180Training --name Bead0and180DegUNet256 --model pix2pix --dataset_mode aligned --display_id 0 --preprocess none --num_threads 0 --gpu_ids 0 --batch_size 10 --input_nc 3 --output_nc 3 --n_epochs 100 --n_epochs_decay 50 --netG unet_256 --norm batch --pool_size 0 --direction AtoB --no_flip'

cmd29 = 'py test.py --dataroot ./datasets/0and180Training --name Bead0and180DegUNet256 --model pix2pix --dataset_mode aligned --preprocess none --direction AtoB --input_nc 3 --output_nc 3 --netG unet_256   --norm batch --no_flip --num_test 60'

cmd30 = 'py train.py --dataroot ./datasets/0and180RGBCephalo --name Cephalo0and180DegUNet256 --model pix2pix --dataset_mode aligned --display_id 0 --preprocess none --num_threads 0 --gpu_ids 0 --batch_size 10 --input_nc 3 --output_nc 3 --n_epochs 100 --n_epochs_decay 50 --netG unet_256 --norm batch --pool_size 0 --direction AtoB --no_flip'

cmd31 = 'py test.py --dataroot ./datasets/0and180RGBCephalo --name Cephalo0and180DegUNet256 --model pix2pix --dataset_mode aligned --preprocess none --direction AtoB --input_nc 3 --output_nc 3 --netG unet_256   --norm batch --no_flip --num_test 90'

cmd32 = 'py train.py --dataroot ./datasets/0and90RGBCephalo --name Cephalo0and90DegUNet256 --model pix2pix --dataset_mode aligned --display_id 0 --preprocess none --num_threads 0 --gpu_ids 0 --batch_size 10 --input_nc 3 --output_nc 3 --n_epochs 100 --n_epochs_decay 50 --netG unet_256 --norm batch --pool_size 0 --direction AtoB --no_flip'

cmd33 = 'py test.py --dataroot ./datasets/0and90RGBCephalo --name Cephalo0and90DegUNet256 --model pix2pix --dataset_mode aligned --preprocess none --direction AtoB --input_nc 3 --output_nc 3 --netG unet_256   --norm batch --no_flip --num_test 90'

cmd34 = 'py train.py --dataroot ./datasets/0and5RGBCephalo --name Cephalo0and5DegUNet256 --model pix2pix --dataset_mode aligned --display_id 0 --preprocess none --num_threads 0 --gpu_ids 0 --batch_size 10 --input_nc 3 --output_nc 3 --n_epochs 100 --n_epochs_decay 50 --netG unet_256 --norm batch --pool_size 0 --direction AtoB --no_flip'

cmd35 = 'py test.py --dataroot ./datasets/0and5RGBCephalo --name Cephalo0and5DegUNet256 --model pix2pix --dataset_mode aligned --preprocess none --direction AtoB --input_nc 3 --output_nc 3 --netG unet_256   --norm batch --no_flip --num_test 90'


cmd36 = 'py train.py --dataroot ./datasets/0and5RGBCephalo --name Cephalo0and5DegUNet256PLTry --model pix2pix --dataset_mode aligned --display_id 0 --preprocess none --num_threads 0 --gpu_ids 0 --batch_size 10 --input_nc 3 --output_nc 3 --n_epochs 100 --n_epochs_decay 50 --netG unet_256 --norm batch --pool_size 0 --direction AtoB --no_flip'

cmd37 = 'py train.py --dataroot ./datasets/0and180PolarRGBCephalo --name 0and180PolarRGBCephaloUNet256PolarPL --model pix2pix --dataset_mode aligned --display_id 0 --preprocess none --num_threads 0 --gpu_ids 0 --batch_size 10 --input_nc 3 --output_nc 3 --n_epochs 100 --n_epochs_decay 50 --netG unet_256_periodic --norm batch --pool_size 0 --direction AtoB --no_flip'

cmd38 = 'py test.py --dataroot ./datasets/0and180PolarRGBCephalo --name 0and180PolarRGBCephaloUNet256PolarPL --model pix2pix --dataset_mode aligned --preprocess none --direction AtoB --input_nc 3 --output_nc 3 --netG unet_256_periodic   --norm batch --no_flip --num_test 90'

cmd39 = 'py train.py --dataroot ./datasets/0and90PolarRGBCephalo --name 0and90PolarRGBCephaloUNet256PolarPL --model pix2pix --dataset_mode aligned --display_id 0 --preprocess none --num_threads 0 --gpu_ids 0 --batch_size 10 --input_nc 3 --output_nc 3 --n_epochs 100 --n_epochs_decay 50 --netG unet_256_periodic --norm batch --pool_size 0 --direction AtoB --no_flip'

cmd40 = 'py test.py --dataroot ./datasets/0and90PolarRGBCephalo --name 0and90PolarRGBCephaloUNet256PolarPL --model pix2pix --dataset_mode aligned --preprocess none --direction AtoB --input_nc 3 --output_nc 3 --netG unet_256_periodic   --norm batch --no_flip --num_test 90'

cmd41 = 'py train.py --dataroot ./datasets/0and5PolarRGBCephalo --name 0and5PolarRGBCephaloUNet256PolarPL --model pix2pix --dataset_mode aligned --display_id 0 --preprocess none --num_threads 0 --gpu_ids 0 --batch_size 10 --input_nc 3 --output_nc 3 --n_epochs 100 --n_epochs_decay 50 --netG unet_256_periodic --norm batch --pool_size 0 --direction AtoB --no_flip'

cmd42 = 'py test.py --dataroot ./datasets/0and5PolarRGBCephalo --name 0and5PolarRGBCephaloUNet256PolarPL --model pix2pix --dataset_mode aligned --preprocess none --direction AtoB --input_nc 3 --output_nc 3 --netG unet_256_periodic   --norm batch --no_flip --num_test 90'

cmd43 = 'py train.py --dataroot ./datasets/0DegPolarRGBCephalo --name 0DegPolarRGBCephaloUNet256PolarPL --model pix2pix --dataset_mode aligned --display_id 0 --preprocess none --num_threads 0 --gpu_ids 0 --batch_size 10 --input_nc 3 --output_nc 3 --n_epochs 100 --n_epochs_decay 50 --netG unet_256_periodic --norm batch --pool_size 0 --direction AtoB --no_flip'

cmd44 = 'py test.py --dataroot ./datasets/0DegPolarRGBCephalo --name 0DegPolarRGBCephaloUNet256PolarPL --model pix2pix --dataset_mode aligned --preprocess none --direction AtoB --input_nc 3 --output_nc 3 --netG unet_256_periodic   --norm batch --no_flip --num_test 90'

cmd45 = 'py train.py --dataroot ./datasets/0DegRGBCephalo --name 0DegCephaloDegUNet256 --model pix2pix --dataset_mode aligned --display_id 0 --preprocess none --num_threads 0 --gpu_ids 0 --batch_size 10 --input_nc 3 --output_nc 3 --n_epochs 100 --n_epochs_decay 50 --netG unet_256 --norm batch --pool_size 0 --direction AtoB --no_flip'

cmd46 = 'py test.py --dataroot ./datasets/0DegRGBCephalo --name 0DegCephaloDegUNet256 --model pix2pix --dataset_mode aligned --preprocess none --direction AtoB --input_nc 3 --output_nc 3 --netG unet_256   --norm batch --no_flip --num_test 90'

cmd47 = 'py train.py --dataroot ./datasets/Cephalo0and180PolarRGBCrop --name Cephalo0and180PolarRGBCropUNet256PolarPL --model pix2pix --dataset_mode aligned --display_id 0 --preprocess none --num_threads 0 --gpu_ids 0 --batch_size 10 --input_nc 3 --output_nc 3 --n_epochs 100 --n_epochs_decay 50 --netG unet_256_periodic --norm batch --pool_size 0 --direction AtoB --no_flip'

cmd48 = 'py test.py --dataroot ./datasets/Cephalo0and180PolarRGBCrop --name Cephalo0and180PolarRGBCropUNet256PolarPL --model pix2pix --dataset_mode aligned --preprocess none --direction AtoB --input_nc 3 --output_nc 3 --netG unet_256_periodic   --norm batch --no_flip --num_test 90'


cmd49 = 'py train.py --dataroot ./datasets/cephaloPolarTraining --name Cephalo0and180PolarCheckUNet256PolarPL --model pix2pix --dataset_mode aligned --display_id 0 --preprocess none --num_threads 0 --gpu_ids 0 --batch_size 10 --input_nc 3 --output_nc 3 --n_epochs 100 --n_epochs_decay 50 --netG unet_256_periodic --norm batch --pool_size 0 --direction AtoB --no_flip'
cmd50 = 'py test.py --dataroot ./datasets/cephaloPolarTraining --name Cephalo0and180PolarCheckUNet256PolarPL --model pix2pix --dataset_mode aligned --preprocess none --direction AtoB --input_nc 3 --output_nc 3 --netG unet_256_periodic   --norm batch --no_flip --num_test 90'

#0 and 90
cmd51 = 'py train.py --dataroot ./datasets/Cephalo0and90PolarRGB --name Cephalo0and90PolarUNet256PolarPL --model pix2pix --dataset_mode aligned --display_id 0 --preprocess none --num_threads 0 --gpu_ids 0 --batch_size 10 --input_nc 3 --output_nc 3 --n_epochs 100 --n_epochs_decay 50 --netG unet_256_periodic --norm batch --pool_size 0 --direction AtoB --no_flip'
cmd52 = 'py test.py --dataroot ./datasets/Cephalo0and90PolarRGB --name Cephalo0and90PolarUNet256PolarPL --model pix2pix --dataset_mode aligned --preprocess none --direction AtoB --input_nc 3 --output_nc 3 --netG unet_256_periodic   --norm batch --no_flip --num_test 90'

cmd53 = 'py train.py --dataroot ./datasets/Cephalo0and90RGB --name Cephalo0and90UNet256PL --model pix2pix --dataset_mode aligned --display_id 0 --preprocess none --num_threads 0 --gpu_ids 0 --batch_size 10 --input_nc 3 --output_nc 3 --n_epochs 100 --n_epochs_decay 50 --netG unet_256 --norm batch --pool_size 0 --direction AtoB --no_flip'
cmd54 = 'py test.py --dataroot ./datasets/Cephalo0and90RGB --name Cephalo0and90UNet256PL --model pix2pix --dataset_mode aligned --preprocess none --direction AtoB --input_nc 3 --output_nc 3 --netG unet_256   --norm batch --no_flip --num_test 90'

#0 and 5
cmd55 = 'py train.py --dataroot ./datasets/Cephalo0and5Polar --name Cephalo0and5PolarUNet256PolarPL --model pix2pix --dataset_mode aligned --display_id 0 --preprocess none --num_threads 0 --gpu_ids 0 --batch_size 10 --input_nc 3 --output_nc 3 --n_epochs 100 --n_epochs_decay 50 --netG unet_256_periodic --norm batch --pool_size 0 --direction AtoB --no_flip'
cmd56 = 'py test.py --dataroot ./datasets/Cephalo0and5Polar --name Cephalo0and5PolarUNet256PolarPL --model pix2pix --dataset_mode aligned --preprocess none --direction AtoB --input_nc 3 --output_nc 3 --netG unet_256_periodic   --norm batch --no_flip --num_test 90'

cmd57= 'py train.py --dataroot ./datasets/Cephalo0and5 --name Cephalo0and5UNet256PL --model pix2pix --dataset_mode aligned --display_id 0 --preprocess none --num_threads 0 --gpu_ids 0 --batch_size 10 --input_nc 3 --output_nc 3 --n_epochs 100 --n_epochs_decay 50 --netG unet_256 --norm batch --pool_size 0 --direction AtoB --no_flip'
cmd58 = 'py test.py --dataroot ./datasets/Cephalo0and5 --name Cephalo0and5UNet256PL --model pix2pix --dataset_mode aligned --preprocess none --direction AtoB --input_nc 3 --output_nc 3 --netG unet_256   --norm batch --no_flip --num_test 90'

#0 and 180
cmd59 = 'py train.py --dataroot ./datasets/Cephalo0and180Polar --name Cephalo0and180PolarUNet256PolarPL --model pix2pix --dataset_mode aligned --display_id 0 --preprocess none --num_threads 0 --gpu_ids 0 --batch_size 10 --input_nc 3 --output_nc 3 --n_epochs 100 --n_epochs_decay 50 --netG unet_256_periodic --norm batch --pool_size 0 --direction AtoB --no_flip'
cmd60 = 'py test.py --dataroot ./datasets/Cephalo0and180Polar --name Cephalo0and180PolarUNet256PolarPL --model pix2pix --dataset_mode aligned --preprocess none --direction AtoB --input_nc 3 --output_nc 3 --netG unet_256_periodic   --norm batch --no_flip --num_test 90'

cmd61 = 'py train.py --dataroot ./datasets/Cephalo0and180 --name Cephalo0and180UNet256PL --model pix2pix --dataset_mode aligned --display_id 0 --preprocess none --num_threads 0 --gpu_ids 0 --batch_size 10 --input_nc 3 --output_nc 3 --n_epochs 100 --n_epochs_decay 50 --netG unet_256 --norm batch --pool_size 0 --direction AtoB --no_flip'
cmd62 = 'py test.py --dataroot ./datasets/Cephalo0and180 --name Cephalo0and180UNet256PL --model pix2pix --dataset_mode aligned --preprocess none --direction AtoB --input_nc 3 --output_nc 3 --netG unet_256   --norm batch --no_flip --num_test 90'

#0 only
cmd63 = 'py train.py --dataroot ./datasets/Cephalo0DegPolar --name Cephalo0DegPolarUNet256PolarPL --model pix2pix --dataset_mode aligned --display_id 0 --preprocess none --num_threads 0 --gpu_ids 0 --batch_size 10 --input_nc 3 --output_nc 3 --n_epochs 100 --n_epochs_decay 50 --netG unet_256_periodic --norm batch --pool_size 0 --direction AtoB --no_flip'
cmd64 = 'py test.py --dataroot ./datasets/Cephalo0DegPolar --name Cephalo0DegPolarUNet256PolarPL --model pix2pix --dataset_mode aligned --preprocess none --direction AtoB --input_nc 3 --output_nc 3 --netG unet_256_periodic   --norm batch --no_flip --num_test 90'

cmd65 = 'py train.py --dataroot ./datasets/Cephalo0Deg --name Cephalo0DegUNet256PL --model pix2pix --dataset_mode aligned --display_id 0 --preprocess none --num_threads 0 --gpu_ids 0 --batch_size 10 --input_nc 3 --output_nc 3 --n_epochs 100 --n_epochs_decay 50 --netG unet_256 --norm batch --pool_size 0 --direction AtoB --no_flip'
cmd66 = 'py test.py --dataroot ./datasets/Cephalo0Deg --name Cephalo0DegUNet256PL --model pix2pix --dataset_mode aligned --preprocess none --direction AtoB --input_nc 3 --output_nc 3 --netG unet_256   --norm batch --no_flip --num_test 90'

# cmds = [cmd53, cmd54, cmd55, cmd56, cmd57, cmd58, cmd59, cmd60, cmd61, cmd62, cmd63, cmd64, cmd65, cmd66]
# cmds = [cmd54, cmd58, cmd62, cmd66]
cmds = [cmd58]
for cmd in cmds:
    os.system(cmd)



