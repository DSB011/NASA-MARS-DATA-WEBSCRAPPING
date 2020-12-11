# WEBSCRAPING NASA MARS DATA & WEB APPLICATION DEVELOPMENT

## Overview:
Scraped the [NASA Mars News Site](https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest) and collected the latest News Title and Paragraph Text using MongoDB and Flask application.
JPL Mars Space Images - Featured Image: Used the url for [JPL Featured Space Image](https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars)to scrape the image by using splinter to navigate the site and find the image url for the current Featured Mars Image.<br>

<img src = "https://raw.githubusercontent.com/DSB011/NASA-MARS-DATA-WEBSCRAPPING/master/Images/mission_to_mars.png">

## Scrapped website using Jupyter Notebook, Beautifulsoup, Pandas and Splinter

[NASA Mars News Site](https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest)<br>
* Scarpped using Beautiful Soup<br><br>

[JPL Featured Space Image](https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars)<br>
Used splinter to navigate the site and find the image url for the current Featured Mars Image and assigned the url string to a variable called featured_image_url.<br><br>

[Mars Weather twitter account](https://twitter.com/marswxreport?lang=en)<br>
Scraped the latest Mars weather tweet from the page. Saved the tweet text for the weather report as a variable called mars_weather. <br><br>

[Mars Facts Webpage](https://space-facts.com/mars/)<br>
* Used Pandas to scrape the table containing facts about the planet including Diameter, Mass, etc.<br>
* Use Pandas to convert the data to a HTML table string<br>

[USGS Astrogeology site](https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars)<br>
* Obtained high resolution images for each of Mar's hemispheres. <br>
* Used Python dictionary to store the data using the keys img_url and title.<br>
* Appended the dictionary with the image url string and the hemisphere title to a list. This list contains one dictionary for each hemisphere.<br>

## Website Developed Using MongoDB, Flask, Bootstrap

Created a new HTML page showing the information scraped from the aforementioned URLs.

* Converted my Jupyter notebook into a Python script called scrape_mars.py with a function called scrape to execute and return one Python dictionary containing all of the scraped data.
* Created a route called /scrape to import the scrape_mars.py script and call the scrape function.
* Stored the return value in Mongo as a Python dictionary.
* bCreated a root route / that will query the Mongo database and pass the Mars data into an HTML template to display the data.
* Created a the HTML file index.html that will take the Mars data dictionary and display all of the data in the appropriate HTML elements.
* Used Bootstrap to structure the HTML website.

## Tech Environment Used:
Flask Application, Pandas, Jupyter Notebook, Beautifulsoup, Splinter, HTML, Bootstrap, MongoDB.
