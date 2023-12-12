import asyncio
from pathlib import Path
from timeit import default_timer
import httpx
from bs4 import BeautifulSoup


class Task:
    def __init__(self, url, filename):
        super().__init__()
        self.url: str = url
        self.filename: str = filename
        self.directory: str = 'memy-async'

    def _write(self, resp, filename):
        with open(Path(__file__).parent / self.directory / filename, 'wb') as png_file:
            png_file.write(resp.content)

    async def download_img(self, client: httpx.AsyncClient, filename: str) -> None:
        response = await client.get(self.url)
        self._write(response, filename)


async def bs4_download_images(response, client):

    # scrap html
    html = BeautifulSoup(response.text, 'html.parser')
    # find all img tags in html
    img_tags = html.find_all('img', attrs={'class': 'full-image'})
    # creates download task for each TAG, then appended to list tasks ( work to be done )
    tasks = []
    try:
        for i, img in enumerate(img_tags):
            task = Task(img.attrs['src'], f'{i}.jpg')
            downloaded_img = await task.download_img(client, f'{i}.jpg')
            tasks.append(downloaded_img)
            # execution of all tasks in given list at once
        await asyncio.gather(*tasks)
    except TypeError:
        asyncio.gather().cancel()


async def main():
    # start timer
    before = default_timer()

    url = 'https://kwejk.pl/'
    async with httpx.AsyncClient() as client:
        resp = await client.get(url)

        await bs4_download_images(resp, client)

    # stop timer
    after = default_timer()
    print('Czas trwania programu: ', after - before)

if __name__ == "__main__":
    asyncio.run(main())

