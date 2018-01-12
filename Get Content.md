# Get some video
First, we will need some data. Let's use the [Women's Final from the 2015 National Championships](https://www.youtube.com/watch?v=ULzQS2rv34s), in which Boston Brute Squad takes on Seattle Riot in Frisco, Texas.

One way to save a video from the web is to use the command-line interface to VLC, for example:
```bash
$ vlc -v -I rc --no-sout-audio --sout='#transcode{ vcodec=h264, vb=800, scale=1 }:std{ access=file,
mux=ts, dst=/path/to/resulting/video.mp4 }' https://www.youtube.com/watch?v=ULzQS2rv34s/ vlc://quit
```

[back](README.md)
