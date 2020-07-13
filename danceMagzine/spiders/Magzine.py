import scrapy
import requests
from parsel import Selector
import csv
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from scrapy.selector import Selector
from urllib.parse import urlparse, urljoin
from urllib.parse import urljoin
from scrapy.linkextractors.lxmlhtml import LxmlLinkExtractor
import re
from scrapy import Request
from scrapy import Spider
import urllib.parse


class MagzineSpider(scrapy.Spider):
    name = 'Magzine'
    start_urls = [
        'https://cgsearch.dancemagazine.com/search.php']
    search_url = "https://cgsearch.dancemagazine.com/"

    def __init__(self):
        self.driver = webdriver.Firefox()

    def parse_results_page(self, response):

        yield{
            'urls': response}
        # urls = dataa.xpath(
        #     '//*[@style="float:left;max-width:600px"]//div//text()').extract()

        # sel = Selector(response)
        # yield{
        #     'data': sel
        # }

    def parse(self, response):
        self.driver.get(response.url)
        check_boxes = ["genre_performance",
                       "genre_choreography_composition", "genre_ballet", "genre_modern_contemporary"]
        for key in check_boxes:
            self.driver.find_element_by_name(key).click()
        sleep(5)
        self.driver.find_element_by_xpath(
            '/html/body/a/div/div/form/table/tbody/tr[19]/td/input').click()
        sleep(4)
        html = self.driver.page_source
        # self.driver.get(response.url)
        # sleep(3)
        # data = self.driver.find_element(
        #     By.NAME, "genre_performance").click()
        # sleep(3)
        data = Selector(text=html).css('span::text').getall()

        urlsData = Selector(text=html).css('a').xpath('@href').getall()
        for page_url in urlsData:
            page_url = urljoin(self.search_url, page_url)
            yield {
                'data': page_url
            }
            yield Request(page_url, callback=self.parse_results_page)

        # item_urls = self.sel.xpath('//*[@style="float:left;max-width:600px"]//div//text()').extract()

    # yield {
    #     'html': data,
    #     # 'data': data

    # }

        self.driver.close()
