# -*- coding: utf-8 -*-
"""
Created on Tue May 25 21:31:42 2021

@author: lmx
"""

from pycocotools.coco import COCO
import numpy as np
import matplotlib.pyplot as plt

annfile = './BSD.json'

coco = COCO(annfile)

cats = coco.loadCats(coco.getCatIds())
cat_nms = [cat['name'] for cat in cats ]
print('number of categories:', len(cat_nms))
print('COCO categories: \n',cat_nms)

number_img = []
number_bbox = []

for cat_name in cat_nms:
    catId = coco.getCatIds(catNms=cat_name)
    imgId = coco.getImgIds(catIds = catId)
    annId = coco.getAnnIds(catIds=catId)
    
    print("{<15} {:<6d} {:<10d}".format(cat_name, len(imgId),len(annId)))
    
    number_img.append(len(imgId))
    number_bbox.append(len(annId))
    
bar_width = 0.3

y1 = number_img
y2 = number_bbox

x = np.arange(5)

str1 = cat_nms

for a, b in zip(x,y1):
    plt.text(a,b+0.05,'%.0f' %b,ha = 'center',va = 'bottom',fontsize = 10)
    
for a, b in zip(x,y2):
    plt.text(a+bar_width,b+0.5,'%.0f' %b,ha = 'center',va = 'bottom',fontsize = 10)
    
#柱状图绘制
p1 = plt.bar(x, height=y1, width=0.3,label='image',tick_label=str1)
p1 = plt.bar(x+bar_width, height=y2, width=0.3,label='bbox',tick_label=str1)

plt.figure(num = 1)
plt.legend()
plt.title('class_status')

plt.savefig('柱状统计图')

#饼状图绘制
plt.figure(num=2,figsize=(6,6))
explode=[0.01,0.01,0.01,0.01,0.01]
plt.pie(number_img,explode=explode,labels=str1,autopct='%1.1f%%')
plt.title('image_numbers')
plt.savefig('images统计饼状图')

plt.figure(num=3,figsize=(6,6))
explode=[0.01,0.01,0.01,0.01,0.01]
plt.pie(number_bbox,explode=explode,labels=str1,autopct='%1.1f%%')
plt.title('bbox_numbers')
plt.savefig('bbox统计饼状图')

plt.show()
