# CovidDetectionFromChest-XRay

A CNN-based architecture to classify XRay images into COVID-19 positive or negative. Training accuracy- 92%. Test accuracy- 96%.
#### Dataset:
COVID positive images: https://github.com/ieee8023/covid-chestxray-dataset

Normal Xray images: https://www.kaggle.com/paultimothymooney/chest-xray-pneumonia

Preprocessing has been done to select only the XRay images with a front view of the chest. The code for preprocessing can be found in preprocessing.py. Image data augmentation has been carried out using ImageDataGenerator from keras, since available data is very less.
