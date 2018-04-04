# -*- coding: utf-8 -*-
"""PyCon Colombia 2018 tweets!"""

# Standard library imports
import io
import os

# Third party imports
from bs4 import BeautifulSoup


HERE = os.path.abspath(os.path.dirname(__file__))
FILE_IN = os.path.join(HERE, '#PyConColombia2018_Twitter.html')
FILE_OUT = os.path.join(HERE, 'tweet_texts.txt')

# Load data
with io.open(FILE_IN, 'r') as f:
    html_doc = f.read()

# Process data
soup = BeautifulSoup(html_doc, 'html.parser')
tweet_divs = soup.find_all('div', 'js-tweet-text-container')
texts = [tweet_div.text for tweet_div in tweet_divs]

# Save data
with io.open(FILE_OUT, 'w', encoding='utf-8') as f:
    html_doc = f.write(''.join(texts))
