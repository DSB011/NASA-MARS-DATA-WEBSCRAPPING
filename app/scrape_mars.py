from bs4 import BeautifulSoup as bs
from splinter import Browser
import pandas as pd
import datetime as dt

executable_path = {"executable_path": "/usr/local/bin/chromedriver"}
browser = Browser("chrome", **executable_path, headless=False)

def mars_news(browser):
    # Visit the NASA MARS News website
    url = "https://mars.nasa.gov/news/"
    browser.visit(url)

    browser.is_element_present_by_css("ul.item_list li.slide", wait_time=0.5)
    html = browser.html
    news_soup = bs(html, "html.parser")

    try:
        slide_element = news_soup.select_one("ul.item_list li.slide")
        slide_element.find('div', class_="content_title")

        news_title = slide_element.find('div', class_="content_title").get_text()
        news_p = slide_element.find('div', class_="article_teaser_body").get_text()
    except AttributeError:
        return None, None
    return news_title, news_p

#################################################
# JPL Mars Space Images - Featured Image
#################################################

def featured_image(browser):

    url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
    browser.visit(url)

    image_button = browser.find_by_id("full_image")
    image_button.click()

    browser.is_element_present_by_text("more info", wait_time=1)
    more_info_box = browser.find_link_by_partial_text("more info")
    more_info_box.click()

    html = browser.html
    image_soup = bs(html, "html.parser")

    img = image_soup.select_one("figure.lede a img")
    try:
        img_url = img.get("src")
    except AttributeError:
        return None
    img_url = f"https://www.jpl.nasa.gov{img_url}"
    return img_url
    
#################################################
# Mars Facts
#################################################

def mars_facts():
    try:
        mars_facts_df = pd.read_html("https://space-facts.com/mars/")[0]
    except BaseException:
        return None
    mars_facts_df.columns = ["Description", "Value"]
    mars_facts_df.set_index("Description", inplace=True)
    return mars_facts_df.to_html(classes="table table-striped table-hover")

#################################################
# Mars Hemispheres
#################################################

def mars_hemisphere(browser):
    url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(url)

    hemisphere_image_urls = []
    hemi_links = browser.find_by_css("a.product-item h3")
    for item in range(len(hemi_links)):
        hemisphere = {}
        
        browser.find_by_css("a.product-item h3")[item].click()
        sample_element = browser.find_link_by_text("Sample").first
        hemisphere["img_url"] = sample_element["href"]
        hemisphere["title"] = browser.find_by_css("h2.title").text

        hemisphere_image_urls.append(hemisphere)

        browser.back()
    return hemisphere_image_urls

def scrape_hemi(html_text):
    hemi_soup = bs(html_text, "html.parser")
    try:
        title_ele = hemi_soup.find("h2", class_="title").get_text()
        sample_element = hemi_soup.find("a", text="Sample").get("href")
    except AttributeError:
        title_ele = None
        sample_element = None
    hemisphere = {
        "title": title_ele,
        "img_url" : sample_element
    }
    return hemisphere

def scrape():
    executable_path = {"executable_path": "/usr/local/bin/chromedriver"}
    browser = Browser("chrome", **executable_path, headless=False)
    news_title, news_p = mars_news(browser)
    img_url = featured_image(browser)
    facts = mars_facts()
    hemisphere_image_urls = mars_hemisphere(browser)
    timestamp = dt.datetime.now()

    data_dict = {
        'news_title': news_title,
        'news_p' : news_p,
        "featured_image" : img_url,
        "facts" : facts,
        "hemisphere" : hemisphere_image_urls,
        "last modified" : timestamp
    }
    browser.quit()
    return data_dict

if __name__ == "__main__":
    print(scrape())




        






    











        












   

    




