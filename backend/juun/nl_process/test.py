import sys
from konlpy.tag import Kkma
from wordcloud import WordCloud, STOPWORDS
import numpy as np
from PIL import Image
from icecream import ic
import matplotlib.pyplot as plt
import platform
from nl_prcs.nl_prcs.models import FileDTO, Reader, Printer, Scraper

# kkma = Kkma()
# ic(kkma.pos('한국어 분석을 시작합니다 재미있어요~~'))
context = './data/'

text = open('./data/09. alice.txt').read()
ic(type(text))
alice_mask = np.array(Image.open('./data/09. alice_mask.png'))
ic(type(alice_mask))
#
stopwords = set(STOPWORDS)
stopwords.add("said")

path = "c:/Windows/Fonts/malgun.ttf"
from matplotlib import font_manager, rc
if platform.system() == 'Darwin':
    rc('font', family='AppleGothic')
elif platform.system() == 'Windows':
    font_name = font_manager.FontProperties(fname=path).get_name()
    rc('font', family=font_name)
else:
    print('Unknown system... sorry~~~~')

plt.figure(figsize=(8, 8))
plt.imshow(alice_mask, cmap=plt.cm.gray, interpolation='bilinear')
plt.axis('off')
# plt.show()

wc = WordCloud(background_color='white', max_words=2000, mask=alice_mask,
              stopwords = stopwords)
wc = wc.generate(text)
# ic(wc.words_)
plt.figure(figsize=(12, 12))
plt.imshow(wc, interpolation='bilinear')
plt.axis('off')
plt.show()