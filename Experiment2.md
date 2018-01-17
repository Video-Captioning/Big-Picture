# Experiment #2
## Histograms of Oriented Gradients (HoG)

1. Compute HoGs for the images:
```bash
./HoG.R --cells=1  --bins=9 -o ./data/3_features/HoG_01cells_09bins.csv ./data/2_images/
./HoG.R --cells=4  --bins=9 -o ./data/3_features/HoG_04cells_09bins.csv ./data/2_images/
./HoG.R --cells=9  --bins=9 -o ./data/3_features/HoG_09cells_09bins.csv ./data/2_images/
./HoG.R --cells=16 --bins=9 -o ./data/3_features/HoG_16cells_09bins.csv ./data/2_images/

./HoG.R --cells=1  --bins=9 -o ./data/3_features/HoG_01cells_05bins.csv ./data/2_images/
./HoG.R --cells=4  --bins=9 -o ./data/3_features/HoG_04cells_05bins.csv ./data/2_images/
./HoG.R --cells=9  --bins=9 -o ./data/3_features/HoG_09cells_05bins.csv ./data/2_images/
./HoG.R --cells=16 --bins=9 -o ./data/3_features/HoG_16cells_05bins.csv ./data/2_images/
```

2. Then try re-clustering:

In general:

`$ python3 images_like_this.py path/to/images/ path/to/exemplars/ feature/file.csv`

Using image features extracted from pre-trained VGG16 model:

`$ python3 images_like_this.py ./data/2_images/ ./data/5_exemplars/ ./data/3_features/features_VGG16.csv`

Using Histograms of Oriented Gradients:

`$ python3 images_like_this.py ./data/2_images/ ./data/5_exemplars/ ./data/3_features/HoG_01cells_05bins.csv`






-------------

## Other
[Learning Where to Look](Where-To-Look-Next.md)

[Captioning](Captioning.md)

[Hardware & Configuration](Hardware-And-Config.md)

[Bibliography](Bibliography.md)

[Toolbox](Toolbox.md)
