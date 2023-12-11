# [Wildfires Between 2012 - 2022 in Washinton State](https://kya-rice.github.io/Wildfires-Between-2012-2022/index.html)

## Project Description
### This interactive map uses wildfire data for the state of Washington by county and contains a choropleth map where each county is classified and shaded by the number of wildfires that were within that county. The user can hover over counties in Washington state and get the name of that county, and if the user clicks on one of the counties it will bring up the total acres burned within that county to further express the levels of severity of wildfires in each county using a more cumulative statistic. It will also display the 3 most common causes for wildfires within that county once the user clicks on a specific county. We believe including total acres burned and common causes for wildfires within that county are important statistics that accompany the choropleth visualization and could uncover possible correlations. The user is also able to filter which years they want to look at from 2012 to 2022, and there's also an option to include all data within that 10-year period. This process is done by aggregating individual wildfire data for each county in order to display these statistics on the county-wide level. 

## Project Goal
### There's a lot of interactive maps showing wildfire data available to the public, so we wanted to create our own using the front end programming skills that we've learned in this class. Through our interactive map we hope to provide an effective and interactive visualization for educational purposes, where we draw inspiration from different aspects from many other wildfire maps and interactive visualizations. The summary statistics we chose to display (total acres burned and 3 most common causes) for each county provide a more in-depth summary to the user of the severity of the wildfires within that county, compared to just a choropleth map that has different classifications based on the number of wildfires. The year-choosing function is an important part of the interactive aspect of this map so that users can compare how the statistics compare for each county throughout the years, being able to see how much the distribution of wildfires has shifted throughout the years, if any at all.

## Application URL:

## Screenshots: (Basemap, hovering over county, clicking on county to bring up summary statistics)

## Main Functions
### The main functions used for this project are mostly ones that we've learned in this class, primarily for initializing a basemap using MapBox access tokens, using a mouse hover function that will display the county name the user is hovering over along with its total wildfire count, and a mouse click function that will display the total acres burned for whichever county gets clicked on.
### However, we've also introduced some concepts not related to the content of this course, such as a year selecting function where the user can select certain years that they want to see and the map and associated data will change with whichever year they select. We also utilized some python code that helps with data cleaning where we create a new geojson file that has each county's individual informaton such as the points where each wildfire was located at and each county's total acres burned. This format is much easier for our purpose since we want to map the data on the county level, and having each county be its own feature with its own associated data is much easier to use. 

## Data Sources
### For our wildfire data, we used a dataset from the Washington State Department of Natural Resources Open Data that contains wildfire statistics from 2008 - present. We edited this geojson file to only include data from the past 10 complete years, 2012 - 2022. For the county boundaries we pulled a geojson file from the Washington Geospatial Open Data Portal that just contains the county boundaries for each county in Washington state, along with the county names. The rest of the datasets we used in this project we created in order to filter the data down to specific years and focusing on specific attributes for each county.

## Applied Libraries
### The primary library we used to make this interactive map possible was mapbox gl js, the JavaScript library that we used all quarter in order to make our maps interactive and customizable using our own code. In the process of cleaning our data and filtering it down to the specific entries that we need, we utilized the following python libraries: pandas, geopandas, shapely, and datetime. We primarily used the functions inside geopandas to work with our newly created geodataframe that contained all the information we needed, however there were some functions within pandas that were helpful in aggregating data within our geodataframe. Also, shapely was used to turn each county feature as a multipoint geometry, that way each wildfire instance is grouped with the county that it was located in. We also used datetime to convert the default date column from the original dataset to a cleaner format that would make it easier for us to select by date.

## Acknowledgements
### Below are some individuals and organizations that we'd like to acknowledge:
#### Professor Bo Zhao for instructing this course and facilitating the learning of the concepts that were used in this project and providing material on these concepts.
#### Our TA, Liz Peng for reviewing and giving feedback on the lab assignments where we learned the core concepts of this course and being available to answer coding-related questions.

## Wildfire Data Used
https://data-wadnr.opendata.arcgis.com/datasets/wadnr::dnr-fire-statistics-2008-present/explore?location=47.249274%2C-120.769400%2C7.97
- Properties of dataset:
  - Acres burned
  - Start date
  - County
  - Longitude
  - Latitude 
  - Fire cause 


https://geo.wa.gov/datasets/12712f465fc44fb58328c6e0255ca27e/explore
- WA county boundaries dataset
  - Hovering over a dataset will just display the name of the county, similar to what we did in lab 4.
  - Clicking on a county will show the total acres burned and the top 3 most common fire causes and their numbers.
  - Bar that has a feature with buttons where you can select years between 2012-2022
    - I have code on how to do this
