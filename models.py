import json
import os
import sys
import yaml
from datetime import datetime, timedelta
import logging
import requests
import http.client
from lxml import html, etree
from bs4 import BeautifulSoup


class models(object):

    def __init__(self):
        self.submitted_links = set()

    def add_link(self, link):
        self.submitted_links.add(link)

    def process_detail(self):
        ls = []
        if self.submitted_links:
            for s in self.submitted_links:
                dt = {}
                dt['link'] = s
                page = requests.get('{}'.format(s))
                tree = html.fromstring(page.content)
                soup = BeautifulSoup(page.content, 'html.parser')
                desc = soup.find(id="description")
                dt['description'] = desc.text

                prod = soup.find("li", class_="item product")
                dt['product'] = prod.text
                prc = soup.find(
                    "div", class_="price-box price-final_price")
                prc_really = prc.find("span", class_='price')
                dt['price'] = prc_really.text
                ls.append(dt)
        return ls
