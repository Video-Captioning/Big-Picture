# Classify the Images
See the Image Classification and Collage repository

We are going to use the scikit-learn implementation of K-means clustering, and the following files:

* cluster.py
* all_clusters.sh
* make_collage.py
* all_collages.sh


#### Parameters

* Input: `features_VGG16.csv`
* Number of Clusters: `90`    ( 2, 5, 10, 20, ..., 90 )
* Output: `labels_vgg16_90.csv`

#### Execution
First, let's try making 10 clusters:

`$ python3 cluster.py ./data/3_features/features_VGG16.csv -k 10 -o ./data/4_labels/labels_VGG16_10.csv`

Now let's try making various numbers of clusters:

`$ python3 cluster.py features_vgg16.csv -k 2 -o labels_vgg16.csv`

```bash
for n in 05 10 15 20 25 30 40 50 60 70 80 90
do
 echo 'python3 cluster.py ./data/3_features/features_VGG16.csv -k '$n' -o ./data/4_labels/labels_VGG16_'$n'.csv'
done
```

```bash
python3 cluster.py ./data/3_features/features_VGG16.csv -k 05 -o ./data/4_labels/labels_VGG16_05.csv
python3 cluster.py ./data/3_features/features_VGG16.csv -k 10 -o ./data/4_labels/labels_VGG16_10.csv
python3 cluster.py ./data/3_features/features_VGG16.csv -k 15 -o ./data/4_labels/labels_VGG16_15.csv
python3 cluster.py ./data/3_features/features_VGG16.csv -k 20 -o ./data/4_labels/labels_VGG16_20.csv
python3 cluster.py ./data/3_features/features_VGG16.csv -k 25 -o ./data/4_labels/labels_VGG16_25.csv
python3 cluster.py ./data/3_features/features_VGG16.csv -k 30 -o ./data/4_labels/labels_VGG16_30.csv
python3 cluster.py ./data/3_features/features_VGG16.csv -k 40 -o ./data/4_labels/labels_VGG16_40.csv
python3 cluster.py ./data/3_features/features_VGG16.csv -k 50 -o ./data/4_labels/labels_VGG16_50.csv
python3 cluster.py ./data/3_features/features_VGG16.csv -k 60 -o ./data/4_labels/labels_VGG16_60.csv
python3 cluster.py ./data/3_features/features_VGG16.csv -k 70 -o ./data/4_labels/labels_VGG16_70.csv
python3 cluster.py ./data/3_features/features_VGG16.csv -k 80 -o ./data/4_labels/labels_VGG16_80.csv
python3 cluster.py ./data/3_features/features_VGG16.csv -k 90 -o ./data/4_labels/labels_VGG16_90.csv
```

#### Collages
How well did the clustering work?

Let's make a collage to find out.

`python3 make_collage.py ./data/2_images/ ./data/4_labels/labels_vgg16_05.csv`

![Figure 1.](fig/fig1.png)

Figure 1 shows the first four clusters. Clusters 0 and 2 are good examples of active play. 

To train a classifer that can find images of active play:
1. Make a collage with a large number of clusters

   `python3 make_collage.py ./data/2_images/ ./data/4_labels/labels_vgg16_30.csv`

2. Manually select cluster IDs that are good examples of the desired activity

* choose clusters 0, 2, 5, 8, 11, 13, 15, 19, 23
* make a list of images in these clusters
  - From label file, labels_VGG16_30.csv:
      Label	File
      0	frame_00196.png
      0	frame_00199.png
      ...

```bash
for id in 0 2 5 8 11 13 15 19 23
do
  echo "awk -F '\t' '/^"$id"/{print \$2;}' ./data/4_labels/labels_VGG16_30.csv"
done
```

```
awk -F '\t' '/^0/{print $2;}' ./data/4_labels/labels_VGG16_30.csv
awk -F '\t' '/^2/{print $2;}' ./data/4_labels/labels_VGG16_30.csv
awk -F '\t' '/^5/{print $2;}' ./data/4_labels/labels_VGG16_30.csv
awk -F '\t' '/^8/{print $2;}' ./data/4_labels/labels_VGG16_30.csv
awk -F '\t' '/^11/{print $2;}' ./data/4_labels/labels_VGG16_30.csv
awk -F '\t' '/^13/{print $2;}' ./data/4_labels/labels_VGG16_30.csv
awk -F '\t' '/^15/{print $2;}' ./data/4_labels/labels_VGG16_30.csv
awk -F '\t' '/^19/{print $2;}' ./data/4_labels/labels_VGG16_30.csv
awk -F '\t' '/^23/{print $2;}' ./data/4_labels/labels_VGG16_30.csv
```

```bash
$ for id in 0 2 5 8 11 13 15 19 23; do   echo "awk -F '\t' '/^"$id"/{print \$2;}' ./data/4_labels/labels_VGG16_30.csv"; done | sh > keep.txt
```

List all the files:
`$ awk -F '\t' '{print $2;}' ./data/4_labels/labels_VGG16_30.csv > all.txt`

* make a list of images NOT in these clusters

Subtract keepers from all:
`grep -v -f keep.txt all.txt > toss.txt`

* build a training data set from these lists

`$ sed 's/.*/toss &/g' toss.txt > training`
`$ sed 's/.*/keep &/g' keep.txt >> training`
   
3. Train a classifier with two classes: desired activity( keep ) / other ( toss )

Dimensionality is too high! 513 features, only 630 rows
Cluster around average keeper, average tosser?


10. Featurize examples

`(tensorflow) ~/Dropbox/Projects/Video-Captioning$ python3 im2fea.py -m VGG16 --path ./examples/catches/ --output ./examples/catches/features_vgg16.csv`

4. Test the classifier
5. Refine and repeat

[back](README.md)
