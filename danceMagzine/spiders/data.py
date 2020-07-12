
# import requests
# from parsel import Selector
# import csv
# from selenium import webdriver
# from time import sleep
# from selenium.webdriver.common.by import By


# driver = webdriver.Chrome()

# driver.get(
#     'https://cgsearch.dancemagazine.com/search.php')
# sleep(2)
# check_boxes = ["genre_performance",
#                "genre_choreography_composition", "genre_ballet", "genre_modern_contemporary"]
# for key in check_boxes:
#     driver.find_element_by_name(key).click()
# sleep(5)
# driver.find_element_by_xpath(
#     '//html/body/a/div/div/form/table/tbody/tr[19]/td/input').click()
# # data = driver.find_element(By.NAME, 'genre_performance').click()
# # print(data)
# # sleep(30)
