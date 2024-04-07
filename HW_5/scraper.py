import asyncio
from bs4 import BeautifulSoup
import json
import random
import aiofiles
from fake_useragent import UserAgent
from Path_to_artifacts import PathsToArtifacts
import aiohttp


async def parser(session, page, headers, random_sleep):
    url = PathsToArtifacts.PATH_TO_SITE_CIAN.value
    base_url = url + f'?page={page}'
    await asyncio.sleep(random_sleep)
    async with session.get(base_url, headers=headers) as response:
        if response.status == 200:
            html = await response.text()
            soup = BeautifulSoup(html, 'html.parser')

            listings = soup.select('._93444fe79c--wrapper--W0WqH')
            count = 0
            data_json = []
            for listing in listings[0].contents:
                rows = listing.select('._93444fe79c--row--kEHOK')
                if rows:
                    if len(rows) == 6:
                        flat_describe = rows[1].text.strip()
                        address = rows[2].text.strip()
                        price = rows[3].text.strip()
                        info = rows[4].text.strip()
                    else:
                        flat_describe = rows[0].text.strip()
                        address = rows[1].text.strip()
                        price = rows[2].text.strip()
                        info = rows[3].text.strip()
                    count += 1
                    data_json.append({
                        'count': count,
                        'Address': address,
                        'Flat_describe': flat_describe,
                        'Price': price,
                        'Info': info
                    })

            async with aiofiles.open(f'artifacts/cian_data.json', 'a+', encoding='utf-8') as f:
                await f.write(json.dumps(data_json, ensure_ascii=False, indent=4))
        else:
            print(f'Bad response status: {response.status}')


async def scrape_cian(pages):
    user_agent = UserAgent().random
    headers = {
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "user-agent": user_agent
    }

    async with aiohttp.ClientSession(headers=headers) as session:
        tasks = []

        for page in range(1, pages + 1):
            random_sleep = random.uniform(5, 20)
            task = asyncio.create_task(parser(session, page, headers, random_sleep))
            tasks.append(task)

        await asyncio.gather(*tasks)
