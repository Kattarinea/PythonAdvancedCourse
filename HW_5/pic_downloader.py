import aiohttp
import os
import aiofiles
import asyncio
from Path_to_artifacts import PathsToArtifacts


async def pic_download(num_images, path):
    os.makedirs(path, exist_ok=True)
    headers = {'Connection': 'close', 'Cache-Control': 'no-cache'}
    async with aiohttp.ClientSession(headers=headers) as session:
        url = PathsToArtifacts.PATH_TO_SITE_PIC.value
        for i in range(num_images):
            file = os.path.join(path, f'pic_{i + 1}.jpg')

            async with session.get(url, headers=headers) as response:
                if response.status == 200:
                    img = await response.content.read()
                    async with aiofiles.open(file, 'wb') as img_file:
                        await img_file.write(img)
                else:
                    print(f'Bad response status: {response.status}')
            await asyncio.sleep(1)
