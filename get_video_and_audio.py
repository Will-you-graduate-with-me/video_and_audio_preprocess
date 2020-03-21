from video_preprocess import *

if __name__ == '__main__':

    youtube_url_list = [
        "https://www.youtube.com/watch?v=dP15zlyra3c",
        "https://www.youtube.com/watch?v=M25AP_KPwlI"
    ]

    download_path = './video'

    preprocessingVideoToAudio.download_video_from_youtube(download_path, youtube_url_list)
    preprocessingVideoToAudio.change_video_to_audio(download_path, "wav")