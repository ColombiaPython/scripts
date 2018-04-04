# -*- coding: utf-8 -*-
"""PyCon Colombia 2018 tweets wordcloud"""

# Standard library imports
from os import path

# Third party imports
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS

HERE = path.dirname(__file__)
FILE_IN = path.join(HERE, 'tweet_texts.txt')
FILE_OUT = path.join(HERE, 'pycon_wordcloud.png')
STOP_ES = path.join(HERE, 'stopwords_spanish.txt')
MASK = path.join(HERE, "python_mask.png")
STOP_EXTRA = ["PyConColombia2018", "pyconcolombia", "twitter", "pic",
              "Pycon2018", "Python", "https", "PyCon2018pic", "ThePSF",
              "PyConColombia2019", "PyCon", "ColombiaPython", "bit", "ly",
              "goo", "gl"]
BW = "white"

# Read files
text = open(FILE_IN).read()
python_mask = np.array(Image.open(MASK))
with open(STOP_ES) as f:
    stopwords = set(f.read().split())

# Add stopwords
stopwords.update(STOPWORDS)
stopwords.update(STOP_EXTRA)


# Generate word cloud
wc = WordCloud(background_color=BW,
               max_words=500,
               mask=python_mask,
               width=3000,
               height=3033,
               stopwords=stopwords)
wc.generate(text)

# Store to file
wc.to_file(FILE_OUT)

# show
plt.imshow(wc, interpolation='bilinear')
plt.axis("off")
plt.show()