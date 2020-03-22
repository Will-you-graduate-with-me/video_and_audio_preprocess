download videos from Youtube and extract wav files
------
### 1. package installation
```
pip install -r requirements.txt 
```
### 2. how to run

to download videos with youtube links, locate a text file with youtube links in ./ directory. </br>
download won't proceed without the filename. 
```
python get_video_and_audio.py --youtube yes --fn filename.txt --audio yes
```

download videos from youtube but no extraction of audio files. </br>
```
python get_video_and_audio.py --youtube yes --fn filename.txt --audio no
```

move your videos to ./video directory if downloading from youtube is not necessary. </br>
run the below code only to get the extracted audios from ./video directory.
```
python get_video_and_audio.py --youtube no --audio yes
```

##### downloaded videos will be saved in ./video directory and extracted audio files will be saved in ./audio directory.
### 3. Optional Arguments
```
optional arguments:
  -h, --help          show this help message and exit
  --youtube {yes,no}  Choose whether to download from youtube or not
  --fn FN             Type text file name of youtube links (with the
                      extension)
  --audio {yes,no}    Choose whether to extract audio or not

```
