## Experiments

### Image Classification

----------
Configuration A

* 3471 images, excerpted from 2015bsVriotV.mp4, roughly 1 hour at about 1 frame per second
* Manually select training images in a handfull of categories: fansinstands, highfive, disc, announcer, etc.
----------

[Experiment #1](Experiment1.md): Extract features from images using VGG16 model, pre-trained on ImageNet; Try to predict similar images, given a small number of examples. Result: POOR. Predicted images have little in common with exemplars.

[Experiment #2](Experiment2.md): Calculate HoG for images; Try to predict similar images, given a small number of examples.

#### Configuration B ...
