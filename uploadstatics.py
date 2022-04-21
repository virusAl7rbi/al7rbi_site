
import os
import aiohttp
import asyncio
from aiohttp import ClientSession

from pprint import pprint

BASE_DIR = os.getcwd()
all_files = [os.path.join(root, file) for root, dirs, files in os.walk(os.path.abspath(os.getcwd() + "/static/")) for file in files]

async def fetch(session, path):
    if len(path.split("al7rbi_site/")) == 1:
        file_path = os.path.join(BASE_DIR,path.split("al7rbi_site\\")[1])
    else:
        file_path = os.path.join(BASE_DIR,path.split("al7rbi_site/")[1])
    data = open(file_path,'rb').read()
    path = "al7rbi_site"+path.split("al7rbi_site")[1]
    async with session.post(f"https://cdn.al7rbi.tk/upload?path={path}", data=data) as response:
        return await response.json()


async def fetch_all(urls, loop):
    async with aiohttp.ClientSession(loop=loop) as session:
        results = await asyncio.gather(*[fetch(session, url) for url in urls], return_exceptions=True)
        return results


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    urls = all_files
    upload_static = loop.run_until_complete(fetch_all(urls, loop))
