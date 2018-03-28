# -*- coding: utf-8 -*-
BOT_NAME = 'scrapy_project'

SPIDER_MODULES = ['scrapy_project.spiders']
NEWSPIDER_MODULE = 'scrapy_project.spiders'

ROBOTSTXT_OBEY = True

ITEM_PIPELINES = {
    # 'scrapy_project.pipelines.DownloaderPipeline': 300,
}
