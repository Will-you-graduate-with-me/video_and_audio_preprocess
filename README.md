유튜브 동영상 다운 및 오디오 추출
------
### 1. 패키지 설치
```
pip install -r requirements.txt 
```
### 2. 코드 실행

youtube 링크로 다운받을 경우 유튜브 링크를 포함한 텍스트 파일을 ./ 위치에 저장해두고 실행</br>
텍스트 파일 이름을 입력하지 않고 실행할 경우 다운이 진행되지 않고 종료
```
python get_video_and_audio.py --youtube yes --fn filename.txt
```

기존 로컬 파일에 존재하는 동영상으로 audio 추출만 할 경우 ./video 폴더를 만든 뒤에 동영상을 옮겨 담고 실행</br>
```
python get_video_and_audio.py --youtube no
```
##### video 파일에는 다운로드 된 동영상들이 저장되고, audio 파일에는 video 파일에서 각각 추출된 audio 파일들이 저장됩니다. 

### 3. optional arguments
```
optional arguments:
  -h, --help          show this help message and exit
  --youtube {yes,no}  Choose whether download from youtube or not yes or no
  --fn FN             Type text file name of youtube links (with the
                      extension)
```
