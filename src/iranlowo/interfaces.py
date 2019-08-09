import scrapy


class Scrapper(scrapy.Spider):
    """
    Interface for scrapping data from :mod:`iranlowo.scrapper`
    """

    def __init__(self, name, urls, **kwargs):
        super(Scrapper, self).__init__(name, **kwargs)

    def parse(self, response):
        pass

