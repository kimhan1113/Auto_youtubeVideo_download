import pytube
import youtube_web_crawling
from tqdm import tqdm
import os

# 원하는 유튜버 채널 동영상 경로
url = 'https://www.youtube.com/channel/UCz0YYhcLUgEj2uFWdTRQ_Uw/videos'
#크롤링 작업 코드
url_list = youtube_web_crawling.url_crawling(url)

# 저장할 경로
down_path = 'D:\english_lecture\skull'

def video_down(lists):

    error_list = []

    for i in tqdm(range(len(lists))):

        # 에러나는건 걍 거르자...
        # pytube.exceptions.RegexMatchError: get_ytplayer_config: could not find match for config_patterns

        try:
            ytd = pytube.YouTube(str(lists[i]))
            streams = ytd.streams.filter(progressive=True, file_extension='mp4').all()

            res = ''

            for e in streams:

                if e.resolution == '720p':
                    res = e.itag

                # 720p 없을지는 모르겠지만 혹시라도 없을 경우를 위해 아래 코드를 만듬.
                # 저화질이라도 필요할 경우 아래 코드 주석을 풀면 된다.

                # elif e.resolution == '360p':
                #     res = e.itag

                else:
                    continue

            video = ytd.streams.get_by_itag(int(res))
            video.download(down_path)

        except:
            print('\n' + lists[i])
            error_list.append(lists[i])
            continue

    # 에러목록이 비어있지 않으면.. 로그파일을 생성해 해당 url목록을 저장한다.
    if error_list:
        with open(os.path.join(down_path, 'log.txt'), 'w') as f:
            for v in error_list:
                f.write(v + '\n')

if __name__ == '__main__':
    video_down(url_list)
    print('done')