#/usr/bin/bash
project='Whitman_v_Stanford'

for model in XCEPTION VGG16 VGG19 RESNET50 INCEPTIONV3 INCEPTIONRESNETV2 MOBILENET
do
 for n in 50 40 30 25 20 15 10
 do
  echo 'python3 make_collage.py ~/VLC_stuff/frames/'$project'/' 'labels_'$n'_'$model'.csv -o '$model'_'$n'.png'
 done
done
