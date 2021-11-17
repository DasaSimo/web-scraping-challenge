# Mission to Mars : web-scraping-challenge

In this assignment was created a web application that scrapes various websites for data related to the Mission to Mars and displays the information in a single HTML page. 
## Step 1 - Scraping

For initial scraping were used Jupyter Notebook, BeautifulSoup, Pandas, and Requests/Splinter.



### NASA Mars News

* Jupyter Notebook file called `mission_to_mars.ipynb` contains all of the scraping and analysis tasks. 
* We scraped  the [Mars News Site](https://redplanetscience.com/) to collect the latest News Title and Paragraph Text. Obtained data were stored in a variables title (new title) and par (news paragraph).


### JPL Mars Space Images - Featured Image

* We referenced the url for the Featured Space Image site [here](https://spaceimages-mars.com).

* Splinter was used to navigate the site and find the image url for the current Featured Mars Image.  The url string is assigned into a variable called `featured_image_url`.


### Mars Facts

* From the webpage the Mars Facts  [here](https://galaxyfacts-mars.com) using Pandas was scraped the table containing the facts about the planet including Diameter, Mass, Moons, Distance from Sun, Length of Year and Temperature.

* We used Pandas enviroment to convert the data to a HTML table string .

### Mars Hemispheres

* The astrogeology site [here](https://marshemispheres.com/) was the place to obtain high resolution images for each of Mar's hemispheres.

* Both the image url string for the full resolution hemisphere image, and the Hemisphere title containing the hemisphere name were stored using a Python dictionary( the keys `img_url` and `title`).
* Final list contains one dictionary for each hemisphere.


## Step 2 - MongoDB and Flask Application

Using MongoDB with Flask templating we created a new HTML page that displays all of the information that was scraped from the URLs above.

* First  Jupyter notebook was converted into a Python script called `scrape_mars.py` with a function called `scrape` that executed all of your scraping code from above and return one Python dictionary containing all of the scraped data.

* Next,  a route called `/scrape` was created to import the `scrape_mars.py` script and call the `scrape` function.

* A root route `/` was created and used for querying the Mongo database and pass the mars data into an HTML template to display the data.

* HTML file called `index.html` was used to take the mars data dictionary and display all of the data in the appropriate HTML elements.
