#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Dependencies

from splinter import Browser
from bs4 import BeautifulSoup as soup
from webdriver_manager.chrome import ChromeDriverManager

import pandas as pd


# In[2]:


executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)


# In[3]:


# Visit the mars nasa news site
url = 'http://redplanetscience.com'
browser.visit(url)

# Optioinal delay for loading the page
browser.is_element_present_by_css('div.list_text', wait_time=1)


# In[4]:


# set up the HTML parser
html = browser.html
news_soup = soup(html, 'html.parser')
slide_elem = news_soup.select_one('div.list_text')


# In[5]:


# print(news_soup)


# In[6]:


# print(slide_elem)


# In[7]:


# Show the HTML containing the first headline title
slide_elem.find('div', class_='content_title')


# In[8]:


# Use the parent element to find the first `a` tag and save it as `news_title`
news_title = slide_elem.find('div', class_='content_title').get_text()
news_title


# In[9]:


# slide_elem.find("div", class_='content_title').get_text()


# In[10]:


# Use the parent element to find the paragraph text
news_p = slide_elem.find('div', class_='article_teaser_body').get_text()
news_p


# ### Featured Images

# In[11]:


# Visit URL
url = 'https://spaceimages-mars.com/'
browser.visit(url)


# In[12]:


# Find and click the full image button
full_image_elem = browser.find_by_tag('button')[1]
full_image_elem.click()


# In[13]:


# Parse the resulting html with soup
html = browser.html
img_soup = soup(html, 'html.parser')
img_soup


# In[14]:


# Find the relative image url
img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')
img_url_rel


# In[15]:


# Use the base URL to create an absolute URL
img_url = f'https://spaceimages-mars.com/{img_url_rel}'
img_url


# In[16]:


### Gathering data from Mars Facts webpage


# In[17]:


df = pd.read_html('https://galaxyfacts-mars.com')[0]
df.columns=['description', 'Mars', 'Earth']
df.set_index('description', inplace=True)
df


# In[18]:


df.to_html()


# In[19]:


### Challenge Portion


# In[20]:


# 1. Use Browser to visit the URL
url = 'https://marshemispheres.com/'

browser.visit(url)


# In[21]:


# 2. Create a list to hold the images and titles.
hemisphere_image_urls = []


# In[22]:


# 3. Write code to retrieve the image urls and titles for each hemisphere.
# Set up parser
hemi_html = browser.html
hemi_soup = soup(hemi_html, 'html.parser')

items = hemi_soup.find_all('div', class_='item')

# main_url = 'https://marshemispheres.com/'

# Loop to scrape hemisphere information
for x in items:
    hemisphere = {}
    titles = x.find('h3').text
    
    link_ref = x.find('a', class_='itemLink product-item')['href']
    
    browser.visit(url + link_ref)
    
    image_html = browser.html
    image_soup = soup(image_html, 'html.parser')
    download = image_soup.find('div', class_='downloads')
    img_url = url + download.find('a')['href']
    
    print(titles)
    print(img_url)
    # print(download)
    
    # append list
    hemisphere['img_url'] = img_url
    hemisphere['title'] = titles
    hemisphere_image_urls.append(hemisphere)
    browser.back()


# In[23]:


# 4. Print the list that holds the dictionary of each image
hemisphere_image_urls


# In[24]:


browser.quit()

