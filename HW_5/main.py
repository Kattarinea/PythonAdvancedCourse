import asyncio
import argparse
from pic_downloader import pic_download
from Path_to_artifacts import PathsToArtifacts
from scraper import scrape_cian
from aiomisc import new_event_loop, PeriodicCallback


def get_args():
    parser = argparse.ArgumentParser()

    parser.add_argument('-num_pic', default=3, help='Указание количества картинок для скачивания')
    parser.add_argument('-path', default=PathsToArtifacts.PATH_TO_ARTIFACTS.value,
                        help='Указание пути, куда будет картинка скачана')
    parser.add_argument('-cian', nargs='?', const='', help='Выгружаем данные с Циан')
    parser.add_argument('-pages', default=1, help='Количество страниц')

    return parser.parse_args()


if __name__ == '__main__':
    args = get_args()
    if args.cian is not None:
        loop = new_event_loop()
        periodic_callback = PeriodicCallback(scrape_cian, int(args.pages))
        periodic_callback.start(1, delay=3600)
        loop.run_forever()
    else:
        asyncio.run(pic_download(int(args.num_pic), args.path))
