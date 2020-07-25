# Web Scraping and Exploratory Data Analysis on the food scene in Mumbai, India

## Table of Contents :
* [Introduction](https://github.com/ritik-k/zomato_mumbai#introduction-)
* [Code and Resources Used](https://github.com/ritik-k/zomato_mumbai#code-and-resources-used-)
* [Data Collection](https://github.com/ritik-k/zomato_mumbai#data-collection-)
* [Findings](https://github.com/ritik-k/zomato_mumbai#findings-)
  * [Summary Statistics](https://github.com/ritik-k/zomato_mumbai#summary-statistics-)
  * [Geographic Statistics](https://github.com/ritik-k/zomato_mumbai#geographic-statistics-)
  * [Wordclouds](https://github.com/ritik-k/zomato_mumbai#wordclouds)
  
## Introduction :
### Zomato is a website where users can rate and review the restaurants they've been to. As a self proclaimed "foodie", I wanted to find out more about the experience people have in the restaurants in my city. The unique food culture of Mumbai and the growing number of restaurants and cuisines is what attracted me to inspect the data to get some insights. Data has been scraped from the [Best Restaurants in Mumbai](https://www.zomato.com/mumbai/best-restaurants?page=1) list using Scrapy.

## Code and Resources Used :

#### Python Version : 3.6.10
#### Libraries Used : pandas, numpy, matplotlib, seaborn, re, scrapy, wordcloud, descartes, geopandas
#### Data : [Best Restaurants in Mumbai](https://www.zomato.com/mumbai/best-restaurants?page=1)

## Data Collection :
### Data has been scraped in two phases from Zomato using two different Scrapy spiders. Spider 1 scrapes the restaurant Name, Category, Cuisine, Rating, Number of Reviews, Cost for 2, etc. Spider 2 scrapes the Names and the GPS co-ordinates of the restaurants.
### A total of 1050 restaurants have been scraped.

![scraping sample image](https://raw.githubusercontent.com/ritik-k/zomato_mumbai/master/zomato/images/zom.png)

## Findings :

### Summary Statistics :

#### These are the general summary statistics for restaurants in Mumbai. We can see in the below graphs that most of the restaurants have an average rating of 4.0 - 4.6, and majority have a cost for 2 of less than 1000 Rs.

![rating histogram](https://raw.githubusercontent.com/ritik-k/zomato_mumbai/master/zomato/images/rating_hist.png)

![cost histogram](https://raw.githubusercontent.com/ritik-k/zomato_mumbai/master/zomato/images/cost_hist.png)

#### Now we will look at the 10 most expensive restaurants of Mumbai. As expected, most of these restaurants are located in 5 Star Hotels.

![10 expensive restaurants](https://raw.githubusercontent.com/ritik-k/zomato_mumbai/master/zomato/images/top_exp.png)

#### At a bargain - The 10 cheapest restaurants in top 100 restaurants of Mumbai.
 
![cheap in top 100](https://raw.githubusercontent.com/ritik-k/zomato_mumbai/master/zomato/images/cheap_t100.png)

#### Now we will look at the most popular locations, i.e. locations with the most number of restaurants.

![popular locations](https://raw.githubusercontent.com/ritik-k/zomato_mumbai/master/zomato/images/pop_loc.png)

#### Where are the highest rated restaurants located?
#### We've seen the most popular locations but what about the locations that have the highest rated restaurants. We consider the top 100 restaurants here.

![top 100 restaurants locations](https://raw.githubusercontent.com/ritik-k/zomato_mumbai/master/zomato/images/high_rated_loc.png)

#### Let us look at the most popular cuisines. From the below plot it is clear that Mumbaikars prefer North Indian over any other cuisine.

![popular cuisines](https://raw.githubusercontent.com/ritik-k/zomato_mumbai/master/zomato/images/pop_cuisine.png)

#### Lastly, we will check out the summary statistics of restaurant categories.

![popular categories](https://raw.githubusercontent.com/ritik-k/zomato_mumbai/master/zomato/images/pop_cate.png)

![cost for 2 categories](https://raw.githubusercontent.com/ritik-k/zomato_mumbai/master/zomato/images/cost_cate.png)

#### The above graphs suggest that Casual Dining and Quick Bites are the two most popular restaurant categories in Mumbai.

#### As per the second graph, Fine Dining is the most expensive category, as expected, and it is followed by Lounge, Bar, Brewery and Pub; all of which serve liquor, driving the price up.

#### This concludes our summary statistical findings. Further detailed analysis on cuisines and locations can be found in the link given at the bottom.

### Geographic Statistics :

#### The second spider scraped the GPS co-ordinates for restaurants which are plotted on the map of Mumbai. The Mumbai map is created using a shape file which can be obtained online.

#### Average Rating :
![map for avg rating](https://raw.githubusercontent.com/ritik-k/zomato_mumbai/master/zomato/images/top_1000.png)

#### It seems that the average ratings are distributed throughout Mumbai. Most of the restaurants are rated between 4.0 - 4.4 .

#### Cost for 2 ( in Rs. ) :
![map for cost](https://raw.githubusercontent.com/ritik-k/zomato_mumbai/master/zomato/images/cost_map.png)

### Wordclouds:

#### Lastly we will look at the wordclouds of the restaurant names and locations. Wordclouds have been created as visual representation of data tends to have an impact and generates interest amongst the audience.

#### Restaurant Names :
![name wordcloud](https://raw.githubusercontent.com/ritik-k/zomato_mumbai/master/zomato/images/names_wc.png)

#### Locations :
![location wordcloud](https://raw.githubusercontent.com/ritik-k/zomato_mumbai/master/zomato/images/loc_wc.png)

___
### Usage :
#### This project is best viewed in a notebook viewer, which can be accessed [here](https://nbviewer.jupyter.org/github/ritik-k/zomato_mumbai/blob/master/zomato/ipynb/analysis.ipynb). In this notebook, you will find a walk through of the work done, detailed analysis and the respective code.

### Note :
#### This is a personal project made for non-commercial, educational uses ONLY. This project will not be used to generate any promotional or monetary value for me, the creator, or the user.