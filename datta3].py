import time
import requests
from time import sleep
import re, requests, csv
from bs4 import BeautifulSoup as bs
from selenium.webdriver.common.keys import Keys
import pandas as pd
from selenium import webdriver
keys = Keys()


url = "https://brand.naver.com/skinfood/products/7926935977"
driver = webdriver.Chrome(executable_path='/Users\SS\Downloads\chromedriver-win64\chromedriver-win64')
driver.get(url)

page = requests.get("https://brand.naver.com/skinfood/products/7926935977")