# importing the modules
import requests
import json
from bs4 import BeautifulSoup
from urllib.request import urlopen

with open('./neteaseURLList.txt') as input_file:
    url_list = input_file.read().splitlines()
    for index in range(len(url_list)):
        url = url_list[index]
        headers = {
            'Accept' : 'image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8',
            'Accept-Language' : 'en-US,en;q=0.9',
            'Cache-Control' : 'max-age=0',
            'Connection' : 'keep-alive',
            'Upgrade-Insecure-Requests' : '1',
            'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36 Edg/123.0.0.0'
        }
        # use referer to fake the request as a browser request
        headers['Referer'] = url
        reqs = requests.get(url, headers=headers)
        # news page data as a soup object
        soup = BeautifulSoup(reqs.text, 'html.parser').prettify()
        # hard code news ID
        news_ID = "J0C9ASJE000189FH"
        # hard code product key. can be found in soup object
        product_key = "a2869674571f77b5a0867c3d71db5856"
        comments_api = 'https://comment.api.163.com/api/v1/products/' + product_key + '/threads/' + news_ID
        # hard code board ID. can be found in soup object
        board_ID = "news2_bbs"
        # comment URL
        comment_url = "https://comment.news.163.com/" + board_ID + "/" + news_ID + ".html"

        comment_reqs = requests.get(comment_url, headers=headers)
        # comment page data as a soup object
        comment_soup = BeautifulSoup(comment_reqs.text, 'html.parser').prettify()
        # save comment page data to a file
        output_filename = './neteaseCommentOutput' + str(index) + '.txt'
        with open(output_filename, 'a') as output_file:
            output_file.write(comment_soup)

        ####################################################################################
        # cache_comment = str(urlopen(comments_api).read())
        # output_filename = './test01.txt'
        # with open(output_filename, 'a') as output_file:
        #     output_file.write(cache_comment)

        # boardId = re.findall(r'"boardId":"(\w+)"', str(urlopen(comments_api).read()))[0]
        # comments = ('https://comment.news.163.com/' + boardId + '/' + newsId + '.html')

        # output_filename = './neteaseOutput' + str(index) + '.txt'
        # with open(output_filename, 'a') as output_file:
        #     output_file.write(soup)
        # print(soup)
        ####################################################################################