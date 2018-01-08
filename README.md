# Video-Captioning
Identify and describe the most interesting moments in sports videos
--------

To illustrate the concepts, let's focus on this specific application:

* The sport of Ultimate Frisbee, specifically women's ultimate
* Interesting moments: 
  - During Play: Pulls, Catches, Layouts
  - Between Plays: Scoreboard, High-Fives, Fans in Stands, Miscellaneous

--------

### Inspiration
During MLConf Seattle May 19, 2017, Serena Yeung's presentation, 'Towards Scaling Video Understanding' piqued my curiosity.
Soon after the conference, I read a paper she co-authored, 'End-to-end Learning of Action Detection from Frame Glimpses in Videos.' CVPR 2016 Yeung, Russakovsky, Mori, Fei-Fei.
The basic idea is to peek at the video for a few frames at an arbitrarily selected point in time,
then look at another point some distance away in order to learn how far, and in which direction,
to look for something interesting to annotate.
### Initial Exploration
First, we will need some data. Let's use the [Women's Final from the 2015 National Championships](https://www.youtube.com/watch?v=ULzQS2rv34s), in which Boston Brute Squad takes on Seattle Riot in Frisco, Texas.

One way to save a video from the web is to use the command-line interface to VLC, for example:
```bash
$ vlc -v -I rc --no-sout-audio --sout='#transcode{ vcodec=h264, vb=800, scale=1 }:std{ access=file,
mux=ts, dst=/path/to/resulting/video.mp4 }' https://www.youtube.com/watch?v=ULzQS2rv34s/ vlc://quit
```
A few techniques will be needed in order to achieve our goal: 
* Feature Extraction
* Video Excerpting
* Image Classification
* Learning Where to Look
* Captioning

#### Feature Extraction
See the Feature Extraction repository

#### Video Excerpting
See the Video Excerpting respository

#### Image Classification
See the Image Classification and Collage respository

#### Learning Where to Look

#### Captioning

### Hardware & Configuration

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

