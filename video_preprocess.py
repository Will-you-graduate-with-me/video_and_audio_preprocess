import moviepy.editor as mp
import youtube_dl
import os
from tqdm import tqdm


class preprocessingVideoToAudio:

    def download_video_from_youtube(output_dir, youtube_video_list):

        # title : 동영상 이름
        # ext : 동영상 확장자
        download_path = os.path.join(output_dir, '%(title)s.%(ext)s')

        for video_url in tqdm(youtube_video_list):

            # youtube_dl options
            ydl_opts = {
                'format': 'best/best',  # 가장 좋은 화질로 선택(화질을 선택하여 다운로드 가능)
                'outtmpl': download_path,  # 다운로드 경로 설정
                'writeautomaticsub': False,  # 자동 생성된 자막 다운로드
            }

            try:
                with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                    ydl.download([video_url])
                print("finished downloading videos")
            except Exception as e:
                print('error', e)

    def change_video_to_audio(video_path, audio_type):

        # video_path : 동영상 경로
        # audio_type : 오디오 확장자명

        # print(os.listdir(video_path))

        # 디렉토리에 동영상 존재 여부 확인
        if not os.listdir(video_path):
            print('no videos found')
        else:
            print('videos found')

        video_list = os.listdir(video_path)

        # 변환된 audio 파일 저장할 공간
        download_audio_path = './audio/'

        # 디렉토리 없을 경우에 생성
        os.makedirs(download_audio_path, exist_ok=True)

        # 동영상에서 오디오로 변환
        for video in tqdm(video_list):
            audio = video[:len(video) - 4] + "_audio." + audio_type

            print(video)

            clip = mp.VideoFileClip(video_path + "/" + video)
            clip.audio.write_audiofile(download_audio_path + audio)

        print("finished converting to " + audio_type)

