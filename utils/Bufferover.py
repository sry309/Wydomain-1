import asyncio
from pyppeteer import launch
import json

from config import *

class search_Bufferover(object):
    def __init__(self,domain):
        self.domain = domain
        self.url = 'http://dns.bufferover.run/'

    def run(self):
        url = '{0}dns?q={1}'.format(self.url,self.domain)
        try:
            async def main():
                browser = await launch({'args':['--no-sandbox']})
                page = await browser.newPage()
                await page.goto('{0}'.format(url))
                await asyncio.sleep(5)
                content = await page.content()
                Json_data = json.loads(content[84:-20])
                Json_data_A = Json_data['FDNS_A']
                for sub in Json_data_A:
                    #print(sub.split(',')[1])
                    if is_domain(sub.split(',')[1]):
                        print(sub.split(',')[1])
                        with open('url.txt','a') as f:
                            f.write(sub.split(',')[1] + '\n')
                await browser.close()
            asyncio.get_event_loop().run_until_complete(main())
        except Exception as e:
            print(e)
