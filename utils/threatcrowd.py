import re
import requests
import json
import time
from config import *

class search_threatcrowd(object):
    def __init__(self,domain):
        self.domain = domain
        self.url = 'https://www.threatcrowd.org/'

    def run(self):
        try:
            url = '{0}/searchApi/v2/domain/report/?domain={1}'.format(self.url,self.domain)
            time.sleep(10)
            r = requests.get(url).text
            for sub in json.loads(r).get("subdomains"):
                if is_domain(sub):
                    print(sub)
                    with open('url.txt','a') as f:
                        f.write(sub + '\n')
        except Exception as e:
            print(e)