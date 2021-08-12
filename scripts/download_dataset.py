import shutil
from pathlib import Path

import gdown
import tqdm


URLS = [
    'https://drive.google.com/uc?export=download&id=0BwmD_VLjROrfTHk4NFg2SndKcjQ',  # CNN stories
    'https://drive.google.com/uc?export=download&id=0BwmD_VLjROrfM1BxdkxVaTY2bWs',  # Daily Mail stories
]
DOWNLOAD_PATH = Path('downloaded')
TARGET_PATH = Path('raw_stories')

DOWNLOAD_PATH.mkdir(exist_ok=True)
TARGET_PATH.mkdir(exist_ok=True)


def download_data():
    for url in URLS:
        url_id = url.split('id=')[1]
        if not (DOWNLOAD_PATH / url_id).exists():
            print(f'Downloading {url}...')
            gdown.download(url, str(DOWNLOAD_PATH / url_id), quiet=True)

    for archive_path in DOWNLOAD_PATH.iterdir():
        print(f'Extracting {archive_path}...')
        shutil.unpack_archive(archive_path, str(DOWNLOAD_PATH), format='gztar')

    story_files = list(DOWNLOAD_PATH.rglob('*.story'))
    for story_file in tqdm.tqdm(story_files, desc='Merging folders'):
        shutil.move(str(story_file), str(TARGET_PATH))

    print(f"Removing '{DOWNLOAD_PATH}'...")
    shutil.rmtree(str(DOWNLOAD_PATH), ignore_errors=True)

    print('Done.')


if __name__ == '__main__':
    download_data()
