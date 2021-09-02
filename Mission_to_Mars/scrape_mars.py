from splinter import Browser
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import time


def scrape():
    # browser = init_browser()
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)

    # get NASA Mars News
    url = 'https://redplanetscience.com/'
    browser.visit(url)

    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    title= soup.find_all('div', class_='content_title')[0].text
    par=soup.find_all('div', class_='article_teaser_body')[0].text


    # get JPL Mars Space Images - Featured Image
    url = 'https://spaceimages-mars.com/'
    browser.visit(url)   
    browser.links.find_by_partial_text('FULL IMAGE').click()    

    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    image = soup.find_all('img', class_='fancybox-image')[0]["src"]
    featured_image_url = url + image


    url = 'https://galaxyfacts-mars.com/#'
    tables = pd.read_html(url)
    df = tables[0]
    df.columns = ['Description', 'Mars', 'Earth']

    html_table = df.to_html(index=False)
    html_table = html_table.replace('\n', '')

    url = 'https://marshemispheres.com/'
    browser.visit(url)


    # get hemisphere names and images urls
    hemisphere_image_urls = []

    for hem_num in range (4):
        partial_hem = browser.links.find_by_partial_text('Enhanced')
        name_hem = partial_hem[hem_num].text
        partial_hem[hem_num].click()
    
        html = browser.html
        soup = BeautifulSoup(html, 'html.parser')
        
        img_loc = soup.find('li')
        img_hem = url + img_loc.a['href']
    
        hem_dic = {"title": name_hem, "img_url": img_hem}
        hemisphere_image_urls.append(hem_dic)  
        browser.back()

    Mars_info = {
        'news_title': title, 
        'news_par':par,
        'featured_image' : featured_image_url,
        'table_facts': html_table,
        'hemispheres_info': hemisphere_image_urls
    }
   
    # Quit the browser
    browser.quit()

    return Mars_info



