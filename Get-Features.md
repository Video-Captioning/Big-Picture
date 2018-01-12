# Extract Features From Images
Next, we are going to use a pre-trained model to extract features from the images we just excerpted from the video.

See the Feature Extraction repository, [ImageFeatures](https://github.com/KarlEdwards/ImageFeatures.git)

1. Activate TensorFlow:
`$ source ~/tensorflow/bin/activate`

2. Extract features, in this case, using VGG16:

    `python3 im2fea.py -m VGG16 --path ./data/2_images/ --output ./data/3_features/features_VGG16.csv`

3. Now repeat for all available models

```
for model in XCEPTION VGG16 VGG19 RESNET50 INCEPTIONV3 INCEPTIONRESNETV2 MOBILENET
do
 echo 'python3 -W "ignore:compiletime:RuntimeWarning::0" im2fea.py -m '$model' --path ~/VLC_stuff/frames/2015bsVriot_play --output features_'$model'.csv'
done
```

This script produces another script to repeat the process for all models. Why write a script to produce another script? To allow for a sanity-check before starting a time-consuming process.

```
python3 -W "ignore:compiletime:RuntimeWarning::0" im2fea.py -m XCEPTION --path ~/VLC_stuff/frames/2015bsVriot_play --output features_XCEPTION.csv
python3 -W "ignore:compiletime:RuntimeWarning::0" im2fea.py -m VGG16 --path ~/VLC_stuff/frames/2015bsVriot_play --output features_VGG16.csv
python3 -W "ignore:compiletime:RuntimeWarning::0" im2fea.py -m VGG19 --path ~/VLC_stuff/frames/2015bsVriot_play --output features_VGG19.csv
python3 -W "ignore:compiletime:RuntimeWarning::0" im2fea.py -m RESNET50 --path ~/VLC_stuff/frames/2015bsVriot_play --output features_RESNET50.csv
python3 -W "ignore:compiletime:RuntimeWarning::0" im2fea.py -m INCEPTIONV3 --path ~/VLC_stuff/frames/2015bsVriot_play --output features_INCEPTIONV3.csv
python3 -W "ignore:compiletime:RuntimeWarning::0" im2fea.py -m INCEPTIONRESNETV2 --path ~/VLC_stuff/frames/2015bsVriot_play --output features_INCEPTIONRESNETV2.csv
python3 -W "ignore:compiletime:RuntimeWarning::0" im2fea.py -m MOBILENET --path ~/VLC_stuff/frames/2015bsVriot_play --output features_MOBILENET.csv
```

After convincing myself this is really what I want to do, I paste the generated script into the terminal window and go do something else for a few minutes while the feature extraction occurs.

Which pre-trained model is best (for our purposes?)

If there were no discernable difference in the ability of each model to classify our images, the model having the smallest number of features might be preferrable.

How many feature columns have been produced by each model?

For mobilenet:

`$ awk -F , '(NR<2){print NF}' features_mobilenet.csv`

`1025`

For all models:

```
$ for model in XCEPTION VGG16 VGG19 RESNET50 INCEPTIONV3 INCEPTIONRESNETV2 MOBILENET
    do
      awk -F , '(NR<2){ fn=gensub( "(features_)(.*)(.csv)","\\2", "g", FILENAME ); printf( "%20s\t%4d\n", fn, NF ) }' features_$model.csv
    done
```

```
            XCEPTION	2049
               VGG16	 513
               VGG19	 513
            RESNET50	2049
         INCEPTIONV3	2049
   INCEPTIONRESNETV2	1537
           MOBILENET	1025
```

Let's see what VGG16 can do!

[back](README.md)
