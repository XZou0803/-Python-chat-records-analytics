# -*- coding: utf-8 -*-
pwd #Check the directory

import os
os.chdir('/Users/zouxin/Downloads') 

# Import usefull packages
from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = "all"
import re
import matplotlib.pyplot as plt
import jieba
import wordcloud
import seaborn as sns
import numpy as np
from PIL import Image
from scipy.misc import imread

# Read the contexts 
fl=f.readlines()
for i in fl:
    print(i)

# Noticed that the first six lines are useless, delete them
del fl[:7]
for i in fl:
    print(i)

# Noticed that the real usefull contexts are appeared every three lines(as data-context-blank)
sample1=fl[2::3]
for i in sample1:
    print(i)

strf=' '.join(sample1)
for i in sample1:
    print(i)
    
# Remove the confusing contexts such as Emoji and nicknames 
list1 = re.findall(r'/.{2,3}', strf)
list2 = re.findall(r'\[.+?\]', strf)
set1 = set(list1)
set2 = set(list2)
for item in set1:
    strf = strf.replace(item, '')
for item in set2:
    strf = strf.replace(item, '')

# This package is useful for cut Chinese sentences into words
word_list = jieba.cut(strf, cut_all=True)
word = ' '.join(word_list)

# Then we can start to generate wordclouds
# For year 2010-2011
pic = imread('/Users/zouxin/Downloads/timg.png')
wc = wordcloud.WordCloud(mask=pic,font_path='/Library/Fonts/Songti.ttc',width=1000, height=500, background_color='white').generate(word)
sns.set_context("poster")
plt.imshow(wc)
plt.axis('off')
plt.savefig('wc_0.png',dpi=200)
plt.show()

# The following is for year 2016-2017
f1=open('/Users/zouxin/Downloads/shifu.txt')
fl_1=f1.readlines()

del fl_1[:7]
for i in fl_1:
    print(i)

sample2=fl_1[2::3]
for i in sample2:
    print(i)

strf_1=' '.join(sample2)

list3 = re.findall(r'/.{2,3}', strf_1)
list4 = re.findall(r'\[.+?\]', strf_1)
set3 = set(list3)
set4 = set(list4)
for item in set3:
    strf_1 = strf_1.replace(item, '')
for item in set4:
    strf_1 = strf_1.replace(item, '')

word_list_1 = jieba.cut(strf_1, cut_all=True)
word_1 = ' '.join(word_list_1)

c_1 = imread('/Users/zouxin/Downloads/timg-2.png')
wc_1 = wordcloud.WordCloud(mask=pic_1,font_path='/Library/Fonts/Songti.ttc',width=1000, height=1000, background_color='white').generate(word_1)

sns.set_context("poster")
plt.imshow(wc_1)
plt.axis('off')
plt.savefig('wc_1.png',dpi=200)
plt.show()
