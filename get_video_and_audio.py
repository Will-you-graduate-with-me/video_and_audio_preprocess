from utils.video_preprocess import *
from utils.arguments import *
from utils.open_txt_files import *

if __name__ == '__main__':

    txt_file_dir = './'
    download_path = './video'

    option_selected, txt_file_name, extract_audio = get_arguments()

    if option_selected == "yes":

        # 텍스트 파일에서 유튜브 링크 읽어오기
        if txt_file_name is None:
            print("no txt file name")
            exit()

        youtube_url_list = read_txt_files(txt_file_dir+txt_file_name)

        preprocessingVideoToAudio.download_video_from_youtube(download_path, youtube_url_list)

    if extract_audio =="yes":
        preprocessingVideoToAudio.change_video_to_audio(download_path, "wav")
