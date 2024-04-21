# importing the modules
import requests
import time
from random import randint
from bs4 import BeautifulSoup


with open('./urlList.txt') as input_file:
    url_list = input_file.read().splitlines()
    for index in range(len(url_list)):
        url = url_list[index]
        headers = {
            'Accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'Accept-Language' : 'en-US,en;q=0.9',
            'Cache-Control' : 'max-age=0',
            'Connection' : 'keep-alive',
            'Host' : 'weibo.cn',
            'Upgrade-Insecure-Requests' : '1',
            'User-Agent' : 'Mozilla/5.0 (Linux; U; Android 1.1; en-gb; dream) AppleWebKit/525.10  (KHTML, like Gecko) Version/3.0.4 Mobile Safari/523.12.2'
        }
        reqs = requests.get(url, headers=headers)

        soup = BeautifulSoup(reqs.text, 'html.parser').prettify()
        
        output_filename = './output' + str(index) + '.txt'
        with open(output_filename, 'a') as output_file:
            output_file.write(soup)
        print(soup.title.string)