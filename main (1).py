#!/usr/bin/env python
# coding: utf-8

# In[101]:


import requests
from bs4 import BeautifulSoup
import csv


# In[102]:


urls = ['https://www.brownells.com/rifle-parts/bolt-parts/bolt-carrier-parts/bolt-carriers/m16-sand-cutter-bolt-carrier-prod118544.aspx','https://www.brownells.com/rifle-parts/receiver-parts/receivers/lower-receivers/sr-15-lower-receiver-complete-5-56-sku100027982-120372-222762.aspx?sku=100027982','https://www.brownells.com/reloading/bullets/rifle-bullets/6-5mm-264-147-grain-eld-match-bullets-prod99022.aspx','https://www.brownells.com/rifle-parts/receiver-parts/receivers/lower-receivers/ar-15-mars-l-stripped-lower-receiver-ambidextrous-5-56-prod132418.aspx','https://www.brownells.com/reloading/primers/pistol-primers/pistol-primers-prod35322.aspx','https://www.brownells.com/firearms/handguns/semi-auto/sp5k-pdw-9mm-30-1-prod137836.aspx','https://www.brownells.com/shooting-accessories/flashlights-accessories/flashlight-accessories/hot-button-prod138031.aspx','https://www.brownells.com/optics-mounting/rings-mounts-amp-bases/mount-sets/condition-one-modular-mounts-prod128657.aspx']
product_title=[]


# In[103]:


for url in urls:
    response = requests.get(url).text
    soup = BeautifulSoup(response, "lxml")
    for link in soup.find_all('h1',class_="mbm"):
        print(link.text)
        product_title.append(link.text)


# In[104]:



product_title


# In[105]:


with open('file.csv', 'w') as f:
    write = csv.writer(f) 
    write.writerows(product_title) 


# In[ ]:





# In[94]:


for link in soup.find_all('div',class_="hidden editable skuScroll", id="contentDetails218081"):
    print(link)


# In[ ]:





# In[ ]:




