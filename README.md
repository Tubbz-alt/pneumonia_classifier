**Pneumonia Classifier** 

Deployed using render: <https://pneumonia-classifier.onrender.com> 

**--Model tuning still in progess** 

Pneumonia is a infection that causes inflammation in the lungs. X-rays are currently the best method in identifying pneumonia, however X-rays have there limitations because they dont show which kind of bacteria is attacking the lungs and also generally the data we have is only the frontal view. Advances in deep learning has paved the way for AI to perform better than humans at many different tasks in healthcare. A research paper "CheXNet: Radiologist-Level Pneumonia Detection on Chest X-Rays
with Deep Learning" <https://arxiv.org/pdf/1711.05225v3.pdf> ran a study where they evaluated performance of classification for pneuomonia and other infections while comparing their model scores with experienced radiologists. Using a pretrained model (Imagenet) They were able to outperform radiologists using a 121 layer CNN which is a type of neural network most commonly used for visual images and video. 


**Dataset**

This data set is different than the one used in the CheXNet paper. Our data came from Kaggle, but thanks to the work of Radiological Society of North America (RSNA®) & US National Institutes of Health, The Society of Thoracic Radiology. Which contained a total of 6503 images. 

**Training Set**: 
4707 images

**Validation Set**
1175 images

**Test Set**
624 images


First our model was trained on Resnet which is a residual network.
(more info about residual networks here <https://arxiv.org/pdf/1512.03385.pdf>)







![alt text](https://ujwlkarn.files.wordpress.com/2016/08/screen-shot-2016-08-07-at-4-59-29-pm.png?w=1493)
