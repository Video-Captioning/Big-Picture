#/usr/bin/bash
for model in XCEPTION VGG16 VGG19 RESNET50 INCEPTIONV3 INCEPTIONRESNETV2 MOBILENET
do
 for n in 50 40 30 25 20 15 10 
 do
  echo 'python3 cluster.py features_'$model'.csv -k '$n' -o labels_'$n'_'$model'.csv'
 done
done
