# PerspectiveDeformationCode
 Code and data for **Learning Perspective Deformation Correction in Cone-Beam X-Ray Transmission Imaging**


 # Additional information for Experimental Setup

 ## Numerical bead phantoms
3D bead phantoms are generated to demonstrate the efficacy of our proposed algorithms for general perspective deformation learning. Each bead phantom is a cylinder containing spherical beads. The height and diameter of the cylinder are randomly generated, with values of $240 \pm 16$ mm and $225 \pm 32$ mm respectively. The background intensity value of the cylinder is a random value of $50\pm 35$ HU.  Small and big beads have the sizes of $6.4 \pm 1.6$ mm and $16 \pm 8$ mm, respectively. Their intensities are either $3500 \pm 350$ HU or $6000 \pm 1000$ HU. The phantoms have a size of $512 \times 512 \times 512$ voxels with a voxel size of $0.625 \times 0.625 \times 0.625 \text{mm}^3$. 200 bead phantoms are generated, with 185 phantoms for training, 5 phantoms for validation, and 10 phantoms for testing. Each phantom in the dataset contains approximately 50 spherical beads with random positions inside the cylinder. Note that the number of beads also varies randomly in the same data set. 
%In BeadData III, due to the large number of beads, the bead-to-bead correspondence between different views is very difficult to determine. Therefore, learning perspective deformation is the most challenging for BeadData III among the three data sets.

For data augmentation, each phantom is rotated by $15^\circ$, $30^\circ$, $\dots$, $75^\circ$. This is equivalent to acquire projection data from the view angles of $15^\circ$, $30^\circ$, $\dots$, $75^\circ$. Hence, for each original phantom, six orthogonal projection images with their corresponding $0^\circ$, $90^\circ$, and $180^\circ$ perspective projections images are acquired. This augmentation is applied to the training, validation, and test phantoms.

The projection images in Cartesian coordinates have an image size of $512 \times 512$ with a pixel size of $0.625 \text{mm} \times 0.625 \text{mm}$. Images in polar coordinates have an image size of $512 \times 512$ with a pixel size of $0.375 \text{mm} \times 0.703^\circ$. Images in log-polar coordinates have an image size of $512 \times 512$ with an angular spacing of $0.703^\circ$ and an initial radial spacing of 0.0075 mm. For display, the integral intensity range of [0, 6] in projection images is linearly converted to [0, 255] (the same for the following chest and head data).

For simulation studies on bead phantom data, a cone beam computed tomography (CBCT) system with a source-to-detector distance ($D_{\text{sd}}$) of 1200 mm and a source-to-isocenter distance ($D_{\text{si}}$) of 750 mm is used, which represents a common configuration for floor mounted C-arm CBCT systems. The detector has $1240 \times 960$ pixels with a pixel size of $0.308 \times 0.308 \text{mm}^2$. Acquired projection images are rebinned to a virtual detector at the isocenter, which has $512 \times 512$ pixels with a pixel size of $0.625 \times 0.625 \text{mm}^2$. In practice, higher pixel resolution for the virtual detector is achievable. Here a coarse resolution of $0.625 \times 0.625 \text{mm}^2$ is used as a proof of concept. The volume centers of imaged objects are located at the world coordinate origin. Perspective projections are generated via forward projection of the volumes. The orthogonal projections are generated using a large virtual source-to-detector distance of 12000 mm and a short isocenter-to-detector distance of 100 mm.

## Head CT data
 In dental imaging, orthogonal X-ray projections are preferred over perspective projections for cephalometric analysis. Hence, the proposed perspective deformation learning algorithms are also evaluated on head CT data. The CQ500 dataset \cite{chilamkurthy2018deep} as well as a public domain database for computational anatomy (PDDCA) [\cite{raudaschl2017evaluation}](https://www.thelancet.com/journals/lancet/article/PIIS0140-6736(18)31645-3/abstract) and 10 complete human mandible data sets [\cite{wallner2019computed}](https://www.nature.com/articles/sdata20193) are used for this purpose. The CQ500 dataset consists of 491 scans, and the PDDCA consists of 48 complete patient head and neck CT images. Many volumes in the CQ500 dataset miss the lower head (neck) part. That is why the other two datasets are necessary for training. The training volumes are augmented by random anisotropic scalings. The volumes whose slice spacing is larger than 2.5 mm or the total slice number is smaller than 100 are removed. In total, 960 volumes are used for training, 10 volumes for validation, and 30 volumes for testing.
 
For simulation studies on the head CT data, the CBCT system has a source-to-detector distance of 960 mm and a source-to-isocenter distance of 600 mm, since dental CBCT systems typically have a shorter source-to-detector distance than that of angiographic C-arm CBCT systems. The projection images in Cartesian coordinates have an image size of $512 \times 512$ with a pixel size of $0.5 \text{mm} \times 0.5 \text{mm}$. Images in polar coordinates have an image size of $512 \times 512$ with a pixel size of $0.5 \text{mm} \times 0.703^\circ$. 

## Real data
In total, 20 real cadaver knee datasets are acquired from a mobile C-arm CBCT system, containing 10 knees without metal implants and 10 knees with metal implants. The CBCT scan trajectory is defined by projection matrices. It has a source-to-detector distance ($D_{\text{sd}}$) of approximately 1160 mm and a source-to-isocenter distance ($D_{\text{si}}$) of around 621 mm. Note that due to mechanical instability, these two distances vary slightly from view to view. The detector has $976 \times 976$ pixels with a pixel size of $0.304 \times 0.304 \text{mm}^2$. Acquired projection images are rebinned to a virtual detector at the isocenter, which has $512 \times 512$ pixels with a pixel size of $0.295 \times 0.295 \text{mm}^2$. 400 2D projection images for each scan are acquired with an equiangular increment of $0.4875^\circ$. The total angular range is $195^\circ$.   For each scan, 31 projections ($0^\circ$ to $15^\circ$) have their corresponding complementary view projections ($180^\circ$ to $195^\circ$). One exemplary projection and its complementary view is displayed in Fig. \ref{Fig:RealDataGeometricCalibration}. 

For real CBCT systems, the principal point of each view is not located perfectly at the detector center. Hence, a simple horizontal flip of the complementary view will cause anatomy misalignment.  For example, in Fig. [12c](https://github.com/YixingHuang/PerspectiveDeformationCode/blob/main/Figure12.png) the difference between two complementary views is large at the central region, which violates the perspective deformation property (low deformation at the central region). When rebinning the $0^\circ$ view to the virtual detector, its principal point can be placed at the center, as displayed in Fig. [11](https://github.com/YixingHuang/PerspectiveDeformationCode/blob/main/Figure11.png). For the $180^\circ$ complementary view, its structures need to be aligned to those in the $0^\circ$ view. In practice, the perspective projection of world origin, which is the last column of the perspective projection matrix, is located very close to the principal point. Therefore, shifting the second virtual detector based on its perspective projection of world origin will reduce such anatomy misalignment. Note that due to mechanical instability the principal point varies from view to view. Because of this, after structure alignment, the principal point of the complementary view still has slight shift from that of the $0^\circ$ view, as illustrated by the red point in Fig. [11](https://github.com/YixingHuang/PerspectiveDeformationCode/blob/main/Figure11.png). In this real dataset, the majority of principal point shifts are within 10 pixels (1.6 mm in the virtual detector) and all the views are with 20 pixels (3.2 mm), which has limited influence on network performance. For example, after such calibration, the difference magnitude increases from the center towards the outside in Fig. [12d](https://github.com/YixingHuang/PerspectiveDeformationCode/blob/main/Figure11.png) like it does in DRRs with an ideal scan trajectory. 

To train deep learning models, 50 multi-slice CT volumes from the SIACS medical image repository [\cite{kistler2013virtual}](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3841349/) are used. Each volume contains a single knee. The volumes are resampled to a volume size of $300\times 600 \times 600$ with an isotropic voxel spacing of 0.5 mm. Synthetic metal implants like K-wires, screws, and plates with holes are drawn by AutoCAD [\cite{fan2022metal}](https://ieeexplore.ieee.org/document/10230412). These implants are randomly selected and placed in the CT volumes as ground truth volumes. These volumes are forward projected to generate projections by CONRAD [\cite{maier2013conrad}](https://aapm.onlinelibrary.wiley.com/doi/10.1118/1.4824926) with an ideal circular trajectory with $D_{\text{sd}}=1160$ mm and $D_{\text{si}}=$ 621 mm using the same detector configuration as the real mobile C-arm system. In total, 1400 images are used for training, 150 images are used for validation and 620 images from the real cadaver data are used for test.

![Figure 11](https://github.com/YixingHuang/PerspectiveDeformationCode/blob/main/Figure11.png)

![Figure 12](https://github.com/YixingHuang/PerspectiveDeformationCode/blob/main/Figure12.png)

## Network Training Parameters
For training Pix2pixGAN, the Adam optimizer is used with an initial learning rate of 0.0002 and a momentum term of 0.5. The weights $\lambda_1$ and $\lambda_2$ are set to 100 and 50 for the $\ell_1$ loss and the perceptual loss, respectively. Validation is performed during training to avoid over-fitting. In total, 150 epochs are used for training. 

For TransU-Net, the pretrained model of ViT-B/16 is used. For further training, the momentum optimizer is used, with an initial learning rate of 0.01, a momentum term of 0.9 and a weight decay rate of 0.0001. The perceptual loss weight $\lambda_3$ is set to 0.5. Note that setting $\lambda_3$ to a large value of 1.0 causes TransU-Net to predict the beads only without the cylinder background in our experiments. In total, 150 epochs are used for training.

For learning in the Cartesian space, zero padding is used for convolutional operations to keep the same image size. In contrast, for learning in the polar space, periodic padding is used to reduce stitching artifacts at the $0^\circ$ ($360^\circ$) radial direction.
