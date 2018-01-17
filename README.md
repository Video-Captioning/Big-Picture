# Video-Captioning
## Identify and describe the most interesting moments in sports videos
--------
[Overview](Overview.md)
--------
## Current Task
1. [Extract still images from the video](Excerpt.md)

`$ sh excerpt.sh ./data/1_video/2015bsVriot.mp4 ./data/2_images/ 00 3000`

2. [Extract Features From Images](Get-Features.md)

`$ python3 -W "ignore:compiletime:RuntimeWarning::0" im2fea.py -m VGG16 --path ./data/2_images/ --output ./data/3_features/features_vgg16.csv`

3. Manually collect images to use as training examples
```
 |-data
 |---0_training
 |-----announcer
 |-----catch
 |-----disc
 |-----fansinstands
 |-----highfive
 |-----hug
 |-----jerseys
 |-----layout
 |-----notplaying
 |-----pull
```

4. Train an SVM classifier on one category of examples, and then find similar images in the whole set, for example, fans in stands.

In general:
`$ python3 images_like_this.py path/to/images/ path/to/exemplars/ feature/file.csv --output collage.png`

Specifically:
`$ python3 images_like_this.py ./data/2_images/ ./data/0_training/fansinstands/ ./data/3_features/features_VGG16.csv --output collage.png`

Here are the training examples:
![Examples](./figures/positive_fansinstands.png?raw=true "Examples")

And here are the similar images:
![Results](./figures/predicted_fansinstands.png?raw=true "Results")

## Evaluate the accuracy of the classifier

The resulting images are similar to the examples, just not in the way I had envisioned! 'Group of people' might be a better description for the category. The results for the other categories were not encouraging. To capture small details, such as a disc, let's try a different approach.

## Histograms of Oriented Gradients (HoG)

Instead of using features extracted using a pre-trained VGG16 model, compute HoGs as follows:

`./HoG.R  -o ./data/3_features/HoG.csv ./data/2_images/`

Then try re-clustering:
`$ python3 images_like_this.py ./data/2_images/ ./data/0_training/fansinstands/ ./data/3_features/HoG.csv`


## Other
[Learning Where to Look](Where-To-Look-Next.md)

[Captioning](Captioning.md)

[Hardware & Configuration](Hardware-And-Config.md)

[Bibliography](Bibliography.md)

[Toolbox](Toolbox.md)
