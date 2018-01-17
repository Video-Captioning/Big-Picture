# Experiment #1

[Extract Features From Images](Get-Features.md)

`$ python3 -W "ignore:compiletime:RuntimeWarning::0" im2fea.py -m VGG16 --path ./data/2_images/ --output ./data/3_features/features_vgg16.csv`

Train an SVM classifier on one category of examples, and then find similar images in the whole set, for example, fans in stands.

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
