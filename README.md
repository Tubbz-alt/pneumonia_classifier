**Pneumonia Classifier** 

Deployed using render: <https://pneumonia-classifier.onrender.com>  <Currently In Maintenance>

**--Model tuning still in progess** 

Pneumonia is an infection that causes inflammation in the lungs. X-rays are currently the best method in identifying pneumonia, however, X-rays have their limitations because they don't show which kind of bacteria is attacking the lungs and also generally the data we have is only the frontal view. Advances in deep learning have paved the way for AI to perform better than humans at many different tasks in healthcare. A research paper "CheXNet: Radiologist-Level Pneumonia Detection on Chest X-Rays with Deep Learning" https://arxiv.org/pdf/1711.05225v3.pdf ran a study where they evaluated the performance of classification for pneumonia and other infections while comparing their model scores with experienced radiologists. Using a pre-trained model (Imagenet) They were able to outperform radiologists using a 121 layer CNN which is a type of neural network most commonly used for computer vision.

**Dataset**

This data set is different than the one used in the CheXNet paper. Our data came from Kaggle, but thanks to the work of NIHS we have the opportunity to work on this dataset.

**Size: 1GB**
Approximately 6000 chest x-ray images



First our model was trained on Resnet
(more info about residual networks here <https://arxiv.org/pdf/1512.03385.pdf>)







![alt text](https://ujwlkarn.files.wordpress.com/2016/08/screen-shot-2016-08-07-at-4-59-29-pm.png?w=1493)
