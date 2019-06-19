
# encoding: utf-8

import re

def is_domain(domain):
    domain_regex = re.compile(
        r'(?:[A-Z0-9_](?:[A-Z0-9-_]{0,247}[A-Z0-9])?\.)+(?:[A-Z]{2,6}|[A-Z0-9-]{2,}(?<!-))\Z', re.IGNORECASE)
    return True if domain_regex.match(domain) else False

def Duplicate_removal():
    file_list = []
    file_txt = 'url.txt'
    with open(file_txt,'r',encoding='utf-8') as f:
        file_txt_2 = f.readlines()
        for flie in file_txt_2:
            file_list.append(flie)
        out_file = list(set(file_list))
        for out in out_file:
            with open('result.txt','a+') as f:
                f.write(out + '\n')