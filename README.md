# Video-Captioning
## Identify and describe the most interesting moments in sports videos
--------

To illustrate the concepts, let's focus on this specific application:

* The sport of Ultimate Frisbee, specifically women's ultimate
* Interesting moments: 
  - During Play: Pulls, Catches, Layouts
  - Between Plays: Scoreboard, High-Fives, Fans in Stands, Miscellaneous

--------

## Inspiration
During MLConf Seattle May 19, 2017, Serena Yeung's presentation, 'Towards Scaling Video Understanding' piqued my curiosity.
Soon after the conference, I read a paper she co-authored, 'End-to-end Learning of Action Detection from Frame Glimpses in Videos.' CVPR 2016 Yeung, Russakovsky, Mori, Fei-Fei.
The basic idea is to peek at the video for a few frames at an arbitrarily selected point in time,
then look at another point some distance away in order to learn how far, and in which direction,
to look for something interesting to annotate.

--------

## Step-By-Step Exploration

### Step 1: Get some video
First, we will need some data. Let's use the [Women's Final from the 2015 National Championships](https://www.youtube.com/watch?v=ULzQS2rv34s), in which Boston Brute Squad takes on Seattle Riot in Frisco, Texas.

One way to save a video from the web is to use the command-line interface to VLC, for example:
```bash
$ vlc -v -I rc --no-sout-audio --sout='#transcode{ vcodec=h264, vb=800, scale=1 }:std{ access=file,
mux=ts, dst=/path/to/resulting/video.mp4 }' https://www.youtube.com/watch?v=ULzQS2rv34s/ vlc://quit
```
A few techniques will be needed in order to achieve our goal: 
* Video Excerpting
* Feature Extraction
* Image Classification
* Learning Where to Look
* Captioning

### Step 2: Extract still images from the video

Since our video is nearly two hours long, let's grab an excerpt of just a few minutes, and sample a few frames per second from that excerpt. See the [Video Excerpting repository](https://github.com/KarlEdwards/Practical-VLC.git)

#### Parameters

* Input: `~/VLC_stuff/2015bsVriot.mp4`
* Start time: `3600` ( seconds from beginning of video )
* Duration: `60` ( seconds )
* Output: `./`  ( current directory )

#### Execution
Putting it all together as follows:

```$ sh excerpt.sh ~/VLC_stuff/2015bsVriot.mp4 ./ 3600 60```

yields a series of a few hundred frames from the video, each frame in a file having a name like frame_0####.png

### Step 3: Feature Extraction
Next, we are going to use a pre-trained model to extract features from the images we just excerpted from the video.

See the [Feature Extraction repository](https://github.com/KarlEdwards/ImageFeatures.git)

1. Activate TensorFlow:
`$ source ~/tensorflow/bin/activate`

2. Extract features, in this case, using MOBILENET:

    `python3 im2fea.py -m MOBILENET --path /to/image/files/ --output features_mobilenet.csv`

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

### Step 4: Image Classification
See the Image Classification and Collage respository

### Step 5: Learning Where to Look

### Step 6: Captioning

--------

## Hardware & Configuration

* Model Name:	Mac mini
* Model Identifier:	Macmini7,1
* Processor Name:	Intel Core i7
* Processor Speed:	3 GHz
* Number of Processors:	1
* Total Number of Cores:	2
* L2 Cache (per Core):	256 KB
* L3 Cache:	4 MB
* Memory:	8 GB
* Boot ROM Version:	MM71.0220.B07
* SMC Version (system):	2.24f32

### Bibliography

### Toolbox
* [VLC](https://www.videolan.org/vlc/index.html)-2.2.8
* [Tensorflow](https://www.tensorflow.org/install/install_mac)
* [Python3](https://wsvincent.com/install-python3-mac/)

