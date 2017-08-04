import pandas as pd
import asyncio
import time


async def parse_and_save_result(url):
    data_html = pd.read_html(url)
    data_html[0].to_json('test.json')
    data_html[0].to_csv('test.xlsx')


async def accept_url(url):
    await parse_and_save_result(url)

if __name__ == '__main__':
    a = time.time()
    loop = asyncio.get_event_loop()
    loop.run_until_complete(accept_url('https://coinmarketcap.com/all/views/all/'))
    loop.close()
    print(time.time() - a)

