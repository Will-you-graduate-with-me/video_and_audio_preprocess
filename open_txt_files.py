def read_txt_files(txt_dir):

    youtube_links = list()

    f = open(txt_dir, 'r')
    while True:
        line = f.readline()
        if not line: break
        youtube_links.append(line) #리스트에 각 유튜브 링크 추가

    print("finished moving Youtube links")
    print(youtube_links)
    f.close()

    return youtube_links