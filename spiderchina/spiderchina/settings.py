# -*- coding: utf-8 -*-

# Scrapy settings for spiderchina project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'spiderchina'

SPIDER_MODULES = ['spiderchina.spiders']
NEWSPIDER_MODULE = 'spiderchina.spiders'
DOWNLOAD_DELAY=1
# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'spiderchina (+http://www.yourdomain.com)'
