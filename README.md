# Visualizing Wildfires Between 2012 - 2022

## This interactive dashboard uses wildfire data for the state of Washington by county and contains a choropleth map where each county is classified and shaded by the number of wildfires that were within that county. If the user clicks on one of the counties it will bring up the total acres burned within that county, as well as the 3 most common fire causes and their counts. The user is also able to filter which years they want to look at from 2012 to 2022, and there's also an option to include all data within that 10-year period. This process is done by aggregating individual wildfire data for each county in order to display these statistics on the county-wide level. 

There is a large amount of wildfire maps and interactive dashboards out there, so we wanted to create our own using the front end programming skills that we've learned in this class. Through our map-based dashboard we hope to provide an effective and interactive visualization for educational purposes, where we draw inspiration from different aspects from many other wildfire maps and interactive visualizations. The summary statistics we chose to display for each county provide a summary to the user of the severity of the wildfires within that county, that way the user has some numerical figures to accompany the choropleth classification that county was placed into. The year-choosing function is an important part of the interactive aspect of this dashboard so that users can compare how the statistics compare for each county throughout the years, being able to see how much the distribution of wildfires has shifted throughout the years, if any at all.


## Wildfire data set we could use 
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
