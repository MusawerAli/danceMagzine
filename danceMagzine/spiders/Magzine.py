import scrapy
import requests
from parsel import Selector
import csv
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from scrapy.selector import Selector


class MagzineSpider(scrapy.Spider):
    name = 'Magzine'
    start_urls = [
        'https://cgsearch.dancemagazine.com/search.php']

    def __init__(self):
        self.driver = webdriver.Firefox()

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

        yield {
            'html': html,
            # 'data': data

        }

        # self.driver.close()
