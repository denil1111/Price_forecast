# -*- coding: utf-8 -*-

# Scrapy settings for spider project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'spider'

SPIDER_MODULES = ['spider.spiders']
NEWSPIDER_MODULE = 'spider.spiders'
USER_AGENT = 'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_2; en-US) AppleWebKit/533.3 (KHTML, like Gecko) Chrome/5.0.354.0 Safari/533.3'  
WEBKIT_DOWNLOADER=['kaw','kawsi']
DOWNLOAD_DELAY=10
DOWNLOAD_TIMEOUT = 15
COOKIES_ENABLED = False
RETRY_ENABLED = False
RANDOMIZE_DOWNLOAD_DELAY = True
DOWNLOADER_MIDDLEWARES = {
    'spider.spiders.mid.WebkitDownloader': 543,
    # 'spider.spiders.mid.WebkitDownloader': 600,
    # 'spider.spiders/.mid.WebkitDownloader': 700,
    # 'spider.spiders.mid.WebkitDownloader': 800,
}   
 
import os
os.environ["DISPLAY"] = ":21"
# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'spider (+http://www.yourdomain.com)'
